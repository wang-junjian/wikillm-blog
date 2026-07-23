# 编译工作流详细指南

本指南定义 WikiLLM 的批量编译流水线。适用于：

- **首次冷启动**：`wiki/` 为空，需要把 `raw/` 中全部素材编译成 Wiki
- **增量编译**：`raw/` 有新增或修改的文件，需要更新 Wiki
- **小批量编译**：新增文件 ≤ 10 个，可在一个 batch 内完成

对于首次构建，请先阅读 [bootstrap.md](bootstrap.md)。

## 批量编译检查清单

- [ ] **读取状态**：开场先读 `wiki/_state/progress.md` 和 `batches.tsv`，确认当前阶段
- [ ] **扫描检查**：运行 `python3 tools/wikillm.py scan`
- [ ] **资源同步**：运行 `python3 tools/wikillm.py sync-images`
- [ ] **分类法存在**：确认 `wiki/_state/taxonomy.md` 存在（不存在则走 bootstrap）
- [ ] **批次规划**：新增/变更文件较多时，运行 `python3 tools/wikillm.py batches`
- [ ] **subagent 派发**：每批原始内容由 subagent 阅读，主上下文不直接读 raw
- [ ] **更新状态**：每次 batch 完成后更新 `compile-results.tsv` 和 `batches.tsv`
- [ ] **链接注入**：每完成一个主题，更新主题枢纽页、Glossary、INDEX、timeline
- [ ] **Lint**：会话结束前运行 `python3 tools/wikillm.py lint`
- [ ] **记录进度**：更新 `progress.md`

## 阶段 0：扫描与资源同步

**任务**：把 `raw/` 的元数据和图片资源同步到 Wiki 侧，并识别变更。

### 0.1 扫描 raw/posts

```bash
python3 tools/wikillm.py scan
```

输出 `wiki/_state/manifest.tsv`：

| 字段 | 说明 |
|------|------|
| `raw_path` | 原始文件路径 |
| `sha256` | 文件哈希 |
| `size` | 文件字节数 |
| `mtime` | 修改时间 |
| `type` | frontmatter 中的 type |
| `title` | 标题 |
| `date` | 发布日期 |
| `tags` | 标签，用 `|` 分隔 |
| `n_images` | 本地图片引用数量 |
| `status` | `new` / `changed` / `unchanged` |

### 0.2 同步图片

```bash
python3 tools/wikillm.py sync-images
```

- 源：`raw/images/`
- 目标：`wiki/assets/images/`
- **必须保留目录树**：`raw/images/2024/CogVLM2/foo.png` → `wiki/assets/images/2024/CogVLM2/foo.png`
- 同名但不同路径的文件禁止互相覆盖
- 跳过未变更文件（按 size+mtime，必要时 hash）

### 0.3 识别变更

对比 `manifest.tsv` 与 `compile-results.tsv`：

- `new`：新文件
- `changed`：哈希变化
- `unchanged`：已编译且未变化，跳过

## 阶段 1：主题分类

**任务**：为新增/变更的文章确定主题归属和目标页面类型。

### 触发条件

- 首次构建时，由 LLM 设计完整 `taxonomy.md`
- 增量编译时，新增/变更文件数量较多，需要更新归属

### 输入

- `wiki/_state/cluster-report.md`（标签统计、共现对、每篇文章一行摘要）
- 现有 `wiki/_state/taxonomy.md`

### 输出

- `wiki/_state/taxonomy.md`：主题分类法
- `wiki/_state/assignments.tsv`：每篇文章的 topic、page_type、target_pages

### 目标页面类型

| 类型 | 说明 | 示例 |
|------|------|------|
| `concept` | 概念/原理聚合页 | `RAG-检索增强生成.md` |
| `practice` | 实践/工具聚合页 | `vLLM-部署实践.md` |
| `source` | 重要长文的独立页 | `UI-TARS-原生智能体.md` |
| `absorbed` | 被吸收，不建独立页 | quote / link / note / 短 how-to |

