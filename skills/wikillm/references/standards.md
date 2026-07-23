# 输出质量标准与文件结构

## 标准文件系统架构

严格遵循 I/O 分离原则，确保知识库的纯净度与可迁移性：

```text
📁 wikillm
├── 📁 raw/                    # 【输入层】原始素材（只读）
│   ├── 📁 posts/              # Markdown 文章（按年份组织）
│   └── 📁 images/             # 原始图片文件（按年份 + 主题子目录组织）
└── 📁 wiki/                   # 【输出层】编译器生成的知识产物
    ├── 📁 _state/             # 编译状态与中间产物
    │   ├── manifest.tsv
    │   ├── taxonomy.md
    │   ├── assignments.tsv
    │   ├── batches.tsv
    │   ├── batches/
    │   ├── compile-results.tsv
    │   ├── compile.log
    │   ├── progress.md
    │   └── lint-report.md
    ├── 📁 assets/images/      # 图片资源（从 raw/images/ 同步，保留年份树）
    ├── 📁 concepts/           # 核心概念、原理分析（聚合页）
    ├── 📁 practices/          # 部署指南、最佳实践（聚合页）
    ├── 📁 sources/            # 重要长文的单篇深度页
    ├── 📁 topics/             # 主题枢纽页
    ├── 📁 timeline/           # 年度/季度索引
    ├── 📁 visual/             # Marp 幻灯片、Matplotlib 趋势图
    ├── 📁 queries/            # 高价值 Q&A 的沉淀归档
    ├── INDEX.md               # 动态索引与学习路径
    ├── Glossary.md            # 统一术语表与双链枢纽
    └── sources.md             # 来源文档索引
```

## 页面类型与模板

### 1. concept / practice 页（聚合页）

用于把多篇 raw 文章聚合成一个主题页。

```yaml
---
title: 检索增强生成（RAG）
type: concept              # concept 或 practice
tags: [rag, llm, retrieval]
raw_sources:
  - path: raw/posts/2023/2023-04-14-autogpt.md
    hash: "sha256:abc123..."
  - path: raw/posts/2024/2024-05-20-rag-paper.md
    hash: "sha256:def456..."
last_updated: 2026-07-21
---
```

### 2. source 页（单篇深度页）

用于 60 KB 以上的重要长文或深度系列。

```yaml
---
title: UI-TARS 原生 GUI 智能体
source: UI-TARS 论文
type: source
tags: [ui-tars, agent, gui, computer-use]
raw_sources:
  - path: raw/posts/2025/2025-01-27-UI-TARS_Pioneering-Automated-GUI-Interaction-with-Native-Agents.md
    hash: "sha256:abc123..."
last_updated: 2026-07-21
---
```

### 3. topic 页（主题枢纽页）

```yaml
---
title: LLM 推理优化
type: topic
topic: llm-inference
tags: [llm, inference, vllm, kv-cache]
last_updated: 2026-07-21
---
```

### 4. timeline 页（年度索引）

```yaml
---
title: 2024 年文章索引
type: timeline
year: 2024
last_updated: 2026-07-21
---
```

### 5. query 页（Q&A 归档）

```yaml
---
title: "问题标题（用中文）"
source: "WikiLLM Q&A"
date: 2026-07-21
tags:
  - "Q&A"
  - "其他标签"
question: |
  在这里记录原始问题
---
```

## 聚合规则

| raw 类型 | 处理方式 |
|----------|----------|
| `article` 短 how-to（< 4 KB） | 按工具/任务聚合进 `practices/` |
| `article` 中篇 | 作为证据聚合进 `concepts/` |
| `article` 长文（> 60 KB）或深度系列 | `sources/` 独立页 |
| `quote` / `link` / `note` | 不建独立页，仅作为引文/例子吸收 |
| `release` | 并入对应工具的实践页"版本动态"小节 |

## 表达标准

**原则**：读起来像是由该领域的资深专家直接用中文撰写的。

**禁止词汇**：产生、输出（作为动词）、这个、那个（指代不明）

**提倡词汇**：负责构建、驱动、沉淀、权衡（Trade-off）

## 技术标准

| 维度 | 要求 |
| :--- | :--- |
| **术语表** | `Glossary.md` 必须覆盖全部核心概念，中英对照并带有 Wikilink |
| **链接密度** | 每 500 字需包含至少 3–5 个内部链接 |
| **视觉呈现** | 复杂架构必须有 Mermaid 图，数据趋势必须有 Markdown 表格 |
| **Marp 适配** | 综述类主题必须同步生成一份 `visual/` 下的 Slide 文档 |
| **可追溯性** | 每个 wiki 页面的 `raw_sources` 必须列出全部贡献源及其 sha256 |

## 图片引用规范

- 同步目标：`wiki/assets/images/YYYY/...`（保留年份目录树）
- wiki 中引用：`![](../assets/images/YYYY/topic/file.png)`
- **禁止扁平化**：不要把所有图片放到 `wiki/assets/images/` 根目录
- 外部图片 URL 可保留原样，但需记录到 `sources.md`

## Wikilink 格式规范

- 文件名使用 kebab-case（连字符分隔），例如：`Docker-容器化基础.md`
- Wikilink 格式为 `[[文件名|显示文本]]`，其中**文件名部分必须与实际文件名完全匹配**（不带 .md 扩展名）

**正确示例**：`[[Docker-容器化基础|Docker 容器化基础]]`

**错误示例**：`[[Docker 容器化基础|Docker 容器化基础]]`（文件名带空格）

### 文章列表格式

**错误写法**（表格无法正确解析双链）：

```markdown
| 文章 | 描述 |
|------|------|
| [[Mitchellh-Adoption-Journey|Mitchellh AI 采用之旅]] | HashiCorp 创始人从怀疑论者到深度用户的六个阶段 |
```

**正确写法**（使用无序列表）：

```markdown
- [[Mitchellh-Adoption-Journey|Mitchellh AI 采用之旅]] - HashiCorp 创始人从怀疑论者到深度用户的六个阶段
```

## 编译状态文件

### 1. `wiki/_state/manifest.tsv`

- 字段：`raw_path`, `sha256`, `size`, `mtime`, `type`, `title`, `date`, `tags`, `n_images`, `status`
- 由 `tools/wikillm.py scan` 生成，是 raw 层的完整清单

### 2. `wiki/_state/compile-results.tsv`

- 字段：`raw_path`, `hash`, `last_modified`, `wiki_paths`, `batch_id`, `compile_time`, `status`
- `wiki_paths` 可包含多个页面，用 `;` 分隔
- 记录每个 raw 文件的编译状态和生成的 wiki 文档

### 3. `wiki/_state/batches.tsv`

- 字段：`batch_id`, `topic`, `n_posts`, `status`, `session`, `completed_at`
- 批量编译的队列与状态

### 4. `wiki/_state/progress.md`

- 人工可读的编译进度与续跑指针
- 每次会话结束时更新

### 5. `wiki/_state/compile.log`

- 详细的编译日志
- 记录每次编译的输入、输出、决策过程

### 6. `wiki/sources.md`

- 来源文档索引
- 格式：`- [标题](URL)` 的无序列表
- 按"学术论文"、"概念文章"、"实践指南"、"工具发布"等分类组织

## 常用命令

```bash
# 查看当前编译状态
python3 tools/wikillm.py status

# 查看所有已编译文件
cat wiki/_state/compile-results.tsv

# 查找特定文件的编译状态
grep "raw/xxx.md" wiki/_state/compile-results.tsv

# 查看最近的编译日志
tail -100 wiki/_state/compile.log

# 查看 lint 报告
cat wiki/_state/lint-report.md
```
