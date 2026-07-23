---
title: RAG-检索增强生成
type: topic
topic: RAG-检索增强生成
domain: LLM 与生成式 AI
tags: [rag, retrieval-augmented-generation, embeddings, vector-search, faiss, qdrant, graphrag, text2sql, knowledge-base, hybrid-search, reranking, agentic-rag]
last_updated: 2026-07-21
status: complete
---

# RAG-检索增强生成

> 领域：LLM 与生成式 AI
> 状态：完整

## 概述

检索增强生成（Retrieval-Augmented Generation，RAG）是一套将 LLM 的推理能力与外部知识源的检索能力相融合的技术范式——让模型基于"开卷考试"的方式生成回答。其核心思路是在推理阶段动态注入与查询相关的上下文，有效缓解 LLM 的幻觉问题、知识时效性问题以及私有数据不可访问的问题，已成为生产级 AI 应用的事实标准架构。

本主题覆盖 RAG 的完整技术栈：从嵌入模型与向量表示、FAISS/Qdrant/Chroma/Milvus 等向量数据库，到文档解析、分块、索引、检索、重排序、生成七阶段工作流程，再到 Text-to-SQL、GraphRAG、Agentic RAG 等高级变体。同时涵盖 RAGFlow 平台、Easy Dataset 数据制备、智能客服与投资分析等应用场景。

## 核心概念页

- [[concepts/RAG-检索增强生成]]——RAG 的完整技术体系，涵盖嵌入与向量表示、向量数据库、工作流程、高级变体、平台工具、基础设施、智能体编排与应用场景

## 关键知识点

1. **[[嵌入]]与向量表示**——文本映射为高维稠密向量，语义相近文本在向量空间中距离更近；中文场景下 BAAI/bge 系列与 stella 系列是主流选择
2. **[[FAISS]]**——Facebook AI Similarity Search，高效相似性搜索库，相比暴力余弦距离计算提速约 354 倍
3. **[[Qdrant]]**——生产就绪的向量相似性搜索引擎，专为扩展的过滤支持量身定制，与 FastEmbed 深度集成
4. **[[RAGFlow]]**——基于深度文档理解的开源 RAG 引擎，提供从文档解析到对话生成的端到端能力
5. **[[Text-to-SQL]]**——RAG 在结构化数据上的延伸，Vanna.AI 与 LangChain Text2SQL Agent 代表两种实现路径
6. **[[GraphRAG]]**——Microsoft 提出，将知识图谱引入 RAG 流程，支持全局搜索与本地搜索两种查询模式
7. **[[混合检索]]**——同时进行语义检索（向量搜索）和关键词搜索（BM25），通过 Rerank 模型进行语义排序
8. **[[Agentic RAG]]**——RAG 从静态管道向自主代理演进，支持分支逻辑和循环的状态机架构
9. **[[RAG 2.0]]**——引入上下文检索（Contextual Retrieval），在嵌入前为每个 chunk 补充上下文描述
10. **[[Easy Dataset]]**——基于 LLM 的微调数据集生成工具，解决 RAG 系统冷启动阶段训练数据不足的问题

## 重要来源

- RAG 工作流程与知识库构建、RAGFlow 平台与 MCP Server
- GraphRAG 实践与中文嵌入模型测试
- Text-to-SQL 解决方案与 LangChain Text2SQL Agent
- 智能问答售后服务系统与价值投资分析应用
- DeepSeek-mHC 架构演进与 RAG 系统生成组件能力上限

## 相关主题

- [[topics/向量数据库与语义搜索]]——向量检索的基础设施专题
- [[topics/Prompt-Engineering-与上下文工程]]——提示工程与 RAG 的互补关系
- [[topics/微调与模型训练]]——RAG 与微调的知识注入路径对比
- [[topics/LLM-编码助手]]——RAGFlow MCP Server 接入编码工具
- [[topics/主流-LLM-与厂商]]——Qwen2/DeepSeek 等模型在 RAG 中的应用