## 阶段 2：批次规划

**任务**：把同一主题下的文章分成大小适中的 batch，便于 subagent 处理。

```bash
python3 tools/wikillm.py batches
```

### 批次规则

- 每批 ≤ 12 篇文章
- 每批原始文本总量 ≤ 100 KB
- 单篇 > 60 KB 的长文单独成批
- 同一主题内按日期升序排列，保留实践演进脉络

### 输出

- `wiki/_state/batches/NNN-<topic>.md`：每个 batch 的简报
- `wiki/_state/batches.tsv`：batch 队列

### batch 简报内容

```markdown
---
batch_id: 001
topic: docker
n_posts: 10
target_pages:
  - Docker-容器化基础.md
  - Docker-镜像优化.md
---

## 文件列表

1. `raw/posts/2020/2020-03-15-docker-intro.md` — "Docker 入门" — tags: docker, container, linux
2. ...

## 目标

- 把本批文章综合成 `concepts/Docker-容器化基础.md`
- 保留命令示例和实际案例
- 所有图片引用改为 `../assets/images/YYYY/...`
```

## 阶段 3：批量合成

**任务**：由 subagent 分批阅读 raw 文章，写入/更新 wiki 页面。

### 主上下文职责

- 读取 `progress.md` 和 `batches.tsv`
- 挑选 pending batch
- 为每个 batch 启动 subagent
- 接收 subagent 报告
- 更新 `compile-results.tsv`、`batches.tsv`、`progress.md`
- **禁止**直接阅读 raw 文件

### subagent 职责

- 阅读分配给它的 raw 文件
- 按目标页面类型生成/更新 wiki 页面
- 在 frontmatter 中填写 `raw_sources`（含 sha256）
- 将图片引用改为相对路径 `../assets/images/YYYY/...`
- 返回简洁报告

### subagent prompt 模板

```markdown
你是 WikiLLM 的批量编译子智能体。请处理以下 batch：

## Batch 简报

[粘贴 batch 简报]

## 写作标准

- 文件名使用 kebab-case
- Wikilink 格式：`[[File-Name|显示文本]]`，文件名部分必须与磁盘文件名完全一致
- 每 500 字至少 3 个内部链接
- 复杂架构使用 Mermaid 图
- 聚合页 frontmatter 的 `raw_sources` 列出全部来源

## 术语锁定

[从 Glossary.md 摘录相关术语]

## 图片引用规则

将 raw 中的 `/images/YYYY/...` 改为 `../assets/images/YYYY/...`。

## 输出要求

1. 写出所有目标 wiki 文件
2. 返回报告：写入文件列表、消耗的来源 hash、发现的异常
```

### 更新 compile-results.tsv

每完成一个 batch，追加/更新记录：

```tsv
raw_path	hash	last_modified	wiki_paths	batch_id	compile_time	status
```

`wiki_paths` 可包含多个目标页面，用 `;` 分隔。

## 阶段 4：网络化链接与索引

**任务**：在每个主题内部和跨主题之间建立链接，并更新索引。

### 4.1 主题枢纽页

每完成一个主题的全部 batch，生成/更新 `wiki/topics/<Topic>.md`：

- 主题定义与范围
- 演进脉络（按时间线）
- 核心概念页链接
- 实践页链接
- 来源页链接
- 相关主题链接

### 4.2 术语表

更新 `wiki/Glossary.md`：

- 补充本主题新出现的术语
- 统一中英文对照
- 给核心术语加上 Wikilink

### 4.3 年度时间线

更新 `wiki/timeline/<YYYY>.md`：

- 按主题分组列出该年度文章
- 每行一个 Wikilink + 一句话摘要

### 4.4 总索引

更新 `wiki/INDEX.md`：

