---
title: MCP
type: concept
tags: [MCP, 协议, AI-Agent, 工具调用]
last_updated: 2026-07-21
---

# MCP

MCP（Model Context Protocol，模型上下文协议）是一种开放标准，用于在 AI 模型与外部数据源、工具之间建立统一的连接协议。它定义了模型如何发现、调用和交互外部能力，使得 AI Agent 能够安全、标准化地访问文件系统、数据库、API 等资源。

MCP 采用客户端-服务器架构，通过 JSON-RPC 协议进行通信，解决了过去每个 AI 应用需要单独集成各种工具的问题，正在成为 AI Agent 生态的通用接口标准。

## 主要页面

- [[MCP-协议栈]] - MCP 协议架构、实现与生态工具链

## 相关概念

- [[AI-Agent-编排]]
- [[LLM]]
- [[工具调用与函数调用]]
