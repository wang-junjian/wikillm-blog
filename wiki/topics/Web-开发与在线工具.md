---
title: Web-开发与在线工具
type: topic
topic: Web-开发与在线工具
domain: 数据、存储与 Web
tags: [web-development, static-site, ai-coding-agent, llm, nextjs, typescript, rust, knowledge-graph, minhash, blog-design, browser-api, code-attribution]
last_updated: 2026-07-21
status: complete
---

# Web 开发与在线工具

> 领域：数据、存储与 Web

## 概述

从静态站点生成器到 AI 编码智能体，从代码知识图谱到浏览器原生 API——本主题聚合作者在 Web 开发、在线工具构建、AI 编程助手架构等领域的实践与思考。时间跨度 2020–2026，覆盖 29 篇文章、八大主题领域。

Web 开发生态正经历 AI 驱动的重构：Cline 将 Agent Loop 嵌入 VS Code，Vercel AI SDK 实现 50+ 提供商零成本切换，Kilo Code 构建"全栈智能体工程平台"；代码知识图谱（Understand-Anything、code-review-graph）将代码库转化为交互式图谱；MinHash + LSH 算法支撑文本去重与代码归因量化；浏览器原生能力（Web Speech API、Canvas、QR Code）解锁纯前端 AI 应用可能。

## 实践页链接

- [[practices/Web-开发与在线工具]] — Web 开发与在线工具完整实践手册（29 篇文章，2020–2026）

## 关键知识点

1. **AI 编码智能体** — Cline 五层架构（表示/应用/领域/基础设施/数据）、Vercel AI SDK（LanguageModelV4 接口、useChat Hook）、Claude Code 插件系统（plugin.json + 事件驱动）
2. **Kilo Code 生态** — VS Code 扩展 + CLI + Cloud 三位一体、500+ AI 模型集成、Memory Bank 长期记忆、Agent Manager 多智能体编排（Git Worktree 隔离）
3. **智能体运行时** — TypeScript Namespace 组织、AsyncLocalStorage 单例、Zod Schema 验证、Hono HTTP Server + SSE 通信
4. **安全架构** — KiloClaw 五层租户隔离（JWT 路由 → Fly 应用 → WireGuard → Firecracker VM → LUKS 加密卷）、故障闭合身份验证
5. **代码图谱** — Understand-Anything（6 智能体并行流水线、knowledge-graph.json）、code-review-graph（Tree-sitter 解析、Token 用量降低 5–10 倍）
6. **MinHash 算法** — Jaccard 相似度、MinHash 核心定理、LSH 分桶策略（128 维 × 16 band）、MurmurHash3 工程实现
7. **代码归因** — AST-aware MinHash 指纹（k-Shingle、变量重命名免疫）、行级 Diff 归因算法、置信度分级（HIGH/LOW/SUSPECT/UNIQUE）
8. **静态博客** — Jekyll Docker 容器化、Simon Willison 博客设计研究（六种内容类型融合）、Giscus 评论方案（GitHub Discussions 原生）
9. **浏览器 API** — Web Speech TTS（语音列表异步加载、多层回退选择、长文本分句、Watchdog 机制）、QR Code 中文编解码
10. **知识表示** — llms.txt（LLM 友好 Web 标准）、Open Knowledge Format（OKF，YAML frontmatter + Markdown + 交叉链接）

## 相关主题链接

- [[topics/LLM-编码助手]] — LLM 编码助手专题
- [[topics/计算机视觉与目标检测]] — 前端视觉应用
- [[topics/引用链接与科技评论]] — 行业洞察与人物观点
