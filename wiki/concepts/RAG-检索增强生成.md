---
title: RAG 检索增强生成
type: concept
tags: [rag, retrieval-augmented-generation, embeddings, vector-search, faiss, qdrant, graphrag, text2sql, knowledge-base, hybrid-search, reranking, agentic-rag, llm]
raw_sources:
  - path: raw/posts/2023/2023-04-25-openai-api-doc-embeddings.md
    hash: "sha256:695e6b9fc4460faab1402d5904683ca7b3a90a182040fec939ef57f270e640e3"
  - path: raw/posts/2023/2023-09-02-private-gpt.md
    hash: "sha256:f8fb1290efcc368fffacda85942cf93c8d2e76f0b6743ec6f49e66d2f5b18a50"
  - path: raw/posts/2023/2023-09-09-llm-leaderboard.md
    hash: "sha256:510688395567331165ef54a0d503e0684a664e1228bf0d844a6d5b459c105fc2"
  - path: raw/posts/2023/2023-10-16-private-gpt-chinese-embeddings-model-test.md
    hash: "sha256:1f36b9c97237ea33d87f9c2293ed5cfd79ae52f208924ffba4288c8938a43662"
  - path: raw/posts/2023/2023-10-22-langchain-huggingfaceembeddings-faiss.md
    hash: "sha256:83287c940bde1ed4a46d440d691f86df5fb6dc3aca08ae8807c7624cb9145f61"
  - path: raw/posts/2023/2023-11-09-transformers-pipeline.md
    hash: "sha256:961432b338fb2c1ad8452eb7b4405f0830077e486303a62af9010f065f4bff50"
  - path: raw/posts/2023/2023-11-20-nginx-reverse-proxy.md
    hash: "sha256:c17810c175e6c1909c448ba08f54688a7dff5f07b77215a266dab7d4cc12041d"
  - path: raw/posts/2024/2024-04-12-LangChain-Text2SQL-Agent.md
    hash: "sha256:8400b5a5a05973acd5d9867f56f5c54483ee52f5d27fbaf3c8e8a83e9e1a02ee"
  - path: raw/posts/2024/2024-06-30-RAG-workflow-and-building-knowledge.md
    hash: "sha256:075926364806ef54718e7e8fc48f5f2183aa6a49507212ca77b212d51394cc3a"
  - path: raw/posts/2024/2024-07-04-VannaAI.md
    hash: "sha256:e14891e9425e55aa8452595e8f890037821743691e822a68fa297e3ea1b27192"
  - path: raw/posts/2024/2024-07-06-FastEmbed.md
    hash: "sha256:93b2321ab7428391202252c6d1783e3bc87ddb270cc8d90346f0b992b0eb5fc0"
  - path: raw/posts/2024/2024-07-07-Qdrant.md
    hash: "sha256:8e34e6d037cbf095490b5bca86de0fef9a33997dc9ed9474c440114e84d9bf77"
  - path: raw/posts/2024/2024-07-25-GraphRAG.md
    hash: "sha256:9516a313508133afacc1a7e1e4f61266870f978faa672109f1df25b5010f7390"
  - path: raw/posts/2024/2024-09-23-Qwen2-Technical-Report.md
    hash: "sha256:ec1d47d304a47c68af6d9eec64110bd38544f995229ed216c5ce0a81932b3df2"
  - path: raw/posts/2024/2024-10-28-LangChain-Blog-In-the-Loop.md
    hash: "sha256:b7483e0323419ba34a3dcdff695bf4ae76976ab1b4a7291bd1c1e50862bc153d"
  - path: raw/posts/2024/2024-11-13-Atlas 900-AI-Cluster.md
    hash: "sha256:f50242af804ffeb84df3f923d5c2b16cefc6c09da34ce15bd43fa7432d5c32e4"
  - path: raw/posts/2025/2025-03-18-RAGFlow.md
    hash: "sha256:ec98eb041450db672c140eba2b6c3b1130c496e2365b41682560cb308c11e008"
  - path: raw/posts/2025/2025-03-22-RAG2.md
    hash: "sha256:cafbe9502905180ba2b1ff0ff4265220d2195181ddc757aeb6e5df4ef063bccd"
  - path: raw/posts/2025/2025-03-24-Easy-Dataset.md
    hash: "sha256:44baecbae47a8fa5c986e5e73348df60b67363af55af0949546e492541565b54"
  - path: raw/posts/2025/2025-04-06-RAGFlowAssistant.md
    hash: "sha256:438b5c87ed9cb5fec9eed60073d841b1a458f17c8471064e5e47a0afcc48f4d3"
  - path: raw/posts/2025/2025-04-07-RAGFlow-MCP-Server.md
    hash: "sha256:3ca164be8819c721f61b0ae10fed89b25cb511869321920a1e1a996be4aeeea3"
  - path: raw/posts/2025/2025-04-15-cline-deepseek-mcp-tictactoe.md
    hash: "sha256:de0d8bf111dda7e7bbc2112cfae3e1f37f88ad85c3d4d97213b40d286e0064a8"
  - path: raw/posts/2025/2025-04-30-Text-to-SQL.md
    hash: "sha256:0696f624f9595901d34193944896791622c1ac938ba0aa7e6f741c936ff0c4b3"
  - path: raw/posts/2026/2026-01-05-DeepSeek-mHC-Manifold-Constrained-Hyper-Connections.md
    hash: "sha256:54a51415371c1fd28f91a0cb021863edaacea2de9ea47165ea31d22d26be3ec4"
  - path: raw/posts/2026/2026-04-10-2604_08224v1.md
    hash: "sha256:bb36953640755132ecb69bf8116b34221a9594947be369cf6c2ab5e06129f26e"
  - path: raw/posts/2026/2026-04-29-value_china_2025.md
    hash: "sha256:edef5aa9621ce5d5564e14317f53d1fbee6dcd502d59f0ee2944cfe3f235d3f2"
  - path: raw/posts/2026/2026-07-01-intelligent-customer-service.md
    hash: "sha256:f26dda7dffe3ec23dde2b965910b0841c04288f95bf8f534ceb8ebcc83c752e8"
