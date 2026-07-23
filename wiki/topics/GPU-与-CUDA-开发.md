---
title: GPU-与-CUDA-开发
type: topic
topic: GPU-与-CUDA-开发
domain: AI 硬件与芯片加速
tags: [gpu, cuda, nvidia, tensorrt, onnxruntime, llm-inference, kubernetes, docker, driver, deep-learning, tvm, ffmpeg]
last_updated: 2026-07-21
status: complete
---

# GPU-与-CUDA-开发

> 领域：AI 硬件与芯片加速

## 概述

图形处理器（GPU）已从单纯的图形渲染加速器，演变为驱动深度学习、科学计算和物理 AI 的核心算力引擎。现代 GPU 开发栈是一个分层架构：硬件 → 驱动 → CUDA Toolkit → 加速库（cuDNN、TensorRT、NCCL）→ 框架（PyTorch、PaddlePaddle）→ 服务层（ONNXRuntime、TensorRT-LLM、Triton）。理解每一层的职责与依赖关系，是排查版本兼容性问题的关键——驱动版本决定最高 CUDA 版本，CUDA 版本约束 cuDNN 和 TensorRT 版本。

本主题系统梳理 NVIDIA 生态下的驱动安装（APT/Runfile）、CUDA Toolkit 配置、容器化 GPU 方案（nvidia-docker2、K8s GPU 共享）、推理服务部署（ONNXRuntime、PaddlePaddle、TensorRT-LLM + Triton）、软件栈全貌、FFmpeg GPU 加速、TVM 深度学习编译器，以及 Jetson Thor 边缘设备配置。

## 实践页链接

- [[practices/GPU-与-CUDA-开发]] — GPU 与 CUDA 开发完整实践手册（20 篇文章，2020–2026）

## 关键知识点

1. **驱动安装** — APT 方式（ubuntu-drivers）vs Runfile 手动安装（禁用 nouveau）、`nvidia-smi` 验证、驱动卸载与切换
2. **CUDA Toolkit** — Runfile/APT 安装、nvcc 编译器、deviceQuery 验证、多版本管理（软链接切换）
3. **容器化 GPU** — nvidia-docker2 安装与验证、K8s GPU 共享（阿里云 gpu-mem、GaiaGPU/vCUDA）、NVIDIA Device Plugin
4. **推理引擎** — ONNXRuntime（CUDA/TensorRT EP）、PaddlePaddle GPU 镜像、TensorRT-LLM 引擎构建 + Triton 服务化
5. **LLM 部署** — Qwen/ChatGLM/Baichuan 开源模型部署、Flash-Attention 加速、INT8/INT4 量化
6. **软件栈** — GPU Driver → CUDA → cuDNN → TensorRT → NCCL 分层架构、全栈 AI 方案（NIM/NeMo/Isaac Lab）
7. **系统信息** — lspci/modinfo/nvcc/nvidia-smi 查看 GPU 状态、驱动版本、CUDA 版本
8. **FFmpeg 加速** — NVENC 硬编码、CUVID 解码、h264_nvenc/libx264 性能对比
9. **TVM 编译器** — 源码安装（LLVM 依赖）、CUDA/OpenCL/Vulkan 后端、tvmc 高层 API
10. **故障排查** — 驱动占用（lsof /dev/nvidia*）、版本不匹配、libc 头文件缺失、Xorg 占用 GPU

## 相关主题链接

- [[topics/Kubernetes-编排]] — K8s GPU 调度与共享
- [[topics/Jetson-与边缘计算]] — 边缘端 GPU 推理
- [[topics/华为昇腾与国产芯片]] — 国产 AI 芯片替代方案
