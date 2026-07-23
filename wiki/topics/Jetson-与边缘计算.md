---
title: Jetson-与边缘计算
type: topic
topic: Jetson-与边缘计算
domain: AI 硬件与芯片加速
tags: [jetson, edge-computing, edge-ai, nvidia, jetson-thor, jetson-agx-orin, embedded, onnx-runtime, litert-lm, physical-ai]
last_updated: 2026-07-21
status: complete
---

# Jetson-与边缘计算

> 领域：AI 硬件与芯片加速

## 概述

边缘计算将 AI 推理从云端下沉到数据源附近，以低延迟、高隐私、离线可用的方式驱动实时智能。其本质是在数据产生的位置附近完成推理决策，避免海量原始数据向云端回传带来的延迟与带宽开销。嵌入式 AI 芯片需要在功耗、算力、成本之间做出严苛的权衡（Trade-off）——从寒武纪 MLU220 的嵌入式系统编译，到百度 EasyEdge 的端云协同平台，再到 NVIDIA Jetson 系列的大模型落地，边缘 AI 正从"能否运行"走向"能否规模化部署"。

本主题聚合 Jetson 平台演进（AGX Orin → Thor）、边缘硬件选型（GPU/VPU/NPU/SoC）、端侧大模型部署（vLLM/Ollama/llama.cpp/LiteRT-LM）、电力等行业应用（1D-CNN 故障识别、Autoencoder 入侵检测）、嵌入式系统编译（Buildroot/OpenIL）、Google AI Edge 生态（LiteRT/LiteRT-LM/AI Edge Gallery），以及具身智能与 Physical AI 前沿。

## 实践页链接

- [[practices/Jetson-与边缘计算]] — Jetson 与边缘计算完整实践手册（10 篇文章，2022–2026）

## 关键知识点

1. **Jetson 平台演进** — AGX Orin（CUDA 8.7）大模型部署困境（JetPack 5.x 版本锁定）、Jetson Thor（Blackwell GPU + Isaac ROS）
2. **版本依赖链** — 推理框架（vLLM 需 CUDA 11.8+、Ollama 需驱动 531+）→ 驱动 → 操作系统（JetPack 6.0 强制 Ubuntu 22.04）→ 机器人中间件（ROS1/ROS2）
3. **边缘硬件生态** — Jetson Orin/Thor、Intel Movidius Myriad X、寒武纪 MLU220、昇腾 310；NVMe/LPDDR/M.2 存储内存技术
4. **端侧推理框架** — vLLM（JetPack 6.0+）、Ollama、llama.cpp（全系列兼容）、LiteRT-LM（Android/iOS/Linux 跨平台）
5. **多模态端侧模型** — Gemma 4 12B（16GB VRAM 运行、35M 参数视觉嵌入器、16kHz 音频线性投影）
6. **电力边缘 AI** — 1D-CNN 毫秒级故障识别、Autoencoder 入侵检测、Bi-LSTM 预测性维护、PCA+VAE 数据压缩
7. **端侧工具链** — 百度 EasyEdge（Paddle Lite 端云协同）、Google AI Edge（LiteRT/LiteRT-LM/Gallery/Eloquent）
8. **嵌入式系统编译** — Buildroot 交叉编译、OpenIL 开源工业 Linux、寒武纪 MLU220 系统构建
9. **具身智能** — Physical AI（GROOT 人形机器人基础模型 + Isaac Lab 仿真 + Omniverse 数字孪生）、世界模型（World Model）
10. **NITROS 加速** — NVIDIA Isaac Transport for ROS 2 消息硬件加速传输、端到端传感器到推理延迟优化

## 相关主题链接

- [[topics/GPU-与-CUDA-开发]] — NVIDIA GPU 开发与 CUDA 基础
- [[topics/华为昇腾与国产芯片]] — 国产边缘 AI 芯片方案
- [[topics/计算机视觉与目标检测]] — 边缘端视觉推理算法
