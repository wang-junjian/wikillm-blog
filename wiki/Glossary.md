---
title: WikiLLM 术语表
type: glossary
last_updated: 2026-07-21
---

# WikiLLM 术语表

> 统一的中英术语对照，确保全 Wiki 术语使用一致。
> 每个术语标注首选中文翻译（锁定），避免术语漂移。
> 核心术语已添加 Wikilink，方便跳转至对应页面。

---

## 通用 AI 术语

| 英文 | 首选中文 | 别名/说明 |
|------|---------|----------|
| Large Language Model (LLM) | 大语言模型 | 大模型 |
| Generative AI | 生成式 AI | 生成式人工智能 |
| Artificial Intelligence (AI) | 人工智能 | |
| Machine Learning | 机器学习 | |
| Deep Learning | 深度学习 | |
| Foundation Model | 基础模型 | 基座模型 |
| Fine-tuning | 微调 | |
| Pre-training | 预训练 | |
| Alignment | 对齐 | |
| Reinforcement Learning from Human Feedback (RLHF) | 基于人类反馈的强化学习 | |
| Prompt Engineering | 提示工程 | 提示词工程 |
| Context Engineering | 上下文工程 | |
| Chain-of-Thought (CoT) | 思维链 | |
| In-Context Learning | 上下文学习 | |
| Retrieval-Augmented Generation (RAG) | 检索增强生成 | |
| Embedding | 嵌入 / 向量表示 | |
| Token | 词元 | |
| Tokenizer | 分词器 | |
| Inference | 推理 | |
| Hallucination | 幻觉 | |
| Agent | 智能体 | |
| Multi-Agent System | 多智能体系统 | |

## 模型术语

| 英文 | 首选中文 | 别名/说明 |
|------|---------|----------|
| Parameter | 参数 | |
| Billion/Million Parameters | 十亿/百万参数 | |
| Quantization | 量化 | |
| Mixture of Experts (MoE) | 专家混合 | |
| Low-Rank Adaptation (LoRA) | 低秩适应 | |
| QLoRA | 量化低秩适应 | |
| KV Cache | 键值缓存 | |
| Context Window | 上下文窗口 | |
| Temperature | 温度（采样参数） | |
| Top-p / Top-k | 核采样 / Top-k 采样 | |
| Vision-Language Model (VLM) | 视觉语言模型 | |
| Vision-Language-Action Model (VLA) | 视觉语言动作模型 | |
| Multimodal Large Language Model (MLLM) | 多模态大语言模型 | |
| Diffusion Model | 扩散模型 | |
| Stable Diffusion | 稳定扩散模型 | |
| Latent Diffusion Model (LDM) | 潜在扩散模型 | |

## 推理与部署

| 英文 | 首选中文 | 别名/说明 |
|------|---------|----------|
| vLLM | vLLM（推理框架） | |
| SGLang | SGLang（推理框架） | |
| TensorRT-LLM | TensorRT-LLM | |
| llama.cpp | llama.cpp | |
| Ollama | Ollama | |
| Text Generation Inference (TGI) | 文本生成推理 | |
| Speculative Decoding | 推测解码 / 投机解码 | |
| Continuous Batching | 连续批处理 | |
| PagedAttention | 分页注意力 | |
| Model Serving | 模型服务 | |
| Inference Endpoint | 推理端点 | |
| Model Quantization | 模型量化 | INT4/INT8/FP8/GGUF |
| GGUF | GGUF（模型格式） | GPT-Generated Unified Format |
| Model Merging | 模型合并 | Task Vector |
| Model Editing | 模型编辑 | ROME / Hypernetwork |

## RAG 与向量检索

| 英文 | 首选中文 | 别名/说明 |
|------|---------|----------|
| Vector Database | 向量数据库 | |
| Vector Search | 向量搜索 | |
| Semantic Search | 语义搜索 | |
| Dense Retrieval | 密集检索 | |
| Sparse Retrieval | 稀疏检索 | |
| Reranker | 重排序器 | |
| Chunk | 文本块 / 分块 | |
| Chunking | 分块策略 | |
| Recall | 召回率 | |
| Precision | 精确率 | |
| GraphRAG | 图检索增强生成 | Microsoft 知识图谱 |
| Text-to-SQL | 文本转 SQL | |
| Hybrid Search | 混合检索 | 密集+稀疏 |
| FAISS | FAISS（向量检索库） | Facebook AI Similarity Search |
| Qdrant | Qdrant（向量数据库） | |

## Agent 与 MCP

| 英文 | 首选中文 | 别名/说明 |
|------|---------|----------|
| Model Context Protocol (MCP) | 模型上下文协议 | |
| MCP Server | MCP 服务器 | |
| MCP Client | MCP 客户端 | |
| Tool Use | 工具调用 | |
| Function Calling | 函数调用 | |
| ReAct | 推理-行动框架 | Reasoning + Acting |
| Planning | 规划 | |
| Memory（Agent） | 记忆（智能体） | |
| A2A Protocol | Agent 间协议 | Agent-to-Agent |
| Computer Using Agent (CUA) | 计算机使用代理 | |
| GUI Agent | 图形界面智能体 | |
| Workflow Orchestration | 工作流编排 | |
| Multi-Agent Collaboration | 多智能体协作 | |

