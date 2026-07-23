---
title: SGLang
type: concept
tags: [sglang, llm-serving, inference-engine, radix-attention, structured-generation, open-source, lmsys, batch-scheduling, api-server]
last_updated: 2026-07-21
---

# SGLang

SGLang（Structured Generation Language）是一个高性能的大语言模型服务框架，由加州大学伯克利分校的 Lianmin Zheng（[[vLLM]] 作者之一）和 LMSYS 团队共同开发。其核心目标是通过创新的 RadixAttention 算法和结构化生成能力，在提升推理吞吐量的同时降低推理成本。SGLang 特别擅长处理多轮对话、批量推理和结构化输出（JSON 模式）场景，在 Long-context Eval、JSON Decoding Benchmark 等测试中表现优异。

与 [[vLLM]] 专注于单请求的高效推理不同，SGLang 的独特优势在于：

1. **RadixAttention**：利用基数树（Radix Tree）管理 KV Cache，自动复用多请求之间的公共前缀（如系统提示），显著减少重复计算和显存占用
2. **压缩有限状态机（Compressed FSM）**：高效支持 JSON Schema 约束的生成，保证输出严格符合结构化格式
3. **前端语言**：提供声明式的编程接口，方便构建复杂的 LLM 应用逻辑（分支、循环、并行、批处理）

## 核心概念

### RadixAttention 与 KV Cache 复用

SGLang 的核心创新是 RadixAttention 算法。传统推理引擎为每个请求独立管理 KV Cache，当多个请求共享相同前缀（如系统提示、few-shot 示例）时，会造成大量重复计算和显存浪费。SGLang 使用基数树（Radix Tree）数据结构管理所有请求的 KV Cache，自动识别并复用公共前缀：

- **前缀复用**：100 个请求共享 2000 token 的系统提示时，只需计算和存储一次
- **LRU 淘汰**：当显存不足时，最少使用的 Cache 节点被自动淘汰
- **前缀感知调度**：调度器优先处理能复用已有 Cache 的请求，最大化缓存命中率

在 ShareGPT 和 Synthetic 数据集上，RadixAttention 相比 [[vLLM]] 可实现 5 倍的吞吐量提升。这一优势在多轮对话和批量推理场景中尤为显著。

### 结构化生成

SGLang 内置了对 JSON Schema 约束生成的原生支持。通过压缩有限状态机（Compressed FSM）技术，SGLang 能够在解码过程中实时约束 token 的生成空间，确保输出严格符合指定的 JSON Schema。这一能力对于需要结构化输出的场景至关重要：

- **函数调用**：LLM 输出的 JSON 需要满足 API 调用格式
- **数据提取**：从非结构化文本中提取结构化信息
- **代码生成**：生成符合语法规则的代码片段

SGLang 的结构化生成在 JSON Decoding Benchmark 上表现出色，且对吞吐量的影响远小于其他方案。

### 前端编程接口

SGLang 提供了一种声明式的 Python DSL（领域特定语言），用于构建复杂的 LLM 应用逻辑：

```python
@function
def multi_turn_qa(s, question1, question2):
    s += system("You are a helpful assistant.")
    s += user(question1)
    s += assistant(gen("answer1", max_tokens=256))
    s += user(question2)
    s += assistant(gen("answer2", max_tokens=256))
```

支持 `gen`（生成）、`select`（选择）、`concat`（拼接）等原语，以及分支、循环、并行等控制流。前端语言编译为中间表示后，由后端运行时高效执行。

### 高性能后端

SGLang 后端采用多种优化技术：

- **Continuous Batching**：动态批处理，最大化 GPU 利用率
- **Tensor Parallelism**：多 GPU 张量并行，支持大模型推理
- **FlashInfer Attention**：高效的注意力计算内核
- **CUDA Graph**：减少内核启动开销
- **Chunked Prefill**：将长输入的预填充分块处理，避免阻塞正在生成的请求

### 与 vLLM 的对比

| 维度 | SGLang | vLLM |
|------|--------|------|
| 核心优势 | 前缀复用、结构化生成 | PagedAttention 内存管理 |
| 多轮对话 | RadixAttention 自动复用 | 需手动配置 prefix caching |
| 结构化输出 | Compressed FSM 原生支持 | 依赖第三方库（如 outlines） |
| 编程接口 | 声明式前端语言 | OpenAI 兼容 API |
| 生态成熟度 | 快速迭代中 | 更成熟，社区更大 |
| 适用场景 | 多轮对话、批量推理、结构化输出 | 通用单请求推理 |

两者并非完全替代关系——SGLang 更擅长多轮和批量场景，vLLM 在通用推理场景中生态更成熟。

## 技术架构

```mermaid
flowchart LR
    A[用户请求] B[前端 DSL 编译] C[调度器] D[RadixAttention 引擎] E[GPU 推理] F[响应返回]
    A --> B --> C --> D --> E --> F
    G[Radix Tree Cache] --> D
    H[Compressed FSM] --> D
    I[Continuous Batching] --> C
```

## 应用场景

- **多轮对话服务**：聊天机器人、客服系统，利用前缀复用大幅降低重复计算
- **批量离线推理**：大规模数据处理、评估推理，利用动态批处理提升吞吐
- **结构化输出**：JSON Schema 约束的函数调用、数据提取、表单填写
- **Agent 系统**：多步推理、工具调用，前端语言简化复杂逻辑编排
- **长文本处理**：文档摘要、长上下文问答，前缀复用减少显存占用
- **竞赛与基准评测**：LMSYS Chatbot Arena 使用 SGLang 作为推理后端

## 相关技术

- [[LLM-推理优化]]——SGLang 所属的推理加速技术体系
- [[vLLM]]——同类推理引擎，PagedAttention 方案
- [[Flash Attention]]——高效注意力计算算法
- [[CUDA Graph]]——GPU 计算图优化技术
- [[Outlines]]——结构化生成替代方案

## 主要页面

- [[LLM-推理优化]] - LLM 推理加速技术与 SGLang 的实践定位
- [[vLLM]] - 同类推理引擎对比与选型参考
