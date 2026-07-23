---
title: Whisper
type: concept
tags: [whisper, speech-recognition, asr, openai, multilingual, transcription, audio-processing, encoder-decoder, transformer, weak-supervision]
last_updated: 2026-07-21
---

# Whisper

Whisper 是 [[OpenAI]] 于 2022 年 9 月开源的自动语音识别（ASR）模型，以其强大的多语言转录能力和鲁棒性著称。该模型在 68 万小时的多语言、多任务监督数据上训练，涵盖了 99 种语言的语音转录和翻译能力。Whisper 的发布标志着开源 ASR 领域的一次重大突破——在此之前，高精度多语言语音识别主要依赖商业 API（如 Google Cloud Speech-to-Text、Azure Speech Services），而 Whisper 以开源形式提供了接近商业方案的性能。

Whisper 的核心方法论是"弱监督的大规模预训练"——利用互联网上大量存在的音视频及其字幕文本作为训练数据，通过自动对齐和过滤构建大规模训练集。这种方法避免了对精确标注的依赖，使得模型能够从海量数据中学习语音与文本的对应关系。Whisper 采用标准的 [[Transformer]] 编码器-解码器架构，支持语音转录（Speech-to-Text）和语音翻译（Speech-to-English Translation）两种任务。

## 核心概念

### 编码器-解码器架构

Whisper 采用 [[Transformer]] 编码器-解码器架构，输入为音频的 log-Mel 频谱图（log-Mel spectrogram），输出为文本 token 序列：

- **编码器**：处理 30 秒音频片段的 log-Mel 频谱图，提取声学特征表示
- **解码器**：自回归生成文本 token，支持多任务预测（转录、翻译、时间戳、语言识别）
- **特殊 Token**：模型通过特殊 token 区分不同任务（`<|transcribe|>`、`<|translate|>`）、语言（`<|zh|>`、`<|en|>`）和时间戳（`<|0.00|>`）

这种统一的架构设计使单个模型能够处理多种语音任务，无需为每种语言或任务训练独立的模型。

### 多语言与多任务能力

Whisper 支持 99 种语言的语音识别和语音到英语的翻译。在训练数据分布上，英语数据占约 65%，非英语数据占 35%。模型的多语言能力体现在：

- **语言自动识别**：自动检测输入音频的语言，无需手动指定
- **多语言转录**：直接输出对应语言的文本
- **语音翻译**：将非英语语音直接翻译为英语文本
- **代码切换**：处理同一句话中混合多种语言的情况

在 Multilingual LibriSpeech（MLS）基准上，Whisper large-v3 的词错误率（WER）达到业界领先水平。

### 模型规模与变体

Whisper 提供多种规模的模型变体，用户可根据精度和速度需求选择：

| 模型 | 参数量 | 英文 WER | 多语言 WER | 推理速度 |
|------|--------|----------|-----------|---------|
| tiny | 39M | 15.6 | 34.3 | ~32x |
| base | 74M | 10.3 | 24.0 | ~16x |
| small | 244M | 6.2 | 15.8 | ~6x |
| medium | 769M | 4.8 | 11.6 | ~2x |
| large-v3 | 1.55B | 3.6 | 8.6 | 1x |
| large-v3-turbo | 809M | 4.2 | 9.5 | ~1.5x |

其中 large-v3-turbo 是 OpenAI 在 GPT-4o 发布后推出的优化版本，在保持较高精度的同时显著提升了推理速度。

### 鲁棒性与泛化能力

Whisper 在噪声环境、口音变化、技术术语等挑战性场景下仍保持较高的识别准确率。这得益于：

- **大规模多样化训练数据**：涵盖不同口音、噪声环境、录音设备
- **数据增强**：训练时加入背景噪声、混响等增强
- **上下文学习**：模型能够利用上下文纠正识别错误

在实际应用中，Whisper 对中文普通话的识别效果优秀，对粤语、四川话等方言也有一定识别能力，但效果因方言差异而异。

### 开源生态

Whisper 的开源催生了丰富的生态工具：

- **faster-whisper**：基于 CTranslat2 的加速实现，速度提升 4-5 倍
- **whisper.cpp**：纯 C/C++ 实现，支持 [[Apple Silicon]]、[[CUDA]]、CPU
- **WhisperX**：支持词级时间戳和说话人分离
- **insanely-fast-whisper**：基于 Optimum 的快速推理工具
- **Whisper Live**：实时流式转录

## 技术架构

```mermaid
flowchart LR
    A[音频输入] B[log-Mel 频谱图] C[Transformer 编码器] D[Transformer 解码器] E[文本输出]
    A --> B --> C --> D --> E
    F[特殊 Token] --> D
    G[语言检测] --> D
    H[时间戳预测] --> D
```

## 应用场景

- **会议转录**：将会议录音自动转为文字记录，支持多语言会议
- **视频字幕生成**：为视频内容自动生成多语言字幕
- **语音助手**：作为语音交互系统的 ASR 前端
- **播客与采访整理**：将长篇音频内容转为可搜索的文本
- **语言学习**：对比发音与标准文本，辅助语言学习
- **无障碍服务**：为听障人士提供实时字幕和语音转文字

## 相关技术

- [[语音与音频处理]]——Whisper 所属的语音技术体系
- [[Transformer]]——Whisper 采用的模型架构
- [[MLX]]——在 Apple Silicon 上运行 Whisper 的框架
- [[faster-whisper]]——Whisper 的加速实现
- [[说话人分离]]——与 Whisper 配合的多说话人识别技术

## 主要页面

- [[语音与音频处理]] - 语音识别与音频处理技术体系
- [[MLX]] - 在 Apple Silicon 上运行 Whisper 的实践
