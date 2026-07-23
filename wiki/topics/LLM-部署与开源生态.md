---
title: LLM-部署与开源生态
type: topic
topic: LLM-部署与开源生态
domain: LLM 与生成式 AI
tags: [llm-deployment, open-source, ollama, litellm, fastchat, xinference, langfuse, cloud-platform, ai-gateway, model-serving]
last_updated: 2026-07-21
status: complete
---

# LLM-部署与开源生态

> 领域：LLM 与生成式 AI
> 状态：完整

## 概述

LLM 部署与开源生态负责构建从模型到生产环境的完整链路，涵盖本地推理框架、服务化平台、AI 网关、可观察性工具以及云端推理服务，形成一套层次分明的工具矩阵。随着开源模型的成熟，本地部署与私有托管成为数据敏感场景的核心需求，而云端推理服务则为弹性扩展提供了免运维的替代方案。

本主题覆盖部署生态的完整分层：客户端层（Web UI/SDK/语音交互）、网关与代理层（LiteLLM）、可观察性层（Langfuse）、服务化层（Ollama/FastChat/Xorbits Inference/vLLM）、云端服务层（Together AI/SiliconFlow），以及 Dify 应用框架与 Reachy Mini 嵌入式部署实践。

## 实践指南页

- [[practices/LLM-部署与开源生态]]——LLM 部署的完整实践指南，涵盖本地推理框架、服务化平台、AI 网关、可观察性工具、云端服务与选型建议

## 关键知识点

1. **[[Ollama]]**——当前最流行的本地 LLM 运行框架，支持 GGUF 格式模型，提供类 Dockerfile 的 Modelfile 机制
2. **[[LiteLLM]]**——最活跃的 LLM 代理/网关解决方案，将 100+ 模型提供商的 API 统一为 OpenAI 格式
3. **[[FastChat]]**——LMSYS 推出的开放平台，采用 Controller-Worker 架构实现多模型服务化
4. **[[Xorbits Inference]]**——专注模型服务化的开源平台，覆盖数十种模型，支持 GGML 引擎
5. **[[Langfuse]]**——开源 LLM 工程平台，覆盖请求追踪、提示管理、评估与数据集管理
6. **[[Open WebUI]]**——类 ChatGPT 的聊天界面，支持 Ollama 与 OpenAI API 两种后端
7. **[[Together AI]]**——最快的生成式 AI 云平台，提供 OpenAI API 兼容接口
8. **[[SiliconFlow]]**——国内领先的 AI 基础设施平台，提供 SiliconCloud 云服务与 SiliconLLM 推理引擎
9. **[[Dify]]**——开源 LLM 应用开发平台，支持通过可视化工作流构建智能体
10. **[[OpenAI-API]] 兼容性**——Ollama/LiteLLM/Xinference/MindIE 均提供 `/v1/chat/completions` 兼容接口

## 重要来源

- Ollama 部署与 Open WebUI 集成
- LiteLLM 代理实践与 Langfuse 可观察性集成
- FastChat 多模型服务与 Xorbits Inference 平台
- Together AI 云端推理与 SiliconFlow 国产方案
- Dify 自定义 Agent 与 Reachy Mini 语音智能体
- 本地 AI 技术栈构建（Ollama + LiteLLM + Langfuse + Chatbox）

## 相关主题

- [[topics/LLM-推理优化]]——vLLM/SGLang 等高性能推理引擎
- [[topics/LLM-编码助手]]——编码助手的本地部署与模型推理
- [[topics/主流-LLM-与厂商]]——开源模型（Llama/Qwen/DeepSeek）的部署选择
- [[topics/RAG-检索增强生成]]——RAG 系统的部署依赖（嵌入模型 + 向量检索）
- [[topics/GPU-与-CUDA-开发]]——本地部署的硬件基础
