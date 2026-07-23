---
title: Kubernetes-编排
type: topic
topic: Kubernetes-编排
domain: 工程与基础设施
tags: [kubernetes, orchestration, workloads, scheduling, networking, security, gpu, helm, prometheus, storage]
last_updated: 2026-07-21
status: complete
---

# Kubernetes-编排

> 领域：工程与基础设施

## 概述

Kubernetes 是容器编排领域的事实标准，构建声明式驱动的工作负载管理体系，驱动集群资源的高效调度与自动化运维。其核心设计是"声明式 API + 控制器模式"——用户描述期望状态，控制平面持续协调实际状态向期望状态收敛。理解 Kubernetes 需掌握分层架构：控制平面（API Server、Scheduler、Controller Manager、etcd）负责决策，工作节点（Kubelet、kube-proxy）负责执行。

本主题汇聚 33 篇实践笔记，覆盖集群搭建（kubeadm、Minikube）、API 对象模型（标签/注解/名字空间）、工作负载管理（ReplicaSet、DaemonSet、Job/CronJob、StatefulSet）、调度策略（污点/容忍度、节点/Pod 亲和性）、服务网络（Service、Ingress）、安全控制（RBAC、ServiceAccount）、资源管理（QoS、LimitRange、ResourceQuota）、持久化存储（StorageClass、Velero 备份）、可观测性栈（Prometheus Operator + Grafana）以及机器学习平台实践。

## 实践页链接

- [[practices/Kubernetes-编排]] — Kubernetes 编排完整实践手册（33 篇文章，2021–2023）

## 关键知识点

1. **集群搭建** — kubeadm 初始化流程、cgroupDriver=systemd 对齐、网络插件（Weave Net）、证书过期处理（kubeadm alpha certs renew）
2. **API 对象模型** — 四大核心字段（apiVersion/kind/metadata/spec）、标签选择器、注解（Annotations）、JSONPath 查询
3. **工作负载** — ReplicaSet 副本维持、DaemonSet 节点级部署、Job/CronJob 任务调度、StatefulSet 有状态服务（稳定网络标识 + 数据克隆）
4. **调度策略** — 污点（NoSchedule/PreferNoSchedule/NoExecute）与容忍度、节点亲和性（required/preferred）、Pod 亲和/反亲和、自定义调度器策略（MostRequested/LeastRequested）
5. **服务网络** — Service 三种类型（ClusterIP/NodePort/LoadBalancer）、CoreDNS 服务发现、Ingress 七层路由、端口转发调试
6. **安全控制** — RBAC（Role/ClusterRole + RoleBinding）、ServiceAccount 身份凭证、API 服务器认证链
7. **资源管理** — requests/limits 定义、QoS 三级（Guaranteed/Burstable/BestEffort）、LimitRange 默认值、ResourceQuota 总量限制、NVIDIA Device Plugin GPU 调度
8. **持久化存储** — StorageClass 动态供给、NFS Subdir External Provisioner、Velero 备份与迁移（快照 vs Restic 文件级）
9. **可观测性** — Prometheus Operator（ServiceMonitor/PodMonitor CRD）、Grafana 仪表板、Alertmanager 告警路由
10. **生产运维** — 节点管理（drain/reset/join）、Dashboard 部署、ECK Operator、MySQL 主从集群

## 相关主题链接

- [[topics/Docker-容器化]] — 容器化基础与 Docker 实践
- [[topics/GPU-与-CUDA-开发]] — GPU 开发与 K8s GPU 共享
- [[topics/Linux-与系统管理]] — Linux 系统管理基础
