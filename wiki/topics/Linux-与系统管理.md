---
title: Linux-与系统管理
type: topic
topic: Linux-与系统管理
domain: 工程与基础设施
tags: [linux, ubuntu, sysadmin, ssh, networking, command-line, storage, mirror, docker, kubernetes, shell, performance, openvino, edge-computing, model-optimization, fastapi, nvidia]
last_updated: 2026-07-21
status: complete
---

# Linux 与系统管理

> 领域：工程与基础设施

## 概述

面向 Ubuntu 生态的 Linux 系统管理实战手册，覆盖远程访问、网络配置、存储管理、镜像源加速、Shell 脚本、性能调优、边缘 AI 推理与模型部署。Linux 是整个工程与基础设施领域的基石——掌握其系统管理能力后，可平滑过渡到 [[Docker-容器化|Docker 容器化]] 与 [[Kubernetes-编排|Kubernetes 编排]] 等上层平台。

本主题汇聚 79 篇实践笔记，时间跨度 2018–2022，覆盖 29 个维度：SSH 服务与密钥认证、netplan 网络配置、NFS 文件共享、磁盘分区格式化挂载、用户/时区/输入法管理、apt/Docker/K8s/pip 镜像源加速、命令行工具链（ls/wget/sed/grep/find/cp/tar/zip/base64）、文件权限与链接、Shell 编程、系统监控（top/du/stress/sysstat）、Vim/Thonny/Fritzing 开发工具、AI 数据集打包、嵌入式系统编译（Buildroot）、Go 语言环境、MinIO 对象存储、HTTP 基准测试（wrk/ab）、FastAPI REST API 部署、OpenVINO 推理引擎、NVIDIA 软件栈与 GPU 切换、模型优化（Conv-BN 融合/ONNX Simplifier/TVM）、边缘 AI 平台。

## 实践页链接

- [[practices/Linux-与系统管理]] — Linux 与系统管理完整实践手册（79 篇文章，2018–2022）

## 关键知识点

1. **SSH 远程管理** — openssh-server 安装、密钥认证（ssh-keygen + authorized_keys）、root 密码登录权衡、X11 Forwarding 图形转发
2. **网络配置** — netplan 静态 IP、systemd-resolved DNS 设置、NFS 文件共享（服务端/客户端）
3. **存储管理** — fdisk 分区 → mkfs 格式化 → mount 挂载 → fstab UUID 持久化、K8s 禁用交换分区
4. **镜像源加速** — apt（sed 替换 sources.list）、Docker daemon.json、Kubernetes apt-key、pip config、GitHub 加速（cnpmjs/hosts）
5. **命令行工具** — ls/wget/sed/grep/find/cp/tar/zip/base64、ImageMagick 图像处理、cp -u 批量拷贝性能最优
6. **Shell 编程** — 执行方式（bash/source/./）、变量作用域与 export、重定向、快捷键（Ctrl+r/l/a/e）
7. **性能调优** — 平均负载（Load Average）概念、CPU/I/O/进程三类场景分析、mpstat/pidstat 工具
8. **权限管理** — chown 所有权、ln 软链接、useradd/usermod 用户增删
9. **包管理与服务** — yum（CentOS 下载+离线安装）、helm（K8s 包管理）、vsftpd FTP 服务器
10. **AI 工程实践** — 数据集打包（tar + scp）、模型自动化发布、OpenVINO IR 转换/推理/分析、PyTorch Conv-BN 融合、ONNX Simplifier、TVM 编译

## 相关主题链接

- [[topics/Docker-容器化]] — 容器化上层平台
- [[topics/Kubernetes-编排]] — 集群编排管理
- [[topics/GPU-与-CUDA-开发]] — GPU 开发与驱动安装
