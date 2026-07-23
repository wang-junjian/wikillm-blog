#!/usr/bin/env python3
"""WikiLLM CLI: deterministic helpers for scanning, syncing, clustering,
batching, searching, and linting the wiki.  Uses only the Python 3 stdlib.

Usage:
    python3 tools/wikillm.py scan
    python3 tools/wikillm.py sync-images
    python3 tools/wikillm.py cluster
    python3 tools/wikillm.py assign
    python3 tools/wikillm.py batches
    python3 tools/wikillm.py search <query> [--top N]
    python3 tools/wikillm.py lint
    python3 tools/wikillm.py status
"""

import argparse
import hashlib
import re
import shutil
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent
RAW_POSTS = ROOT / "raw" / "posts"
RAW_IMAGES = ROOT / "raw" / "images"
WIKI = ROOT / "wiki"
WIKI_ASSETS = WIKI / "assets" / "images"
WIKI_STATE = WIKI / "_state"
MANIFEST_TSV = WIKI_STATE / "manifest.tsv"
TAXONOMY_MD = WIKI_STATE / "taxonomy.md"
ASSIGNMENTS_TSV = WIKI_STATE / "assignments.tsv"
BATCHES_DIR = WIKI_STATE / "batches"
BATCHES_TSV = WIKI_STATE / "batches.tsv"
COMPILE_RESULTS_TSV = WIKI_STATE / "compile-results.tsv"
COMPILE_LOG = WIKI_STATE / "compile.log"
PROGRESS_MD = WIKI_STATE / "progress.md"
LINT_REPORT_MD = WIKI_STATE / "lint-report.md"

# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict:
    """Parse a minimal subset of YAML frontmatter used in this repo."""
    data = {}
    m = FRONTMATTER_RE.match(text)
    if not m:
        return data
    fm = m.group(1)
    for line in fm.splitlines():
        line = line.rstrip()
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if key == "tags" or key == "categories":
            data[key] = _parse_inline_list(value)
        elif key in ("title", "type", "date", "author", "excerpt", "linkUrl"):
            data[key] = _unquote(value)
    return data


def _parse_inline_list(value: str) -> list:
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        value = value[1:-1]
    items = []
    for item in value.split(","):
        item = item.strip().strip('"').strip("'")
        if item:
            items.append(item)
    return items


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
        return value[1:-1]
    return value


