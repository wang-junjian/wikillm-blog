---
title: AI-Agent-编排
type: topic: AI-Agent-编排
domain: LLM 与生成式 AI
tags: [agent, ai-agent, multi-agent, langchain, openclaw, a2a, mcp, tool-use, function-calling, autogen, crewai, cline, gemini-cli, skill]
last_updated: 2026-07-21
status: complete
---

# AI-Agent-编排

> 领域：LLM 与生成式 AI
> 状态：完整

## 概述

AI Agent 编排是构建 LLM 驱动智能系统的核心工程领域，负责协调模型、工具、记忆与人机交互之间的复杂协作——可将其理解为"AI 应用程序的指挥中心"。从简单的单次 LLM 调用，到路由器、状态机、自主代理，智能体性（Agentic）构成一个六级递增的光谱。

本主题覆盖 Agent 编排的完整技术栈：从模型-工具-指令三大核心组件、函数调用与工具调用机制，到提示链/路由/并行化/协调者-工作者/评估器-优化器五种工作流模式，再到 MCP/A2A 通信协议标准、记忆系统、GUI 代理、主流编排框架对比，以及编码智能体、Hermes 自进化机制、KiloClaw 安全架构等深度实践。

## 核心概念页

- [[concepts/AI-Agent-编排]]——Agent 编排的完整技术体系，涵盖智能体光谱、核心组件、工具调用机制、编排模式、通信协议、记忆系统、GUI 代理、框架对比、工程实践与开发方法论

## 关键知识点

1. **[[智能体光谱]]**——从纯代码到自主代理的六级递增：单次 LLM 调用→调用链→路由器→状态机→自主代理
2. **[[函数调用]]（Function Calling）**——LLM 接收函数定义的 JSON Schema，根据用户输入选择调用哪个函数及参数
3. **[[LangGraph]]**——基于图结构的编排框架，通过状态机模式支持分支、循环和持久化状态
4. **[[MCP]] 与 [[A2A-协议]]**——MCP 连接代理与工具（结构化输入输出），A2A 实现代理间对等协作（自然模态交互）
5. **[[记忆系统]]**——程序性/语义/情景/工作四类记忆；OpenClaw 采用 Markdown 文件管理，双路索引（Embedding + TF-IDF）检索
6. **[[Computer-Using Agent]]（CUA）**——OpenAI 提出的计算机使用代理，通过感知-推理-行动循环操作 GUI
7. **[[UI-TARS]]**——字节跳动提出的原生 GUI 代理模型，端到端设计仅感知截图输入
8. **[[编码智能体的核心组件]]**——Sebastian Raschka 提出的六大组件：实时仓库上下文、提示词结构、工具访问、上下文膨胀抑制、会话记忆、子智能体委派
9. **[[Hermes-智能体]]**——Nous Research 开发，核心创新在于自进化学习闭环（自主技能创建 + 持续优化）
10. **[[KiloClaw-安全白皮书]]**——五层租户隔离架构：身份路由→应用隔离→网络隔离→Firecracker 虚拟机→卷隔离

## 重要来源

- Anthropic 构建有效代理、LangChain In the Loop 认知架构
- OpenClaw 架构、记忆系统、技能系统与语音通话插件
- Kilo Code 架构设计与编码智能体最佳实践
- Hermes 智能体研究报告与 OpenClaw 对比分析
- A2A 协议与 MCP 协议的互补关系
- Reachy Mini 机器人语音对话智能体开发

## 相关主题

- [[topics/MCP-协议栈]]——智能体工具集成的标准协议
- [[topics/LLM-编码助手]]——Cline/Claude Code 等编码智能体实践
- [[topics/LLM-推理优化]]——Agent 场景下的前缀缓存与级联推理优化
- [[topics/Prompt-Engineering-与上下文工程]]——提示工程作为 Agent 编排的基础层
- [[topics/具身智能与机器人]]——Reachy Mini 等物理智能体编排
