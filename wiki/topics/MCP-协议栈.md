---
title: MCP-协议栈
type: topic
topic: MCP-协议栈
domain: LLM 与生成式 AI
tags: [mcp, model-context-protocol, json-rpc, client-server, transport, tools, resources, prompts, sdk, authorization]
last_updated: 2026-07-21
status: complete
---

# MCP-协议栈

> 领域：LLM 与生成式 AI
> 状态：完整

## 概述

模型上下文协议（Model Context Protocol，MCP）是一套开放标准，负责规范化 LLM 应用程序与外部数据源、工具之间的集成方式——可将其理解为 AI 应用程序的"USB-C 端口"。MCP 采用客户端-主机-服务器三元架构，以 JSON-RPC 2.0 作为线路格式，通过能力协商机制实现渐进式扩展。

本主题覆盖 MCP 的完整协议栈：从基础协议与连接生命周期、stdio/Streamable-HTTP 两种标准传输，到资源/工具/提示三类服务器功能原语，再到 Python/TypeScript/Java/Kotlin/Rust 多语言 SDK 生态。同时涵盖 MCPHub 聚合平台与智能路由、FastMCP 高级抽象、Cline 自然语言驱动开发、OpenClaw 智能体平台等实践，以及 OAuth 2.1 授权框架与安全模型。

## 核心概念页

- [[concepts/MCP-协议栈]]——MCP 协议的完整技术栈，涵盖设计哲学、核心架构、基础协议、传输机制、授权框架、服务器功能原语、SDK 生态、客户端/服务器生态、安全考量与能力协商

## 关键知识点

1. **[[MCP-架构]]**——客户端-主机-服务器三元架构，主机作为容器与协调器，客户端与服务器维持 1:1 有状态会话
2. **[[JSON-RPC]] 2.0**——MCP 的线路格式，定义请求、响应、通知三种消息类型，支持批处理
3. **[[能力协商]]**——初始化阶段显式声明支持的功能（prompts/resources/tools/logging/sampling/roots），保持协议可扩展性
4. **[[stdio]] 与 [[Streamable-HTTP]]**——两种标准传输：本地进程间通信 vs 远程多客户端连接，后者支持 SSE 流式推送与会话恢复
5. **[[MCP-服务器功能]]**——资源（应用程序控制的上下文数据）、工具（模型控制的可执行函数）、提示（用户控制的交互模板）三类核心原语
6. **[[FastMCP]]**——Python MCP SDK 的高级抽象，通过装饰器暴露工具、资源和提示，支持 stdio 与 Streamable-HTTP 双传输
7. **[[MCPHub]]**——MCP 服务器聚合平台，通过语义向量匹配实现智能路由，解决工具数量膨胀问题
8. **[[OAuth-2.1]] 授权**——MCP 的授权框架，支持动态客户端注册与授权服务器元数据发现
9. **[[Claude-Skill]]**——与 MCP 互补的知识封装，教导 Claude 如何有效使用服务（MCP 提供连接性，技能提供工作流知识）
10. **[[llms.txt]]**——Jeremy Howard 提出的网站标准化提案，为 LLM 提供简洁专业的内容访问入口

## 重要来源

- MCP 协议规范、架构设计、基础协议与服务器功能详解
- Cline 构建 MCP 服务器、MCP 快速入门与服务器开发协议
- MCPHub 智能路由与内网离线部署方案
- FastMCP 服务器与客户端开发实战
- OpenClaw 智能体平台架构、记忆系统与技能系统
- Claude Skill 构建指南与渐进式披露结构

## 相关主题

- [[topics/AI-Agent-编排]]——MCP 作为智能体工具集成的标准协议
- [[topics/LLM-编码助手]]——Continue/Cursor/Cline 等编码工具对 MCP 的支持
- [[topics/LLM-部署与开源生态]]——MCP 服务器的部署与网关集成
- [[topics/RAG-检索增强生成]]——RAGFlow MCP Server 将知识库问答能力接入编码工具
