---
title: Docker-容器化
type: topic
topic: Docker-容器化
domain: 工程与基础设施
tags: [docker, container, kubernetes, dockerfile, registry, buildkit, devops, deployment, ai-gateway, npm-registry, verdaccio, higress, kong]
last_updated: 2026-07-21
status: complete
---

# Docker-容器化

> 领域：工程与基础设施

## 概述

容器技术彻底改变了软件的构建、分发与运行方式。作为容器生态的事实标准，Docker 通过镜像分层、写时复制与内核级隔离机制，让开发者能够将应用连同依赖打包为轻量、可移植的单元。容器并非虚拟机，而是 Linux 内核能力（Namespace、Cgroups、chroot）组合出的隔离进程——视图隔离、资源限额与根目录隔离三者协同，构建出独立的执行环境。

本主题汇聚从底层原理到生产实践的完整知识体系：Dockerfile 编写优化、镜像仓库管理（私有 Registry、Harbor）、数据持久化、多平台构建（Buildx + QEMU）、GPU 容器化（nvidia-docker2），以及向 [[Kubernetes-编排|Kubernetes 集群]] 编排的平滑过渡。同时覆盖 AI 网关（Higress、Kong）容器化、内网 npm 仓库（Verdaccio）等实战场景。

## 实践页链接

- [[practices/Docker-容器化]] — Docker 容器化完整实践手册（27 篇文章，2018–2025）

## 关键知识点

1. **容器本质** — Linux Namespace（PID/Mount/Network/UTS 视图隔离）+ Cgroups（CPU/内存/IO 资源限额）+ chroot/pivot_root（根目录隔离）
2. **Dockerfile 编写** — 基础指令（FROM/RUN/COPY/ENV/ARG/ENTRYPOINT）、ARG 作用域（FROM 之前 vs 之后）、多阶段构建缩小镜像体积
3. **镜像优化** — BuildKit 缓存挂载（`RUN --mount=type=cache`）、依赖分层优化、`--no-cache-dir` 与 `--no-install-recommends` 压缩层
4. **仓库管理** — 私有 Registry（registry:2）、Harbor 企业级仓库（RBAC/漏洞扫描/签名）、PyPI 私有仓库（PyPIServer）
5. **数据持久化** — emptyDir / hostPath / NFS / configMap / secret 卷类型，tmpfs 内存卷
6. **GPU 容器化** — nvidia-docker2 安装、`NVIDIA_VISIBLE_DEVICES` 多卡隔离、离线安装方案
7. **多平台构建** — Docker Buildx + docker-container 驱动、QEMU 交叉编译、manifest list 推送
8. **AI 网关** — Higress（Envoy 云原生 all-in-one）vs Kong（PostgreSQL 企业级插件生态）的权衡
9. **npm 仓库** — Verdaccio 容器化部署、htpasswd 鉴权、代理缓存机制
10. **故障排查** — macOS Docker.raw 膨胀、cgroup driver 不匹配、CNI 未初始化

## 相关主题链接

- [[topics/Kubernetes-编排]] — 容器编排与集群管理
- [[topics/GPU-与-CUDA-开发]] — GPU 开发与容器化推理
- [[topics/macOS-与-Apple-Silicon]] — macOS 平台 Docker 实践