last_updated: 2026-07-21
---

# RAG 检索增强生成

[[检索增强生成]]（Retrieval-Augmented Generation，RAG）是一套将 [[大型语言模型]]（[[LLM]]）的推理能力与外部知识源的检索能力相融合的技术范式。其核心思路并不在于扩大模型参数规模，而是在推理阶段动态注入与查询相关的上下文，让模型基于"开卷考试"的方式生成回答。这套范式有效缓解了 [[LLM]] 的幻觉问题、知识时效性问题以及私有数据不可访问的问题，已成为生产级 [[AI]] 应用的事实标准架构。

## 技术定位

RAG 的本质是认知外化——将模型内部无法容纳的知识转移到外部存储，再在推理时按需检索。这与 [[LLM-智能体的外化]] 一文中提出的 Harness Engineering 思想一脉相承：模型只负责通用推理，知识、技能、协议都外化到外部组件，由统一的运行层进行协调。

```mermaid
flowchart LR
    A[用户查询] B[查询嵌入] C[向量数据库] D[重排序] E[上下文拼接] F[LLM 生成] G[最终回答]
    A --> B --> C --> D --> E --> F --> G
    H[文档解析] I[分块] J[嵌入模型] K[(向量索引)]
    H --> I --> J --> K --> C
```

## 嵌入与向量表示

嵌入是 RAG 的基石。文本被映射为高维稠密向量，语义相近的文本在向量空间中距离更近。[[OpenAI]] 的 `text-embedding-ada-002` 模型输出 1536 维向量，[[余弦相似度]] 是衡量相关性的首选指标——相比欧几里得距离，余弦相似度只关注方向而非长度，且计算更快。

### 中文嵌入模型生态

中文场景下，嵌入模型的选择直接影响检索质量。经过系统测试的模型包括：

| 模型 | 维度 | 序列长度 | 特点 |
|------|------|----------|------|
| [[BAAI/bge-base-zh]] | 768 | 512 | 通用中文检索 |
| [[infgrad/stella-base-zh-v2]] | 768 | 1024 | 轻量高效 |
| [[sensenova/piccolo-large-zh]] | 1024 | 512 | 商汤两阶段训练 |
| [[BAAI/bge-small-zh-v1.5]] | 512 | 512 | 快速推理首选 |

