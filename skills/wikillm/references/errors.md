# 常见错误与避免方法

## 错误 1：将 Q&A 当作编译任务处理

**表现**：用户提问时，直接去创建 `practices/` 或 `concepts/` 下的文档

**避免**：先看"任务路由"，Q&A 应该归档到 `wiki/queries/YYYY/`

## 错误 2：忘记添加参考文档清单

**表现**：回答了问题，但没有链接到相关 wiki 页面

**避免**：Q&A 回答模板中必须包含"参考文档"部分

## 错误 3：归档后不更新 INDEX.md

**表现**：创建了 `wiki/queries/` 下的文档，但 INDEX.md 中没有入口

**避免**：使用 Q&A 检查清单，确保步骤 5 完成

## 错误 4：大文档只读取开头部分

**表现**：学术论文或长篇技术文章只基于开头部分生成简短摘要

**避免**：使用"大文档处理要求"的检查清单；subagent 必须分段完整阅读

## 错误 5：Wikilink 格式错误

**表现**：`[[Harness Engineering|Harness 工程]]` 而不是 `[[Harness-Engineering|Harness 工程]]`

**避免**：参考 Wikilink 格式规范

## 错误 6：试图一次对话编译全部 raw 文档

**表现**：主上下文顺序读取 raw/ 下数百篇文章，导致上下文耗尽或输出截断

**避免**：使用批量编译流水线，主上下文只读状态文件和批次简报

## 错误 7：主上下文逐篇阅读 raw 帖子

**表现**：主对话亲自打开并阅读 `raw/posts/...` 文件

**避免**：原始文档一律由 subagent 在 batch 内阅读，主上下文只编排

## 错误 8：图片同步时扁平化目录

**表现**：把 `raw/images/` 下所有图片直接复制到 `wiki/assets/images/` 根目录，导致同名文件互相覆盖

**避免**：必须保留 `images/YYYY/` 年份目录树；同名冲突报告需人工确认

## 错误 9：聚合页丢失 raw_sources 追溯

**表现**：一篇聚合了 10 篇文章的 concept/practice 页，frontmatter 只列了 1 个来源

**避免**：每个 wiki 页面的 `raw_sources` 必须列出全部贡献源及其 sha256

## 错误 10：续跑时不读状态文件就重来

**表现**：新会话直接从头扫描、重新分类，导致大量重复编译

**避免**：任何编译任务第一步是读 `wiki/_state/progress.md` 与 `batches.tsv`

## 错误 11：batch 过大导致 subagent 输出截断

**表现**：一个 batch 包含 20+ 篇文章或原始文本超过 100 KB，subagent 输出质量下降

**避免**：遵守每批 ≤ 12 篇且 ≤ 100 KB 的限制；长文单独成批

## 错误 12：不区分散页类型

**表现**：quote / link / note 类帖子也生成独立 wiki 页，导致页面泛滥

**避免**：quote / link / note 永不单独立页；release 并入工具实践页

## 总体执行清单

* [ ] **任务路由确认**：已阅读任务路由，确认当前任务属于正确场景
* [ ] **状态读取**：已读取 `progress.md` 和 `batches.tsv`
* [ ] **Raw Scan**：已运行 `python3 tools/wikillm.py scan`
* [ ] **Asset Sync**：已运行 `python3 tools/wikillm.py sync-images` 且保留年份树
* [ ] **Glossary Lock**：是否已锁定全局术语表，确保翻译不漂移？
* [ ] **Multimodal Sync**：图片是否已转化为可编辑的文字解析/Mermaid？
* [ ] **文件名规范**: 所有 wiki 页面文件是否使用 kebab-case（连字符分隔）命名？
* [ ] **Wikilink 格式检查**: 所有 `[[文件名|显示文本]]` 链接中的文件名部分是否与实际文件名完全匹配？
* [ ] **Wikilink Check**: 所有的核心概念是否都已变成 `[[可点击的链接]]`？
* [ ] **Marp Check**: 是否为需要汇报的内容生成了幻灯片格式？
* [ ] **Orphan Check**: 是否存在无法从 `INDEX.md` 或主题枢纽页触达的"孤儿页面"？
* [ ] **Traceability Check**: 每个 wiki 页面是否都包含完整 `raw_sources`？

## Linting 检查清单

- [ ] **一致性检查**：扫描 `wiki/`，发现术语冲突时自动统一
- [ ] **孤岛扫描**：识别没有任何链接指向的页面，强制挂载到导航树
- [ ] **补丁发布**：当 `raw/` 有新版本时，在对应 Wiki 页面顶部发布摘要
- [ ] **死链检查**：`python3 tools/wikillm.py lint` 无 broken wikilink
- [ ] **图片检查**：所有 `![](...)` 引用都能解析到 `wiki/assets/images/` 下的文件
- [ ] **Frontmatter 检查**：必填字段（title, type, raw_sources）无缺失

## 最佳实践提示

* **手离开键盘**：不要手动修改 `wiki/` 目录下的内容，所有的修改应通过"向 LLM 发出 Lint 任务"、"添加 raw 素材后重新编译"或"Q&A 归档"来完成
* **搜索即创作**：把每一次对知识库的提问看作是一次"知识合成"，务必将高质量的回答存回库中
* **结构化思考**：在生成任何长篇文档前，先让 LLM 在内存中构建该主题的"概念地图"
* **利用状态文件**：遇到问题时，先查看 `wiki/_state/progress.md` 和 `compile.log` 了解之前的编译过程
* **先状态后行动**：任何编译会话开场必须先运行 `python3 tools/wikillm.py status`
