# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

WikiLLM is a system for building LLM-powered personal knowledge bases. The workflow consists of:

1. **Data Ingest**: Source documents (articles, papers, repos, datasets, images) are indexed into a `raw/` directory
2. **Wiki Compilation**: An LLM incrementally "compiles" the raw data into a wiki of markdown files with summaries, backlinks, categorized concepts, and interlinked articles — using a batch-oriented, resumable pipeline
3. **IDE**: Obsidian is used as the frontend to view raw data, compiled wiki, and visualizations
4. **Q&A**: The LLM can answer complex questions against the wiki by researching the related data
5. **Output**: Results are rendered as markdown files, Marp slides, or matplotlib images, viewable in Obsidian
6. **Linting**: LLM "health checks" find inconsistencies, impute missing data, suggest new article candidates
7. **Extra Tools**: A Python CLI under `tools/wikillm.py` for scanning, syncing images, clustering, batching, searching, and linting

## Directory Structure

The project will eventually include these key directories:

- `raw/` - Source documents and unprocessed data
  - `raw/posts/` - Markdown articles, organized by year
  - `raw/images/` - Local images, organized by year and topic subfolders
- `wiki/` - LLM-compiled markdown wiki with articles, summaries, and links
  - `wiki/concepts/` - Aggregated concept/principle pages
  - `wiki/practices/` - Aggregated practical guides and tool pages
  - `wiki/sources/` - Dedicated deep-dive pages for long-form articles
  - `wiki/topics/` - Topic hub pages that link related concept/practice/source pages
  - `wiki/timeline/` - Yearly indexes of posts
  - `wiki/visual/` - Marp slides and visualizations
  - `wiki/queries/` - Archived Q&A pages
  - `wiki/assets/images/` - Images synced from `raw/images/`, preserving the year tree
  - `wiki/_state/` - Compilation state: manifest, taxonomy, batches, compile-results, lint reports
  - `wiki/INDEX.md` - Dynamic index and learning paths
  - `wiki/Glossary.md` - Unified terminology hub
  - `wiki/sources.md` - Source document index
- `tools/` - CLI tools for searching, processing, and enhancing the wiki
  - `tools/wikillm.py` - The main WikiLLM CLI (Python 3 stdlib only)
- `skills/wikillm/` - Claude Code skill that defines compilation workflows and standards
- `web/` - Next.js web viewer for browsing the wiki in a browser

## Core Principles

- The LLM writes and maintains all wiki data; manual edits are rare
- Compilation is **batch-oriented and resumable**: large corpora are processed in small batches with checkpoints in `wiki/_state/`
- Deterministic work (hashing, image sync, lint, search) is delegated to `tools/wikillm.py`; the LLM focuses on taxonomy, synthesis, linking, and terminology
- User explorations and queries are filed back into the wiki to enhance it
- The system focuses on markdown files and Obsidian-compatible formats
- Images are downloaded locally for easy LLM reference and preserved in the `images/YYYY/` tree

## How to Compile

When `wiki/_state/taxonomy.md` is missing, this is a first-time bootstrap. Follow `skills/wikillm/references/bootstrap.md`.

When `taxonomy.md` exists, the typical session is:

```bash
python3 tools/wikillm.py scan          # detect new/changed raw posts
python3 tools/wikillm.py status        # read progress and pending batches
# dispatch subagents per batch brief in wiki/_state/batches/
python3 tools/wikillm.py lint          # mechanical health check
```

Always read `wiki/_state/progress.md` and `wiki/_state/batches.tsv` at the start of a compile session to resume from the last checkpoint.

## How to Ask Questions

Use the Q&A flow from `skills/wikillm/references/qa.md`. Start with:

```bash
python3 tools/wikillm.py search "your keywords"
```

## Important Conventions

- **Never flatten image paths**: `raw/images/YYYY/...` must map to `wiki/assets/images/YYYY/...`
- **Always preserve `raw_sources` in frontmatter** with sha256 hashes for traceability
- **Use kebab-case filenames** and exact-match Obsidian wikilinks (`[[File-Name|Label]]`)
- **Do not read `raw/posts/` directly in the main context**: raw posts are read inside subagents processing one batch at a time
