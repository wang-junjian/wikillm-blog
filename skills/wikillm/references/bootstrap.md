# 首次构建指南（Bootstrap）

当 `wiki/` 为空、或 `wiki/_state/taxonomy.md` 不存在时，使用本指南从零构建 Wiki。

## 目标

把 `raw/` 中已有的全部素材（本仓库约 788 篇帖子、约 3000 张图片）批量编译成一个结构化、可浏览、可扩展的中文 Wiki。首次构建会分多次会话完成；每次会话结束时必须更新 `wiki/_state/progress.md` 与 `batches.tsv`，确保下一次能从断点续跑。

## 前置条件

- Python 3 已安装（macOS 自带）
- 已创建 `tools/wikillm.py`
- 已阅读 [workflows.md](workflows.md) 了解六阶段流水线
- 已阅读 [standards.md](standards.md) 了解目录结构与页面模板

## Session 0：基础设施 + 分类法设计

### 步骤 1：生成清单并同步图片

```bash
cd /Users/junjian/GitHub/wang-junjian/wikillm-blog
python3 tools/wikillm.py scan
python3 tools/wikillm.py sync-images
```

验证：

- `wiki/_state/manifest.tsv` 行数应等于 `raw/posts/**/*.md` 文件数（当前约 788）。
- `wiki/assets/images/` 目录结构与 `raw/images/` 一致，图片按 `YYYY/` 年份树保存，无扁平化覆盖。
- `wiki/_state/compile.log` 应有两条记录。

### 步骤 2：生成聚类报告

```bash
python3 tools/wikillm.py cluster
```

输出 `wiki/_state/cluster-report.md`，包含：

- 标签频次表
- 标签共现对
- 每篇文章一行摘要（日期、标题、前 3 个标签）

### 步骤 3：设计主题分类法

阅读 `cluster-report.md`，设计 `wiki/_state/taxonomy.md`。推荐结构：

```markdown
# 主题分类法

## 领域 1：LLM 基础与推理
- LLM-推理优化（seed tags: llm, inference, vllm, kv-cache）
- RAG-检索增强生成（seed tags: rag, retrieval, embedding）
- 提示工程（seed tags: prompt-engineering, few-shot, cot）

## 领域 2：智能体与工具
- AI-Agent 架构（seed tags: agent, ai-agent, 智能体）
- MCP-模型上下文协议（seed tags: mcp）
- 自主应用（seed tags: autonomous-application, workflow）

## 领域 3：AI 编程助手
- AI-Coding-Assistant（seed tags: ai-coding-assistant, github-copilot, claude-code, cursor）
- IDE 与编辑器集成（seed tags: vscode, continue, cody）

## 领域 4：模型与训练
- 大语言模型（seed tags: llm, qwen, openai, deepseek, generative-ai）
- 微调与对齐（seed tags: fine-tuning, llama-factory, alignment）

## 领域 5：部署与工程
- Docker 与容器化（seed tags: docker, container）
- Kubernetes 与编排（seed tags: kubernetes, k8s, helm）
- Linux 与系统管理（seed tags: linux, ubuntu, sysadmin, command-line）
- macOS 与 Apple Silicon（seed tags: macos, apple-silicon）

## 领域 6：Python 与开发工具
- Python 语言（seed tags: python）
- TypeScript 与前端（seed tags: typescript, frontend）

## 领域 7：计算机视觉与语音
- 计算机视觉（seed tags: computer-vision, opencv, openvino）
- 语音与音频（seed tags: whisper, speech, asr）

## 领域 8：硬件与推理加速
- GPU 与 CUDA（seed tags: gpu, cuda, nvidia）
- 边缘推理与芯片（seed tags: edge, jetson, openvino, atlas）
```

**人工审阅点**：主题的命名、边界、种子标签是否准确。这是整个 Wiki 质量的根基，强烈建议人工确认。

### 步骤 4：生成归属与批次

```bash
python3 tools/wikillm.py assign
python3 tools/wikillm.py batches
```

- `assign` 按种子标签做初版归属，输出 `wiki/_state/assignments.tsv`。
- LLM 检查 `assignments.tsv` 中的 `UNASSIGNED` 或边缘案例，手工调整归属。
- `batches` 按主题和体积切分，输出 `wiki/_state/batches/*.md` 与 `batches.tsv`。

### 步骤 5：创建骨架页面