在 [[Private GPT]] 中文嵌入测试中，使用"合作方人员出勤及结算管理信息化支撑规则"作为测试文档，对比不同模型在"怎么报工""每月补卡次数"等查询上的检索精度。结果表明，不同模型在精确匹配类查询上表现相近，但在需要语义理解的场景下差异显著。

### 嵌入工具链

[[HuggingFaceEmbeddings]] 配合 [[LangChain]] 是快速搭建 RAG 原型的主流选择。对于需要离线运行的场景，模型文件需提前下载至本地缓存。[[FastEmbed]] 则提供了更轻量的方案——由 [[Qdrant]] 团队开发，支持 20+ 款嵌入模型，原生集成 [[ONNX]] 运行时，无需 [[PyTorch]] 依赖。

## 向量数据库

向量数据库负责存储和检索高维向量，是 RAG 架构中的核心基础设施。不同产品在索引算法、过滤能力、部署模式上各有侧重。

### FAISS

[[FAISS]]（Facebook AI Similarity Search）是一个用于高效相似性搜索的库，数据存储在内存中。在亚马逊耳机评论数据集上的测试显示，[[FAISS]] 相比暴力余弦距离计算提速约 354 倍（7.8s vs 2.2s/10万次查询）。[[FAISS]] 提供 CPU 和 GPU 两种安装模式，支持 `IndexFlatL2` 等多种索引类型。

### Qdrant

[[Qdrant]] 是一个生产就绪的向量相似性搜索引擎，提供 REST API 和 gRPC 接口。它专为扩展的过滤支持量身定制，支持在向量上附加 payload 进行混合过滤。[[Qdrant]] 与 [[FastEmbed]] 深度集成，通过 `qdrant-client[fastembed]` 即可实现端到端的嵌入生成与检索。

### 其他向量数据库

- **[[Chroma]]**：轻量级嵌入式向量数据库，依赖 SQLite，适合原型验证
- **[[Milvus]]**：分布式架构，支持 IVF_FLAT 等索引，适合大规模生产环境
- **[[LanceDB]]**：[[GraphRAG]] 默认向量存储，支持稀疏向量

## RAG 工作流程

完整的 RAG 系统包含文档解析、分块、嵌入、索引、检索、重排序、生成七个阶段。[[RAGFlow]] 将这一流程产品化，提供了基于深度文档理解的开源 [[RAG]] 引擎。

### 文档解析与分块

不同文档类型需要不同的解析策略。[[RAGFlow]] 内置了丰富的解析方法：基于 Token 数分割、问答对解析、简历结构化、手册按标题切片、表格按行列解析、论文按章节拆分、法律文件按文本特征检测分割点、演示文稿逐页成块、图像 OCR 或视觉 LLM 描述。

### 检索策略

复杂场景下的检索采用三级流水线：

1. **召回模式**：从多个数据集中选出最相关的子集，支持 N 选 1、N 选 M、多路召回
2. **混合检索**：同时进行语义检索（向量搜索）和关键词搜索（[[BM25]]）
3. **重排序**：使用 Rerank 模型对混合结果进行语义排序和归一化

[[RAG 2.0]] 进一步引入了 [[Contextual Retrieval]]（上下文检索）——在嵌入前为每个 chunk 补充上下文描述，显著提升检索精度。[[SPLADE]] 和 [[BM25]] 的稀疏检索方案与稠密向量检索形成互补。

### 生成阶段

检索到的上下文与用户查询拼接后送入 [[LLM]] 生成回答。提示词模板通常包含角色设定、上下文注入、回答规则（如"不知道就说不知道""字数限制"等）。[[LangChain]] 的 [[LangGraph]] 框架支持构建更复杂的认知架构——从简单的线性管道到带循环和分支的状态机。

## 高级 RAG 变体

### Text-to-SQL

