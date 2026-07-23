---
title: vLLM
type: concept
tags: [vLLM, 推理引擎, LLM, 部署]
last_updated: 2026-07-21
---

# vLLM

vLLM 是一个高性能的开源 LLM 推理引擎，专为大规模部署设计。它通过 PagedAttention 内存管理技术、连续批处理（Continuous Batching）和高效的 CUDA 内核优化，显著提升了 LLM 推理的吞吐量和显存利用率。

vLLM 支持多种主流大模型（Llama、Mistral、Qwen 等），兼容 OpenAI API 格式，是目前生产环境中部署 LLM 服务的核心工具之一。

## 主要页面

- [[LLM-推理优化]] - vLLM 在推理加速与部署中的实践

## 相关概念

- [[LLM]]
- [[模型量化]]
- [[GPU-推理]]