用脚本生成以下空骨架（内容待后续填充）：

- `wiki/INDEX.md`
- `wiki/Glossary.md`（至少包含 taxonomy 中的核心术语锁定翻译）
- `wiki/timeline/2018.md` 至 `wiki/timeline/2026.md`
- `wiki/topics/*.md`（每个主题一个枢纽页）
- `wiki/sources.md`

更新 `wiki/_state/progress.md`：

```markdown
# 编译进度

- Stage 0 扫描与同步：完成
- Stage 1 主题分类：完成
- Stage 2 批次规划：完成
- Stage 3 批量合成：进行中
  - 已完成 batch：无
  - 待处理 batch：见 batches.tsv
- Stage 4 链接与索引：未开始
- Stage 5 Lint：未开始
- 最后更新：YYYY-MM-DD
```

## Session 1..K：批量合成

每次会话执行以下循环：

1. **开场**：
   ```bash
   python3 tools/wikillm.py status
   ```
   读取 `wiki/_state/progress.md` 与 `batches.tsv`，确认当前 stage 和待处理 batch。

2. **选择批次**：
   - 优先选择一个中等规模、标签清晰的主题（如 Docker、Linux）来磨合 subagent 输出格式。
   - 每次处理 5–10 个 batch，并行启动 3–4 个 subagent。
   - 同一主题的 batch 尽量在一次会话内完成，以便统一做 Stage 4 链接。

3. **派发 subagent**：
   每个 subagent 的 prompt 必须包含：
   - batch 简报文件内容
   - 目标页面类型（concept / practice / source）
   - `wiki/Glossary.md` 中的锁定术语
   - [standards.md](standards.md) 中的写作标准摘要
   - 图片引用规则：`../assets/images/YYYY/...`
   - 输出要求：写入哪些文件、每页的 `raw_sources` 列表

4. **整合**：
   - 主上下文不读 raw 文件，只读 subagent 返回的报告。
   - 更新 `compile-results.tsv`、`batches.tsv`、`progress.md`。

5. **主题级链接（Stage 4）**：
   - 若某主题全部 batch 已完成，生成/更新 `wiki/topics/<Topic>.md`。
   - 在主题内部页面注入 wikilink。
   - 更新 `Glossary.md`、相关 `timeline/YYYY.md`、`INDEX.md`。

6. **Lint（Stage 5）**：
   ```bash
   python3 tools/wikillm.py lint
   ```
   修复死链、孤立页、缺失 frontmatter 等机械问题。

7. **收尾**：
   更新 `progress.md`，记录本次完成的 batch 和发现的问题。

## 最终整理会话

当所有 batch 状态为 `done` 后：

1. 全局 `python3 tools/wikillm.py lint`
2. 统一术语：检查 `Glossary.md` 是否覆盖全部核心概念，修正漂移
3. 补充跨主题链接：例如把 `Docker-容器化实践` 链接到 `Kubernetes-编排`
4. 更新 `wiki/sources.md`：按学术论文、概念文章、实践指南、工具发布等分类
5. 为 top 5 综述主题生成 Marp 幻灯片到 `wiki/visual/`
6. 在 `progress.md` 中标记"首次构建完成"，并写入 steady-state 说明

## 常见问题

### 为什么必须先设计 taxonomy.md？

taxonomy 是后续 batch 划分、主题枢纽页、学习路径的根基。没有它，subagent 会各自为政，导致术语和分类体系不一致。

### 人工审阅 taxonomy 需要关注什么？

- 主题数量是否合理（建议 25–40 个）
- 种子标签是否能覆盖大部分文章
- 主题之间是否有明显重叠
- 主题命名是否符合中文技术语境

### 如果某个主题太大怎么办？

可在 taxonomy 中拆分子主题。例如 "LLM-推理优化" 可拆为 "vLLM-服务化"、"KV-Cache 与量化"、"投机解码" 等。拆完后重新运行 `assign` 和 `batches`。

### 如何处理 60 KB 以上的超大文章？

这类文章单独成批，作为 `wiki/sources/` 下的独立页面。subagent 需要完整阅读全文（遵循 workflows.md 中的"大文档完整阅读要求"）。

### 首次构建大概需要多少次会话？

按每批 8–10 篇文章、每次处理 5–10 批计算，约 8–14 次会话。状态文件保证每次都能断点续跑。