[[Text-to-SQL]] 是 RAG 在结构化数据上的延伸。[[Vanna.AI]] 提供了完整的 Text-to-SQL 框架：通过 `vn.train(ddl=...)` 训练 RAG"模型"，再通过 `vn.ask(question=...)` 生成可执行的 SQL 查询。它支持 [[ChromaDB]]、[[Qdrant]] 作为向量存储，支持 [[Ollama]] 本地 LLM。

[[LangChain Text2SQL Agent]] 则利用 [[Function Calling]] 实现参数提取——将自然语言中的省份、城市、供电所等实体提取为结构化参数，再拼接 SQL 条件。测试显示，[[OpenAI]] 的 GPT-3.5-turbo 在此类任务上表现最佳，而开源模型（如 Qwen-14B、Mistral）在复杂提取场景下仍有差距。

[[Text-to-SQL 解决方案]] 一文系统梳理了 Schema Linking、Chain-of-Thought、RSL-SQL、RB-SQL 等前沿方法。核心挑战在于：如何将自然语言意图精确映射为数据库 schema 元素。

### GraphRAG

[[GraphRAG]] 由 Microsoft 提出，将 [[知识图谱]] 引入 RAG 流程。它从非结构化文本中提取实体和关系，构建层次化社区结构，支持全局搜索（Global Search）和本地搜索（Local Search）两种查询模式。

[[GraphRAG]] 的索引流水线包含 14 个阶段：从 `create_base_text_units` 到 `create_final_documents`，涵盖实体提取、关系构建、社区聚类、报告生成。在模型兼容性方面，[[Ollama]] 的 `mistral:v0.2` 表现稳定，而 `llama3:8b`、`qwen2:7b` 等模型在 `create_base_entity_graph` 阶段易出错。嵌入模型推荐使用 `nomic-embed-text` 或 `bge-base-zh-v1.5`。

## 平台与工具

### RAGFlow

[[RAGFlow]] 是当前最活跃的开源 RAG 引擎之一，提供从文档解析到对话生成的端到端能力。其系统架构包含知识库管理、Agent 编排、对话界面、搜索引擎四大模块。支持 [[vLLM]] 接入本地 LLM，支持思维导图式搜索结果展示。

[[RAGFlowAssistant]] 是基于 [[RAGFlow SDK]] 构建的 Streamlit 应用，封装了客户端初始化、知识库列表获取、聊天会话管理、流式问答等核心功能。[[RAGFlow MCP Server]] 则将 RAGFlow 的能力暴露为 [[MCP]] 工具（`list_datasets`、`create_chat`、`chat`），可被 [[GitHub Copilot]]、[[Continue]]、[[Cline]] 等 AI 编码工具直接调用。

### Easy Dataset

[[Easy Dataset]] 是一套基于 [[LLM]] 的微调数据集生成工具。它通过智能分割、领域分析、批量生成问题等步骤，将文献转化为 [[Alpaca]]、[[ShareGPT]]、[[LLaMA Factory]] 格式的训练数据。虽然不直接属于 RAG 范畴，但它解决了 RAG 系统冷启动阶段训练数据不足的问题。

## 基础设施

### 模型推理

[[Transformers Pipeline]] 提供了标准化的推理接口，将预处理、推理、后处理封装为三步流水线。[[LLM.int8]] 量化可将显存占用降低约 72%（205MB → 119MB），速度提升 33%。[[Qwen2]] 系列模型采用 [[Grouped Query Attention]]（GQA）优化 KV Cache，支持 30+ 语言，在 MMLU、HumanEval、GSM8K 等基准上表现优异。

### 计算集群

大规模 RAG 系统的训练和推理依赖高性能计算基础设施。[[Atlas 900 AI 集群]]（济南人工智能计算中心）搭载华为 [[昇腾]] 处理器，采用 [[InfiniBand]] 高速互联和分布式存储，提供 384 张 NPU 卡的算力。这类集群为嵌入模型训练、大规模向量索引构建提供了硬件基础。

### 网络代理

生产环境中，RAG 服务通常通过 [[NGINX]] 反向代理对外暴露。[[NGINX]] 支持 HTTP 和 WebSocket 反向代理、多服务路由、负载均衡。配置时需注意 `proxy_redirect` 处理绝对路径引用，以及 WebSocket 所需的 `Upgrade` 和 `Connection` 头设置。

