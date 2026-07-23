---
title: LLM-推理优化
type: topic
topic: LLM-推理优化
domain: LLM 与生成式 AI
tags: [llm, inference, vllm, sglang, quantization, speculative-decoding, kv-cache, benchmarking, model-serving]
last_updated: 2026-07-21
status: complete
---

# LLM-推理优化

> 领域：LLM 与生成式 AI
> 状态：完整

## 概述

LLM 推理优化贯穿"模型→框架→硬件→服务"全链路，是将大语言模型从研究原型推向生产级服务的关键工程领域。随着模型规模从数十亿迈向万亿参数，推理侧的显存效率、吞吐能力与延迟表现直接决定了服务的经济性与用户体验。

本主题覆盖五大技术层次：模型层的量化压缩与推测解码、引擎层的 vLLM/SGLang 等推理框架、服务层的网关与代理、硬件层的 GPU/NPU 适配，以及评测层的性能压测方法论。从 DeepSeek-V3 的 MoE+MLA 架构创新，到 vLLM V1 引擎的分段式 CUDA 图优化，再到 DSpark 的半自回归推测解码，推理优化正在架构与算法两个维度同步突破。

## 核心概念页

- [[concepts/LLM-推理优化]]——推理优化的完整技术栈，涵盖模型部署、推理引擎对比、量化压缩、推测解码、多 LoRA 适配器、显存规划、服务网关、硬件适配与性能压测

## 关键知识点

1. **[[vLLM]] 与 PagedAttention**——通过操作系统虚拟内存的分页思想管理 KV Cache，显存利用率提升至接近 100%，同等 GPU 下支持 2–3 倍并发
2. **[[SGLang]] 与 RadixAttention**——在前缀树（Radix Tree）上复用多个请求共享的 KV Cache 前缀，在多轮对话与 Agent 工作流中显著降低重复计算
3. **[[量化]]技术**——从 Q2_K 到 F16 的多级精度格式，Q4_K_M 通常是"显存-质量"的最佳平衡点；FP8 混合精度训练将吞吐量提升约 50%
4. **[[推测解码]]（Speculative Decoding）**——草稿模型快速生成候选 token，目标模型并行验证，实测可获得 2–3 倍吞吐提升
5. **[[DSpark]] 半自回归推测解码**——并行骨干网络后拼接轻量顺序头，配合置信度调度，在 DeepSeek 生产环境中实现 60%–85% 生成速度提升
6. **[[KV Cache]] 管理**——推理服务显存需求的核心构成，vLLM 的 PagedAttention 与 SGLang 的 RadixAttention 代表两种主流优化方向
7. **[[多-LoRA-推理]]**——共享基座模型的前提下服务多个下游任务，通过动态切换与批处理兼容实现适配器的高效复用
8. **[[TensorRT-LLM]]**——NVIDIA 推出的推理优化框架，提供 Python API 定义模型并构建 TensorRT 引擎，与 Triton Inference Server 配合部署
9. **[[MLX]] 框架**——Apple 为 Apple Silicon 设计的数组框架，统一内存模型支持本地推理与 LoRA 微调
10. **[[性能压测]]方法论**——TTFT、TPOT、Throughput 等核心指标，EvalScope 框架覆盖多维度压测场景

## 重要来源

- vLLM 部署 Qwen1.5、vLLM 核心优化实验、vLLM V1 引擎架构
- SGLang 框架解析与 Jetson Thor 多模态推理部署
- 推测解码原理与 DSpark/DFlash/Eagle3 三种草稿模型对比
- DeepSeek-V3/V4 技术报告中的 MoE、MLA、FP8 训练
- LiteLLM 代理实践与本地 AI 技术栈构建
- 4×NVIDIA T4 服务器上的 vLLM/SGLang/LiteLLM/Higress 四层压测报告

## 相关主题

- [[topics/LLM-部署与开源生态]]——推理框架的本地部署与云端服务化
- [[topics/微调与模型训练]]——LoRA 等参数高效微调方法与训练框架
- [[topics/主流-LLM-与厂商]]——DeepSeek、Qwen 等模型架构演进
- [[topics/LLM-技术报告与前沿论文]]——推理优化前沿研究成果
- [[topics/GPU-与-CUDA-开发]]——硬件层面的推理加速技术
