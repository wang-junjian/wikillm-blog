---
batch_id: 37
topic: Docker-容器化
topic_name: Docker-容器化
completed_at: 2026-07-21
target_page: wiki/practices/Docker-容器化.md
action: append (在 batch 35-36 基础上追加)
---

# Batch 37 编译报告

## 处理概览

| 项目 | 值 |
| --- | --- |
| Batch ID | 37 |
| 主题 | Docker-容器化 |
| 处理文章数 | 3 |
| 目标页面 | `wiki/practices/Docker-容器化.md` |
| 操作类型 | 追加（页面已由 batch 35-36 创建） |

## 消耗的来源文件

| # | 文件路径 | SHA-256 | 标题 | 类型 |
| --- | --- | --- | --- | --- |
| 1 | `raw/posts/2024/2024-09-10-Higress-AI-Gateway.md` | `a8abb1229d3592b01935315d2b519361f48940291f2e8e24fe6260a2a8867453` | Higress AI Gateway | concept |
| 2 | `raw/posts/2024/2024-09-11-Kong-AI-Gateway.md` | `65cf88e218179606357a84ee77b5c0d137e99479e8ca55f9908b866c280592b9` | Kong AI Gateway | concept |
| 3 | `raw/posts/2025/2025-06-16-Build-a-local-npm-registry-based-on-Verdaccio.md` | `bd999e251655a1c71ae69e7edd5c24e5a8a6e825467774580a3a702a70741169` | Verdaccio：构建与管理内网 npm 仓库的实践指南 | practice |

## 页面更新内容

### 新增章节

在"实战案例"部分追加两个子章节：

1. **AI 网关容器化部署**
   - **Higress：基于 Envoy 的云原生网关** — 单镜像 all-in-one 部署、端口分配、AI 代理插件配置
   - **Kong：企业级 AI 网关** — PostgreSQL 依赖、数据库迁移、AI 插件生态对比
   - 包含两者的权衡（Trade-off）分析

2. **Verdaccio：内网 npm 仓库**
   - Docker Compose 部署方式
   - 核心配置四大模块（存储、认证、上行链路、包权限）
   - 使用流程（用户创建、发布、安装、源设置）
   - npm 本地缓存注意事项

### frontmatter 更新

- **tags**：新增 `ai-gateway`、`npm-registry`、`verdaccio`、`higress`、`kong`
- **raw_sources**：追加 3 条新来源记录
- **last_updated**：更新为 2026-07-21

## 内部链接统计

新增内容约 850 字，包含 7 个内部链接引用（6 个唯一链接）：

1. [[大模型服务|大模型]]
2. [[云原生]]
3. [[Kubernetes-编排|Kubernetes]]
4. [[WebAssembly|Wasm]]
5. [[可观测性]]
6. [[流量治理]]
7. [[Docker-容器化|Docker 镜像仓库]]

链接密度：每 500 字约 4.1 个链接（达标，要求 ≥ 3）

## 图片引用

本 batch 的 3 个 raw 文件中，Kong 文章包含 4 张图片引用（`/images/2024/Kong/*.png`），Verdaccio 文章包含 1 张图片引用（`/images/2025/Verdaccio/webui.png`）。由于新增内容以部署实践与配置说明为主，未直接引用这些图片（图片多为产品架构图与 UI 截图，与容器化操作说明关联度较低）。如需后续补充，可同步到 `wiki/assets/images/` 并在页面中引用。

## 异常与注意事项

1. **Kong 图片未引用**：Kong 文章中的架构图与截图未在聚合页中引用，主要因新增内容聚焦于部署命令与配置流程，而非产品介绍。
2. **Verdaccio 图片未引用**：Web UI 截图未引用，原因同上。
3. **术语一致性**：已按术语锁定要求，统一使用"网关"、"仓库"、"AI 网关"、"API 网关"。
4. **风格一致性**：保持与 batch 35-36 一致的写作风格，使用"权衡（Trade-off）"等提倡词汇，避免"产生"、"输出"等禁止词汇。

## 质量检查

- [x] 文件名使用 kebab-case
- [x] Wikilink 格式正确
- [x] 每 500 字至少 3 个内部链接（达标）
- [x] frontmatter 的 raw_sources 列出全部来源及其 sha256
- [x] 表达风格：领域资深专家视角，中文撰写
- [x] 禁止词汇检查通过
- [x] 提倡词汇使用：权衡（Trade-off）✓
- [x] 术语锁定：网关、仓库、AI 网关、API 网关
