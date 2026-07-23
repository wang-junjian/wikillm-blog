---
title: Verdaccio
type: concept
tags: [verdaccio, npm, private-registry, node.js, package-management, proxy-cache, 私有仓库, npm代理, 包管理]
last_updated: 2026-07-21
---

# Verdaccio

Verdaccio 是一个轻量级的私有 npm 代理注册表（Private npm Registry），用于在企业内部搭建私有 Node.js 包管理仓库。它既是 npm 公共注册表的缓存代理，也支持私有包的发布和管理，是前端团队和 Node.js 开发者构建自主可控包管理基础设施的理想选择。Verdaccio 采用 MIT 开源协议，以零配置启动、低资源消耗和插件化架构著称。

npm（Node Package Manager）是 Node.js 生态的包管理工具，公共注册表（registry.npmjs.org）托管了超过 200 万个开源包。然而在企业环境中，直接使用公共注册表面临诸多挑战：网络依赖（外网不稳定或不可达）、安全审计（第三方包的安全风险）、私有包管理（企业内部包的发布和共享）、版本稳定性（公共包的破坏性更新）。Verdaccio 通过搭建本地代理仓库，有效解决了这些问题。

## 核心功能

**代理缓存**是 Verdaccio 的基础功能。当开发者请求一个包时，Verdaccio 首先检查本地缓存；如果未命中，则从上游注册表（默认 npmjs.org）拉取并缓存。后续相同请求直接从本地缓存响应，大幅提升安装速度并降低外网依赖。缓存策略支持 TTL 配置和手动刷新。

**私有包发布**支持企业内部包的版本管理。通过 `npm publish --registry http://localhost:4873` 将私有包发布到 Verdaccio，团队成员通过相同地址安装。Verdaccio 支持语义化版本（SemVer）、标签（Tag）和访问控制，满足企业包管理的完整需求。

**用户认证**保障私有包的安全访问。Verdaccio 内置 htpasswd 认证，支持 LDAP、GitHub OAuth、GitLab 等多种认证方式（通过插件）。发布权限和访问权限可细粒度控制，确保只有授权用户能发布或安装特定包。

**插件化架构**提供灵活的扩展能力。Verdaccio 设计了丰富的插件接口，支持自定义认证、存储后端、中间件、UI 主题等。社区提供了大量插件：S3/MinIO 存储后端、GitHub OAuth 认证、审计日志、Webhook 通知等。

## 部署方式

**本地开发部署**最简单的方式是通过 npx 直接启动：`npx verdaccio`，默认监听 4873 端口。适合个人开发者和小型团队的快速验证。

**Docker 部署**是生产环境推荐方式。Verdaccio 提供官方 Docker 镜像，通过 Docker Compose 可快速搭建包含持久化存储的私有仓库：

```yaml
services:
  verdaccio:
    image: verdaccio/verdaccio
    ports:
      - "4873:4873"
    volumes:
      - ./storage:/verdaccio/storage
      - ./config:/verdaccio/conf
```

**Kubernetes 部署**适合大规模企业环境。通过 Helm Chart 部署 Verdaccio，结合 Persistent Volume 提供持久化存储，Ingress 提供外部访问，ConfigMap 管理配置。

## 配置管理

Verdaccio 的核心配置是 `config.yaml`，主要配置项包括：**uplinks**（上游注册表配置，支持多个上游和优先级）、**packages**（包访问控制，支持作用域包和正则匹配）、**listen**（监听地址和端口）、**auth**（认证插件配置）、**storage**（存储路径或外部存储后端）、**middlewares**（中间件配置，如审计日志）。

典型的包访问控制配置示例：
```yaml
packages:
  '@mycompany/*':
    access: $authenticated
    publish: $authenticated
    proxy: npmjs
  '**':
    access: $all
    publish: $authenticated
    proxy: npmjs
```

## 应用场景

Verdaccio 在前端工程化中扮演重要角色：**企业私有仓库**（内部组件库、工具库的发布和共享）、**npm 缓存代理**（加速 CI/CD 构建，降低外网依赖）、**离线开发环境**（内网环境下的包管理）、**安全审计**（私有包的安全扫描和版本锁定）、**多源聚合**（同时代理 npmjs、淘宝镜像等多个上游）。

## 相关概念

- [[Web-开发与在线工具]] — 前端工程化与包管理生态
- [[网络与分布式存储]] — Verdaccio 的存储后端集成
- [[MinIO]] — Verdaccio 的 S3 兼容存储后端
- [[Docker-容器化]] — Verdaccio 容器化部署

## 主要页面

- [[topics/Web-开发与在线工具]] — 前端工程化与 Verdaccio 实践
- [[topics/网络与分布式存储]] — Verdaccio 存储后端配置
- [[topics/Docker-容器化]] — Verdaccio Docker 部署与运维
