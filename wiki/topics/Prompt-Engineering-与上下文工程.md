---
title: Prompt-Engineering-与上下文工程
type: topic
topic: Prompt-Engineering-与上下文工程
domain: 大模型与算法研究
tags: [prompt-engineering, chain-of-thought, few-shot-prompting, zero-shot-prompting, role-prompting, in-context-learning, system-prompt, structured-output, hallucination]
last_updated: 2026-07-21
status: complete
---

# Prompt-Engineering-与上下文工程

> 领域：大模型与算法研究
> 状态：完整

## 概述

提示工程（Prompt Engineering）是驾驭 LLM 的核心技艺——通过精心设计的指令、示例与上下文，引导模型在无需更新权重的前提下完成复杂任务。其本质是一套系统性的方法论：将模糊的人类意图转化为模型可执行的精确规范，同时约束输出结构、注入领域知识、规避安全风险。

本主题覆盖提示工程的完整方法论：从零样本/少样本提示、角色提示、输出格式控制等基础模式，到思维链（CoT）推理、提示链与系统架构，再到上下文窗口管理、迭代式提示开发、幻觉缓解、Code Llama 代码生成、Llama Guard 安全分类器等实践。同时涵盖模型评分评估与系统化评估方法论。

## 核心概念页

- [[concepts/Prompt-Engineering-与上下文工程]]——提示工程的完整方法论，涵盖基础提示模式、思维链推理、提示链架构、上下文工程、模型能力与局限、代码生成与安全分类器

## 关键知识点

1. **[[零样本提示]]与[[少样本提示]]**——零样本仅提供任务结构，少样本嵌入 2-5 个已完成示例让模型通过上下文学习捕捉任务模式
2. **[[思维链]]（Chain-of-Thought）**——强制模型输出中间推理步骤，在数学/逻辑/多步决策任务上将准确率提升 30%–50%
3. **[[角色提示]]（Role Prompting）**——为模型赋予特定身份，获得更一致的响应；需注意被恶意利用进行越狱的风险
4. **[[提示链]]（Chaining Prompts）**——将多个提示串联成流水线，LangChain 提供 LLMChain/SimpleSequentialChain/SequentialChain/RouterChain 多种模式
5. **[[上下文学习]]（In-Context Learning）**——示例的排列顺序与多样性直接影响 ICL 效果，质量与多样性比数量更重要
6. **[[幻觉]]（Hallucination）**——LLM 生成流畅可信但完全编造的内容，可通过 RAG 提供事实锚点、要求标注信息来源等策略缓解
7. **[[温度]]参数**——控制输出随机性：0 适合分类/审核，0.7 适合创意写作，1 为最大创造性
8. **[[Llama Guard]]**——专门训练的内容安全分类模型，检测六类不安全内容（暴力/色情/犯罪/枪支/管制物质/自残）
9. **[[Code Llama]]**——Meta 推出的代码专用模型系列，支持代码生成、代码填充与长上下文窗口
10. **[[模型评分评估]]**——让一个 LLM 评估其他 LLM 的输出，从准确性、指令遵循等维度打分

## 重要来源

- Prompt Engineering with Llama 2 系统教程
- ChatGPT Prompt Engineering for Developers 课程
- Building Systems with the ChatGPT API 课程
- LangChain 框架文档

## 相关主题

- [[topics/微调与模型训练]]——当提示工程无法满足需求时的进阶路径
- [[topics/RAG-检索增强生成]]——通过外部知识注入增强提示
- [[topics/AI-Agent-编排]]——提示工程作为 Agent 编排的基础层
- [[topics/LLM-编码助手]]——提示工程在编码场景中的实战应用
- [[topics/LLM-技术报告与前沿论文]]——提示工程的理论基础
