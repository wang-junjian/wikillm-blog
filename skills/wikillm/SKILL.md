---
name: wikillm
description: 将大规模 raw 文档批量编译为结构化、交叉链接的中文 Wiki 知识库。适用于首次冷启动、增量编译、Q&A 和 Wiki 维护。
license: MIT
metadata:
  version: "3.0"
  author: WikiLLM Project
---

# WikiLLM Skill

利用 LLM 将原始文档和图像**批量、分阶段、可恢复**地编译为结构化、交叉链接、高质量的中文 Wiki 知识库。

本技能基于 Andrej Karpathy 的 [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 思想构建，并针对中文技术博客语料进行了规模化改造。

## 任务路由（首先阅读本节！）

在执行任何操作前，先判断当前任务属于以下哪个场景：

| 场景 | 判断标准 | 跳转至 |
|------|----------|--------|
| **首次构建 (Bootstrap)** | `wiki/_state/taxonomy.md` 不存在，或 `wiki/` 为空 | [references/bootstrap.md](references/bootstrap.md) |
| **增量编译 (Compile)** | `raw/` 有新增或修改的文件；`taxonomy.md` 已存在 | [references/workflows.md](references/workflows.md) |
| **Q&A** | 用户针对 Wiki 内容提出问题（询问、咨询、探讨） | [references/qa.md](references/qa.md) |
| **Lint / 维护** | 需要检查 Wiki 的一致性、修复孤岛页面、统一术语 | [references/errors.md](references/errors.md) |

判断方法：先检查 `wiki/_state/taxonomy.md` 是否存在。不存在 → 首次构建；存在 → 进入增量编译或 Q&A/Lint。

## 执行模式

| 模式 | 触发条件 | 编排方式 |
|------|----------|----------|
| **批量编译 (Batch)** | 待编译源 > 10 个，或首次构建 | 主上下文只做编排：scan → 批次简报 → 派发 subagent → 整合。原始帖子一律由 subagent 阅读 |
| **小批量编译 (Mini-batch)** | 待编译源 1–10 个 | 同一条流水线，单个批次；可在主上下文内完成，也可派发 1 个 subagent |
| **问答 (Q&A)** | 用户提问 | 先 `python3 tools/wikillm.py search`，再精读命中页面 |
| **巡检 (Lint)** | 用户要求，或每轮编译收尾 | `python3 tools/wikillm.py lint` + LLM 语义检查 |

## 规模化铁律（raw 文档 ≥ 500 篇时强制执行）

1. **主上下文禁读 raw/**：主对话只读 `wiki/_state/` 下的状态文件、批次简报和 subagent 报告。
2. **脚本优先**：哈希、图片同步、链接检查、孤岛扫描一律用 `tools/wikillm.py`，禁止 LLM 逐文件操作。
3. **批次上限**：每批 ≤ 12 篇 且 原始体积 ≤ 100 KB；单篇 > 60 KB 的长文独立成批。
4. **先状态后行动**：任何编译任务第一步是读 `wiki/_state/progress.md` 与 `batches.tsv`，从断点续跑，禁止从零重来。
5. **聚合而非翻译**：quote/link/note 类帖子永不单独立页；短 how-to 合并进实践页；只有长文/深度文才有独立来源页。
6. **图片保树**：同步与引用图片必须保留 `images/YYYY/` 年份目录结构，禁止扁平化。
7. **每个产出页必须可追溯**：frontmatter 的 `raw_sources` 列出全部贡献源及其 sha256。

## 核心基础设施

所有确定性工作由 `tools/wikillm.py` 完成（Python 3 标准库，无外部依赖）：

```bash
python3 tools/wikillm.py scan        # 生成/更新 wiki/_state/manifest.tsv
python3 tools/wikillm.py sync-images # raw/images → wiki/assets/images，保留目录树
python3 tools/wikillm.py cluster     # 标签统计与聚类报告
python3 tools/wikillm.py batches     # 按主题生成批次简报
python3 tools/wikillm.py search <query> # 在 wiki/ 中搜索
python3 tools/wikillm.py lint        # 机械健康检查
python3 tools/wikillm.py status      # 查看编译进度
```

## 详细文档

- **首次构建**：见 [references/bootstrap.md](references/bootstrap.md)
- **编译工作流**：见 [references/workflows.md](references/workflows.md)
- **Q&A 流程**：见 [references/qa.md](references/qa.md)
- **质量标准**：见 [references/standards.md](references/standards.md)
- **常见错误**：见 [references/errors.md](references/errors.md)

## 快速开始

### 首次构建

当 `wiki/` 为空时：

1. 阅读 [references/bootstrap.md](references/bootstrap.md)
2. 创建 `tools/wikillm.py`
3. 运行 `python3 tools/wikillm.py scan` 和 `python3 tools/wikillm.py sync-images`
4. 运行 `python3 tools/wikillm.py cluster`，基于输出设计 `wiki/_state/taxonomy.md`
5. **人工审阅 taxonomy.md 后**，运行 `python3 tools/wikillm.py batches`
6. 按批次派发 subagent 进行综合，每完成一个主题做链接与索引

### 增量编译

当 `taxonomy.md` 已存在且 `raw/` 有新增/修改时：

1. 运行 `python3 tools/wikillm.py scan`
2. 运行 `python3 tools/wikillm.py status`，查看新增/变更文件
3. 阅读 `wiki/_state/progress.md` 和 `batches.tsv`，从断点续跑
4. 按 workflows.md 的批量流水线执行

### Q&A

当用户针对 Wiki 内容提问时：

1. 先运行 `python3 tools/wikillm.py search <问题关键词>`
2. 精读命中页面，给出带 Wikilink 引用的回答
3. 若问题具有通用价值，归档到 `wiki/queries/YYYY/`

### Lint

每次编译会话结束前：

1. 运行 `python3 tools/wikillm.py lint`
2. 根据 `wiki/_state/lint-report.md` 修复机械错误
3. LLM 进行语义一致性检查（术语漂移、跨主题链接缺失）

## 核心理念

- 人工不直接编写 Wiki，仅负责投放素材、发起查询、审阅关键分类
- LLM 负责理解、聚合、链接与维护
- Wiki 是持久化、可复利积累的知识产物，而非每次查询重新推导的临时答案
- 适配工具：Obsidian（IDE 前端）+ Next.js web 查看器