- "按主题浏览"：链接到各主题枢纽页
- "学习路径"：为热门主题推荐阅读顺序
- "最近更新"：列出最新编译的页面

### 4.5 Wikilink 注入

- 全文检索主题内页面标题和 Glossary 术语
- 将首次出现的概念包裹为 `[[Term|中文]]`
- 避免过度链接：同一页面内同一术语只链接一次

## 阶段 5：健康检查与维护

**任务**：发现并修复 Wiki 的机械错误和语义不一致。

### 5.1 机械 Lint

```bash
python3 tools/wikillm.py lint
```

检查项：

- 损坏的 wikilink（目标文件不存在）
- 孤立页面（无任何入链，且未出现在 INDEX 或主题枢纽页）
- 无法解析的图片引用
- `raw_sources` 缺失或 sha256 不匹配
- frontmatter 必填字段缺失
- 图片同名冲突
- 禁用词汇

### 5.2 LLM 语义修复

- 术语漂移统一（如 A 页用"智能体"，B 页用"代理"）
- 跨主题链接补全
- 矛盾声明标记

### 5.3 补丁发布

当 `raw/` 中某篇重要文章更新时：

- 在对应 wiki 页面顶部添加 `[Update Patch]` 摘要
- 更新 `raw_sources` 中的 hash
- 重新评估该页面与其他页面的关系

## 小批量增量编译（≤10 个文件）

当新增/变更文件很少时，可以走简化路径：

1. `python3 tools/wikillm.py scan`
2. 阅读变更文件列表
3. 为变更文件运行 `python3 tools/wikillm.py assign`（仅变更行）
4. 运行 `python3 tools/wikillm.py batches`（通常只有 1 个 batch）
5. 派 1 个 subagent 处理该 batch
6. 更新相关主题枢纽页、Glossary、INDEX
7. `python3 tools/wikillm.py lint`

## 恢复与续跑

每次编译会话必须以以下步骤开场：

```bash
python3 tools/wikillm.py status
```

然后阅读 `wiki/_state/progress.md` 和 `batches.tsv`，找到第一个未完成的 stage 和 pending batch，从断点继续。

### 续跑算法

1. 若 `progress.md` 显示 Stage 0/1/2 未完成，先完成对应阶段
2. 若 Stage 3 未完成，读取 `batches.tsv` 中 `status=pending|failed` 的 batch，继续派发 subagent
3. 若 Stage 4 未完成，按未完成的主题补齐链接与索引
4. 若 Stage 5 未完成，运行 `lint` 并修复

### 失败批次处理

- 状态为 `failed` 的 batch 可重试一次
- 若再次失败，记录异常到 `progress.md`，由人工决定如何处理

## 大文档完整阅读要求

对于篇幅较长的文档（学术论文、长篇技术文章、深度演讲整理），subagent 必须完整阅读：

1. 使用 Grep 搜索章节标题了解结构
2. 分段读取完整内容，确保覆盖所有主要章节
3. 输出内容标准：
   - 学术论文：摘要、核心方法、实验结果、讨论
   - 技术文章：问题背景、完整解决方案、实际案例
   - 保留所有定量数据（表格、指标）

例外：纯新闻报道、简短公告、仅代码/配置的文件可生成较短摘要。

## 视觉解析

对图片进行深度 OCR 与逻辑识别：

- 架构图转化为文字描述 + Mermaid 代码块
- 数据表格转化为 Markdown 表格
- 关键截图在 wiki 页面中保留引用

## 元数据提取

每个 wiki 文档必须包含 YAML frontmatter，格式见 [standards.md](standards.md)。

聚合页的 `raw_sources` 字段必须列出全部贡献来源：

```yaml
raw_sources:
  - path: raw/posts/2023/2023-04-14-autogpt.md
    hash: "sha256:abc123..."
  - path: raw/posts/2024/2024-05-20-rag-paper.md
    hash: "sha256:def456..."
```