### 模型架构前沿

[[DeepSeek-mHC]]（流形约束超连接）代表了深度网络连接范式的最新演进。从残差连接（ResNet）到超连接（HC）再到 mHC，核心目标是在梯度稳定性与特征表达力之间寻找最优解。mHC 通过 Sinkhorn-Knopp 算法将连接矩阵投影至双随机流形，在 27B 模型上实现了训练稳定性和性能提升（相比基线平均提升 8.55%）。这类架构创新直接驱动了 RAG 系统中生成组件的能力上限。

## 智能体与编排

RAG 正在从静态管道向 [[Agentic RAG]] 演进。[[LangChain Blog: In the Loop]] 提出了"代理性"（Agentic）光谱的概念——从简单的路由器到带循环的状态机，再到完全自主的代理。系统越"代理性"，编排框架的帮助越大。

[[LangGraph]] 作为代理编排器，支持分支逻辑和循环的一流表达。[[OpenAI Assistants API]] 和 [[Claude Code]] 代表了两种不同的路线：前者提供通用认知架构但限制定制空间，后者提供分级权限模式和细粒度控制。

[[LLM 智能体的外化]] 一文提出了 Harness Engineering 的六大设计维度：智能体循环与控制流、沙箱与执行隔离、人工监督与审批门限、可观测性与结构化反馈、配置与权限策略编码、上下文预算管理。这为 RAG 系统的工程化落地提供了系统性的设计框架。

## 应用场景

### 智能客服

[[智能问答售后服务系统]] 是 RAG 在垂直行业的典型应用。采用"公众号前端 + 智能客服中台 + 知识库底座"三层架构，基于 RAG 实现 92% 以上的方案匹配准确率。系统支持多模态故障识别（图片/视频）、智能路由转人工、知识自进化。实施路径分三期：MVP（基础知识库 + 智能问答）、增强（多模态 + 工单对接）、优化（知识自进化 + 数据分析）。

### 投资分析

[[价值投资分析]] 展示了 RAG + LLM 在金融领域的应用潜力。使用 [[GLM-5.1]] 模型，以巴菲特/段永平视角对京东健康、美团、泡泡玛特、贵州茅台等公司的年报进行深度分析。这本质上是将海量财报数据作为知识库，通过 RAG 注入上下文，再由 LLM 生成专业投资分析报告。

### 智能编码

[[Cline + DeepSeek + MCP]] 的组合展示了 AI 编码的新范式。[[Cline]] 作为 VS Code 内的 AI 编码助手，配合 [[DeepSeek]] 模型和 [[GitHub MCP Server]]，实现了从代码生成、Issue 管理、Pull Request 创建到代码评审的全流程自动化。[[RAGFlow MCP Server]] 则将知识库问答能力接入编码工具，让开发者在编码过程中直接查询企业知识库。

## 权衡与决策

构建 RAG 系统需要在多个维度进行权衡（Trade-off）：

- **检索精度 vs 召回速度**：混合检索（向量 + 关键词 + 重排序）精度更高但延迟更大
- **嵌入模型容量 vs 推理成本**：大模型检索精度高但嵌入速度慢
- **分块粒度**：大块保留更多上下文但引入噪声，小块精确但丢失全局信息
- **开源 vs 托管**：自部署（[[FAISS]] + [[Ollama]]）可控性强但运维复杂，托管服务（[[OpenAI API]]）开箱即用但成本高
- **通用架构 vs 领域定制**：[[RAGFlow]] 等平台提供通用方案，垂直场景（如 [[Vanna.AI]] 的 Text-to-SQL）需要领域特定的认知架构

[[MTEB Leaderboard]] 和 [[Open LLM Leaderboard]] 为嵌入模型和生成模型的选择提供了客观基准。在实际选型中，中文场景建议优先测试 [[BAAI/bge]] 系列和 [[stella]] 系列，生成模型则需根据任务复杂度在 [[Qwen2]]、[[DeepSeek]] 等开源模型与商用 API 之间权衡。
