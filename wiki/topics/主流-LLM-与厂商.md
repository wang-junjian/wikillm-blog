---
title: 主流-LLM-与厂商
type: topic
topic: 主流-LLM-与厂商
domain: 大模型生态与前沿
tags: [llm, openai, anthropic, meta, deepseek, claude, gpt, llama, qwen, chatglm, 文心一言, phi-3, minicpm, cogvlm, moe, grpo, fp8, distillation]
last_updated: 2026-07-21
status: complete
---

# 主流-LLM-与厂商

> 领域：大模型生态与前沿
> 状态：完整

## 概述

本主题覆盖 2023–2026 年间国内外主流大模型厂商、旗舰模型与配套生态工具，勾勒出一幅完整的 LLM 厂商全景图。过去三年，大语言模型经历了一条"闭源领跑→开源追赶→推理突破"的演进路径：OpenAI 凭借 GPT 系列率先定义对话式 AI 形态，Anthropic 以 Claude 切入安全与长上下文场景，Meta 通过 Llama 驱动开源生态繁荣，DeepSeek 以 MoE 架构与强化学习推理模型异军突起，Qwen、ChatGLM、文心一言、Phi-3、MiniCPM、CogVLM 则分别占据中文、端侧、多模态等细分高地。

## 核心概念页

- [[concepts/主流-LLM-与厂商]]——国内外主流大模型厂商全景，涵盖 OpenAI、Anthropic、Meta、DeepSeek、阿里、智谱、百度、微软、OpenBMB、字节跳动等厂商的旗舰模型、架构特点与生态工具

## 关键知识点

1. **[[OpenAI]]**——闭源领跑者，GPT 系列与 ChatGPT 产品定义对话式 AI 形态；Deep Research 代表从对话助手到自主研究代理的范式跃迁
2. **[[Anthropic]]**——Claude 系列切入安全与长上下文场景，Computer Use API 标志大模型从信息处理向物理世界操作的延伸
3. **[[Meta]]**——Llama 系列驱动开源生态繁荣，Llama 3 采用新 Tokenizer（128,256 词汇）与 GQA 架构
4. **[[DeepSeek]]**——MoE 架构与强化学习推理模型异军突起：V3（671B/37B 激活，FP8 训练）、R1（GRPO 推理）、V4（1.6T/49B，百万 token 上下文）
5. **[[Qwen-通义千问]]**——阿里全栈 LLM，覆盖 1.8B–72B 多尺度，在 Apple Silicon 上通过 FastChat 部署
6. **[[ChatGLM]]**——智谱中英双语模型，ChatGLM2-6B 带来 GLM 混合目标函数、FlashAttention、Multi-Query Attention 三大升级
7. **[[Microsoft-Phi-3]]**——微软开源轻量级多模态模型，4B 参数验证小模型在端侧多模态任务上的可行性
8. **[[CogVLM2]]**——智谱开源多模态大模型，19B 参数在 OCR 任务上表现突出
9. **[[MiniCPM-Llama3-V-2.5]]**——端侧 GPT-4V 级多模态，8B 参数量在 OpenCompass 榜单上超越 GPT-4V
10. **[[UI-TARS]]**——字节跳动原生 GUI 代理模型，在 OSWorld 基准上以 24.6 分超越 Claude 的 22.0

## 重要来源

- DeepSeek R1/V3/V4 技术报告、DeepSeek-OCR 架构
- Gemini CLI 生态与 DXT 桌面扩展规范
- OpenAI Deep Research 与 Claude Computer Use API
- Llama 3 架构与 SeamlessM4T 多模态翻译
- ChatGLM 系列部署与微调实践、文心一言测试
- SWE-bench 编码基准与 OSWorld GUI 代理评测

## 相关主题

- [[topics/LLM-技术报告与前沿论文]]——DeepSeek R1/V3/V4、UI-TARS、OSWorld 等技术报告深度解读
- [[topics/LLM-推理优化]]——vLLM/SGLang 等推理引擎与 DeepSeek 架构创新
- [[topics/微调与模型训练]]——LLaMA-Factory、OpenAI Fine Tuning 等微调实践
- [[topics/RAG-检索增强生成]]——PrivateGPT、Langchain-Chatchat 等检索增强实践
- [[topics/多模态大模型]]——CogVLM2、MiniCPM-V 2.5、Phi-3-vision 等多模态专题