## 硬件与芯片

| 英文 | 首选中文 | 别名/说明 |
|------|---------|----------|
| GPU | 图形处理器 | |
| CUDA | CUDA（计算平台） | |
| NVIDIA Jetson | 英伟达 Jetson | |
| NVIDIA TensorRT | 英伟达 TensorRT | |
| Huawei Ascend | 华为昇腾 | |
| NPU | 神经网络处理器 | |
| TPU | 张量处理器 | |
| Edge Computing | 边缘计算 | |
| Physical AI | 物理 AI | 具身智能硬件 |
| CANN | CANN（昇腾计算架构） | |
| MindIE | MindIE（昇腾推理引擎） | |

## 开发工具

| 英文 | 首选中文 | 别名/说明 |
|------|---------|----------|
| Docker | Docker | |
| Kubernetes (K8s) | Kubernetes | K8s |
| Container | 容器 | |
| Image（Docker） | 镜像 | |
| Dockerfile | Dockerfile | |
| Pod（K8s） | Pod | |
| Deployment（K8s） | 部署 | |
| Service（K8s） | 服务 | |
| Ingress | 入口 | |
| Helm | Helm（包管理） | |
| VS Code Extension | VS Code 扩展 | |
| Language Server Protocol (LSP) | 语言服务器协议 | |

## 具身智能

| 英文 | 首选中文 | 别名/说明 |
|------|---------|----------|
| Embodied AI | 具身智能 | |
| Robotics | 机器人学 | |
| Robot Learning | 机器人学习 | |
| Manipulation | 操作/操控 | |
| Navigation | 导航 | |
| World Model | 世界模型 | |
| Simulation | 仿真 | |
| MuJoCo | MuJoCo（物理仿真引擎） | |
| Isaac Sim | Isaac Sim（NVIDIA 仿真平台） | |
| Digital Twin | 数字孪生 | |

## 语音与音频处理

| 英文 | 首选中文 | 别名/说明 |
|------|---------|----------|
| Automatic Speech Recognition (ASR) | 自动语音识别 | |
| Text-to-Speech (TTS) | 语音合成 | |
| Whisper | Whisper（OpenAI 语音模型） | |
| FunASR | FunASR（阿里语音框架） | |
| SenseVoice | SenseVoice（多维语音理解） | |
| PaddleSpeech | PaddleSpeech（百度语音工具包） | |
| SeamlessM4T | SeamlessM4T（多模态翻译） | |
| Real-time Streaming | 实时流式处理 | |
| Voice Activity Detection (VAD) | 语音活动检测 | |

## 计算机视觉

| 英文 | 首选中文 | 别名/说明 |
|------|---------|----------|
| Object Detection | 目标检测 | |
| Image Classification | 图像分类 | |
| Instance Segmentation | 实例分割 | |
| YOLO | YOLO（实时目标检测） | You Only Look Once |
| OpenVINO | OpenVINO（Intel 推理工具包） | |
| ONNX | ONNX（开放神经网络交换） | |
| Optical Character Recognition (OCR) | 光学字符识别 | |
| Visual Grounding | 视觉定位 | |
| Bounding Box | 边界框 | |

## 微调与训练

| 英文 | 首选中文 | 别名/说明 |
|------|---------|----------|
| Supervised Fine-Tuning (SFT) | 监督微调 | |
| Parameter-Efficient Fine-Tuning (PEFT) | 参数高效微调 | |
| LLaMA Factory | LLaMA Factory（微调框架） | |
| SWIFT | SWIFT（阿里微调框架） | |
| MLX | MLX（Apple 机器学习框架） | |
| Dataset Preparation | 数据集制备 | |
| Data Annotation | 数据标注 | |
| Synthetic Data | 合成数据 | |
| Knowledge Distillation | 知识蒸馏 | |

---

## 使用指南

1. **锁定翻译**：每个术语的"首选中文"列是全 Wiki 统一使用的翻译
2. **避免混用**：同一概念不应在多个页面中使用不同翻译
3. **首次出现加英文**：正文中首次出现术语时，格式为 `中文（English）`
4. **新增术语**：在 subagent 写作中发现未收录术语时，先在此表补充
5. **Wikilink 约定**：核心术语在正文中首次出现时，使用 `[[术语页|中文（English）]]` 格式添加链接

## 术语收录状态

- [x] 具身智能相关术语
- [x] 语音处理相关术语
- [x] 量化相关术语
- [x] 华为昇腾相关术语
- [x] 计算机视觉相关术语
- [x] 微调与训练相关术语
- [x] Agent 与 MCP 相关术语