def count_image_refs(text: str) -> int:
    return len(re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", text))


def extract_image_refs(text: str) -> list:
    return [p for _, p in re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", text)]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def ensure_state_dir():
    WIKI_STATE.mkdir(parents=True, exist_ok=True)
    BATCHES_DIR.mkdir(parents=True, exist_ok=True)


def read_tsv(path: Path, default=None) -> list:
    if not path.exists():
        return default if default is not None else []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()
    if not lines:
        return []
    return [line.split("\t") for line in lines]


def read_tsv_as_dicts(path: Path) -> list:
    rows = read_tsv(path)
    if not rows:
        return []
    headers = rows[0]
    return [dict(zip(headers, row)) for row in rows[1:]]


def write_tsv(path: Path, headers: list, rows: list):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\t".join(headers) + "\n")
        for row in rows:
            f.write("\t".join(str(c) for c in row) + "\n")


def log_event(message: str):
    ensure_state_dir()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(COMPILE_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


def now_iso() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def cmd_scan(_args):
    _ = _args
    ensure_state_dir()
    old_results = {}
    if COMPILE_RESULTS_TSV.exists():
        for row in read_tsv_as_dicts(COMPILE_RESULTS_TSV):
            old_results[row.get("raw_path", "")] = row.get("hash", "")

    headers = ["raw_path", "sha256", "size", "mtime", "type", "title", "date", "tags", "n_images", "status"]
    rows = []
    changed = new = unchanged = 0
    for path in sorted(RAW_POSTS.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        fm = parse_frontmatter(text)
        h = sha256_file(path)
        rel = str(path.relative_to(ROOT))
        status = "unchanged" if old_results.get(rel) == h else ("new" if rel not in old_results else "changed")
        if status == "new":
            new += 1
        elif status == "changed":
            changed += 1
        else:
            unchanged += 1
        rows.append([
            rel,
            h,
            str(path.stat().st_size),
            str(int(path.stat().st_mtime)),
            fm.get("type", ""),
            fm.get("title", ""),
            fm.get("date", ""),
            "|".join(fm.get("tags", [])),
            str(count_image_refs(text)),
            status,
        ])
    write_tsv(MANIFEST_TSV, headers, rows)
    log_event(f"scan: {len(rows)} files, new={new}, changed={changed}, unchanged={unchanged}")
    print(f"scan: {len(rows)} raw posts scanned")
    print(f"  new={new}, changed={changed}, unchanged={unchanged}")
    print(f"  manifest -> {MANIFEST_TSV.relative_to(ROOT)}")


def cmd_sync_images(_args):
    _ = _args
    ensure_state_dir()
    if not RAW_IMAGES.exists():
        print("sync-images: raw/images/ not found, nothing to sync")
        return
    copied = skipped = 0
    collisions = []
    for src in sorted(RAW_IMAGES.rglob("*")):
        if not src.is_file():
            continue
        if src.name.startswith("."):
            continue
        rel = src.relative_to(RAW_IMAGES)
        dst = WIKI_ASSETS / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        need_copy = True
        if dst.exists():
            if dst.stat().st_size == src.stat().st_size:
                # fast path: same size; could hash on doubt
                need_copy = False
        if need_copy:
            shutil.copy2(src, dst)
            copied += 1
        else:
            skipped += 1
    # collision report: same basename in different dirs
    basenames = defaultdict(list)
    for src in sorted(RAW_IMAGES.rglob("*")):
        if src.is_file() and not src.name.startswith("."):
            basenames[src.name].append(str(src.relative_to(RAW_IMAGES)))
    for name, paths in basenames.items():
        if len(paths) > 1:
            collisions.append((name, paths))
    log_event(f"sync-images: copied={copied}, skipped={skipped}, collisions={len(collisions)}")
    print(f"sync-images: copied={copied}, skipped={skipped}")
    print(f"  assets -> {WIKI_ASSETS.relative_to(ROOT)}")
    if collisions:
        print(f"  basename collisions (tree preserved): {len(collisions)}")
        for name, paths in collisions[:5]:
            print(f"    {name}: {', '.join(paths)}")
        if len(collisions) > 5:
            print(f"    ... and {len(collisions)-5} more")


def cmd_cluster(_args):
    _ = _args
    ensure_state_dir()
    manifest = read_tsv_as_dicts(MANIFEST_TSV)
    tag_counter = Counter()
    co_counter = Counter()
    per_post = []
    for row in manifest:
        tags = row.get("tags", "").split("|") if row.get("tags") else []
        tags = [t.strip() for t in tags if t.strip()]
        for t in tags:
            tag_counter[t] += 1
        for i, t1 in enumerate(tags):
            for t2 in tags[i + 1 :]:
                co_counter[tuple(sorted((t1, t2)))] += 1
        top_tags = ", ".join(tags[:3])
        per_post.append((row.get("date", ""), row.get("title", ""), row.get("raw_path", ""), top_tags))

    lines = ["# Cluster Report", ""]
    lines.append(f"Total posts: {len(manifest)}")
    lines.append(f"Unique tags: {len(tag_counter)}")
    lines.append("")
    lines.append("## Top 60 tags")
    for tag, count in tag_counter.most_common(60):
        lines.append(f"- {tag}: {count}")
    lines.append("")
    lines.append("## Top tag co-occurrences")
    for (t1, t2), count in co_counter.most_common(40):
        lines.append(f"- {t1} + {t2}: {count}")
    lines.append("")
    lines.append("## Per-post index (date | title | path | top tags)")
    for date, title, path, tops in per_post:
        lines.append(f"- {date} | {title} | {path} | {tops}")

    report = WIKI_STATE / "cluster-report.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    print(f"cluster: {len(manifest)} posts, {len(tag_counter)} tags")
    print(f"  report -> {report.relative_to(ROOT)}")


def _load_taxonomy() -> dict:
    """Return {topic_slug: {'name': str, 'seeds': [tags]}} from taxonomy.md."""
    topics = {}
    if not TAXONOMY_MD.exists():
        return topics
    current_domain = ""
    for line in TAXONOMY_MD.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("## "):
            current_domain = line[3:].strip()
        elif line.startswith("- "):
            # expected: "- Topic Name (seed tags: a, b, c)"
            body = line[2:]
            name = body
            seeds = []
            m = re.search(r"\(seed tags?[:：]\s*([^)]+)\)", body)
            if m:
                seeds = [s.strip() for s in m.group(1).split(",") if s.strip()]
                name = body[: m.start()].strip()
            slug = name.replace(" ", "-").replace("（", "-").replace("）", "")
            slug = re.sub(r"[^\w\-]", "", slug).strip("-")
            topics[slug] = {"name": name, "seeds": seeds, "domain": current_domain}
    return topics


def cmd_assign(_args):
    _ = _args
    ensure_state_dir()
    manifest = read_tsv_as_dicts(MANIFEST_TSV)
    topics = _load_taxonomy()
    if not topics:
        print("assign: taxonomy.md not found. Please create it first (see bootstrap.md).")
        sys.exit(1)

    headers = ["raw_path", "topic", "page_type", "target_pages", "size"]
    rows = []
    unassigned = 0
    for row in manifest:
        tags = set((row.get("tags") or "").lower().split("|"))
        size = int(row.get("size", "0") or 0)
        rel = row.get("raw_path", "")
        ptype = row.get("type", "article")
        assigned_topic = ""
        best_score = 0
        for slug, info in topics.items():
            seeds = {s.lower() for s in info["seeds"]}
            score = len(tags & seeds)
            if score > best_score:
                best_score = score
                assigned_topic = slug
        if not assigned_topic:
            assigned_topic = "UNASSIGNED"
            unassigned += 1

        if ptype in ("quote", "link", "note"):
            page_type = "absorbed"
            target = "-"
        elif ptype == "release":
            page_type = "practice"
            target = f"{assigned_topic}-releases"
        elif size > 60_000:
            page_type = "source"
            target = Path(rel).stem
        else:
            page_type = "concept" if best_score and "rag" in tags or "llm" in tags else "practice"
            # crude heuristic: use topic + first relevant seed
            target = f"{assigned_topic}-overview"
        rows.append([rel, assigned_topic, page_type, target, str(size)])

    write_tsv(ASSIGNMENTS_TSV, headers, rows)
    print(f"assign: {len(rows)} posts assigned")
    print(f"  unassigned={unassigned}")
    print(f"  assignments -> {ASSIGNMENTS_TSV.relative_to(ROOT)}")
    print("  Tip: review UNASSIGNED rows before running batches.")


def cmd_batches(_args):
    _ = _args
    ensure_state_dir()
    manifest = {r.get("raw_path", ""): r for r in read_tsv_as_dicts(MANIFEST_TSV)}
    assignments = read_tsv_as_dicts(ASSIGNMENTS_TSV)
    topics = _load_taxonomy()
    if not assignments:
        print("batches: assignments.tsv not found. Run 'assign' first.")
        sys.exit(1)

    # group by topic, exclude absorbed
    groups = defaultdict(list)
    for row in assignments:
        if row.get("page_type") == "absorbed":
            continue
        topic = row.get("topic", "UNASSIGNED")
        groups[topic].append(row)

    # sort within topic by date ascending
    for topic in groups:
        groups[topic].sort(key=lambda r: manifest.get(r.get("raw_path", ""), {}).get("date", ""))

    batch_id = 0
    batch_rows = []
    for topic, rows in sorted(groups.items()):
        topic_name = topics.get(topic, {}).get("name", topic)
        current = []
        current_size = 0
        for row in rows:
            size = int(row.get("size", "0") or 0)
            if size > 60_000 or (current and current_size + size > 100_000) or len(current) >= 12:
                if current:
                    batch_id += 1
                    batch_rows.append(_write_batch(batch_id, topic, topic_name, current, manifest))
                current = [row]
                current_size = size
            else:
                current.append(row)
                current_size += size
        if current:
            batch_id += 1
            batch_rows.append(_write_batch(batch_id, topic, topic_name, current, manifest))

    write_tsv(BATCHES_TSV, ["batch_id", "topic", "n_posts", "status", "session", "completed_at"], batch_rows)
    print(f"batches: {batch_id} batches generated")
    print(f"  queue -> {BATCHES_TSV.relative_to(ROOT)}")
    print(f"  briefs -> {BATCHES_DIR.relative_to(ROOT)}")


def _write_batch(bid: int, topic: str, topic_name: str, rows: list, manifest: dict):
    path = BATCHES_DIR / f"{bid:03d}-{topic}.md"
    target_pages = sorted({r.get("target_pages", "") for r in rows if r.get("target_pages")})
    lines = [
        "---",
        f"batch_id: {bid}",
        f"topic: {topic}",
        f"topic_name: {topic_name}",
        f"n_posts: {len(rows)}",
        "target_pages:",
    ]
    for tp in target_pages:
        lines.append(f"  - {tp}")
    lines.extend(["---", "", f"## 文件列表 ({len(rows)} posts)", ""])
    total = 0
    for r in rows:
        rel = r.get("raw_path", "")
        info = manifest.get(rel, {})
        total += int(info.get("size", "0") or 0)
        title = info.get("title", "")
        tags = info.get("tags", "")
        ptype = r.get("page_type", "")
        lines.append(f"- `{rel}` — {title} — type:{ptype} — tags:{tags}")
    lines.extend(["", f"**总大小**: {total} bytes", ""])
    lines.extend([
        "## 输出要求",
        "",
        "1. 阅读上述全部 raw 文件",
        "2. 写入/更新目标 wiki 页面",
        "3. 每个页面 frontmatter 的 raw_sources 列出全部来源及其 sha256",
        "4. 图片引用改为 ../assets/images/YYYY/... 相对路径",
        "5. 返回：写入文件列表、消耗的来源 hash、发现的异常",
    ])
    path.write_text("\n".join(lines), encoding="utf-8")
    return [str(bid), topic, str(len(rows)), "pending", "", ""]


def _score(query_words: list, text: str, title: str, tags: list, path: str) -> int:
    text_lower = text.lower()
    title_lower = title.lower()
    tags_lower = [t.lower() for t in tags]
    path_lower = path.lower()
    score = 0
    for w in query_words:
        score += title_lower.count(w) * 10
        score += path_lower.count(w) * 6
        score += tags_lower.count(w) * 4
        score += text_lower.count(w) * 1
    return score


def cmd_search(_args):
    _ = _args
    if not WIKI.exists():
        print("search: wiki/ not found")
        sys.exit(1)
    query = " ".join(_args.query).lower().split()
    top_n = _args.top
    results = []
    for path in sorted(WIKI.rglob("*.md")):
        rel = str(path.relative_to(WIKI))
        if rel.startswith("_state/"):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        fm = parse_frontmatter(text)
        title = fm.get("title", path.stem)
        tags = fm.get("tags", [])
        score = _score(query, text, title, tags, rel)
        if score > 0:
            # snippet
            snippet = ""
            for w in query:
                idx = text.lower().find(w)
                if idx != -1:
                    start = max(0, idx - 40)
                    end = min(len(text), idx + 80)
                    snippet = text[start:end].replace("\n", " ")
                    break
            results.append((score, rel, title, snippet))
    results.sort(key=lambda x: (-x[0], x[2]))
    for score, rel, title, snippet in results[:top_n]:
        print(f"{score:4d}  {rel}")
        print(f"      {title}")
        if snippet:
            print(f"      ...{snippet}...")
    if not results:
        print("search: no results")


def cmd_lint(_args):
    _ = _args
    ensure_state_dir()
    issues = []
    if not WIKI.exists():
        print("lint: wiki/ not found")
        sys.exit(1)

    # build slug -> file map
    pages = []
    for path in sorted(WIKI.rglob("*.md")):
        rel = str(path.relative_to(WIKI))
        if rel.startswith("_state/") or rel.startswith("assets/"):
            continue
        pages.append((rel, path))

    all_files = {rel for rel, _ in pages}
    link_targets = set()
    for rel, path in pages:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        fm = parse_frontmatter(text)
        title = fm.get("title", "")
        if not title:
            issues.append((rel, "missing title in frontmatter"))
        if "type" not in fm:
            issues.append((rel, "missing type in frontmatter"))
        # Skip raw_sources check for index/glossary/topic/concept-stub pages
        page_type = fm.get("type", "")
        is_index_page = page_type in ("index", "glossary", "topic")
        is_concept_stub = page_type == "concept" and rel.startswith("concepts/")
        if "raw_sources" not in fm and not is_index_page and not is_concept_stub:
            issues.append((rel, "missing raw_sources in frontmatter"))
        # TODO: check raw_sources hashes against manifest
        # wikilink targets
        for m in re.finditer(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", text):
            target = m.group(1).strip()
            link_targets.add(target)
            candidate = target + ".md"
            exists = False
            for r in all_files:
                if r.endswith(candidate):
                    exists = True
                    break
            if not exists:
                issues.append((rel, f"broken wikilink: [[{target}]]"))
        # image refs
        for _, img_path in re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", text):
            if img_path.startswith("http://") or img_path.startswith("https://"):
                continue
            # support ../assets/images/... or /assets/images/...
            clean = img_path.lstrip("./").lstrip("/")
            if clean.startswith("assets/images/"):
                asset = WIKI / clean
            else:
                asset = WIKI / clean
            if not asset.exists():
                issues.append((rel, f"unresolved image: {img_path}"))

    # orphans: pages not in INDEX or topic hubs or glossary
    indexed = set()
    index_path = WIKI / "INDEX.md"
    if index_path.exists():
        index_text = index_path.read_text(encoding="utf-8", errors="ignore")
        for rel in all_files:
            name = Path(rel).stem
            if name in index_text:
                indexed.add(rel)
    glossary_path = WIKI / "Glossary.md"
    glossary_text = glossary_path.read_text(encoding="utf-8", errors="ignore") if glossary_path.exists() else ""
    for rel in all_files:
        name = Path(rel).stem
        if rel in indexed or rel.startswith("topics/") or rel.startswith("timeline/") or rel in ("INDEX.md", "Glossary.md", "sources.md"):
            continue
        if name in glossary_text:
            continue
        # check inbound links
        has_inbound = False
        for other_rel, other_path in pages:
            if other_rel == rel:
                continue
            try:
                other_text = other_path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            if f"[[{name}" in other_text or f"[[{name}|" in other_text:
                has_inbound = True
                break
        if not has_inbound:
            issues.append((rel, "orphan page: no inbound wikilink and not in INDEX/Glossary/topic"))

    report_lines = ["# Lint Report", f"Generated: {now_iso()}", "", f"Total issues: {len(issues)}", ""]
    by_file = defaultdict(list)
    for rel, msg in issues:
        by_file[rel].append(msg)
    for rel in sorted(by_file):
        report_lines.append(f"## {rel}")
        for msg in by_file[rel]:
            report_lines.append(f"- {msg}")
        report_lines.append("")
    LINT_REPORT_MD.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"lint: {len(issues)} issues")
    print(f"  report -> {LINT_REPORT_MD.relative_to(ROOT)}")


def cmd_status(_args):
    _ = _args
    ensure_state_dir()
    manifest = read_tsv_as_dicts(MANIFEST_TSV) if MANIFEST_TSV.exists() else []
    batches = read_tsv_as_dicts(BATCHES_TSV) if BATCHES_TSV.exists() else []
    topics = _load_taxonomy()
    pending = [b for b in batches if b.get("status") == "pending"]
    done = [b for b in batches if b.get("status") == "done"]
    failed = [b for b in batches if b.get("status") == "failed"]
    print("WikiLLM status")
    print(f"  raw posts: {len(manifest)}")
    print(f"  taxonomy: {'present' if topics else 'missing'}")
    print(f"  batches: {len(batches)} total, {len(done)} done, {len(pending)} pending, {len(failed)} failed")
    if pending:
        by_topic = defaultdict(int)
        for b in pending:
            by_topic[b.get("topic", "?")] += 1
        print("  pending by topic:")
        for topic, count in sorted(by_topic.items(), key=lambda x: -x[1]):
            print(f"    {topic}: {count}")
    if PROGRESS_MD.exists():
        print(f"  progress -> {PROGRESS_MD.relative_to(ROOT)}")


def main():
    parser = argparse.ArgumentParser(description="WikiLLM CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("scan", help="scan raw/posts and build manifest.tsv")
    sub.add_parser("sync-images", help="sync raw/images to wiki/assets/images")
    sub.add_parser("cluster", help="generate cluster-report.md")
    sub.add_parser("assign", help="assign posts to topics")
    sub.add_parser("batches", help="generate batch briefs and queue")

    p_search = sub.add_parser("search", help="search wiki pages")
    p_search.add_argument("query", nargs="+", help="search keywords")
    p_search.add_argument("--top", type=int, default=10, help="number of results")

    sub.add_parser("lint", help="run mechanical lint")
    sub.add_parser("status", help="show compile status")

    args = parser.parse_args()
    {
        "scan": cmd_scan,
        "sync-images": cmd_sync_images,
        "cluster": cmd_cluster,
        "assign": cmd_assign,
        "batches": cmd_batches,
        "search": cmd_search,
        "lint": cmd_lint,
        "status": cmd_status,
    }[args.command](args)


if __name__ == "__main__":
    main()
