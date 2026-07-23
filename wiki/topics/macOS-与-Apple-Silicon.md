---
title: macOS-与-Apple-Silicon
type: topic
topic: macOS-与-Apple-Silicon
domain: 工程与基础设施
tags: [macos, apple-silicon, homebrew, automator, m2-max, machine-learning, llm, computer-vision, docker, ffmpeg, imagemagick, openvino, pytorch, tensorflow, yolov8, whisper, llama, launchd, metal, mps]
last_updated: 2026-07-21
status: complete
---

# macOS 与 Apple Silicon

> 领域：工程与基础设施

## 概述

本主题沉淀作者在 macOS 平台上长达八年的技术实践（2018–2026），覆盖系统操作、包管理、Apple Silicon 转型适配、机器学习框架部署、本地大模型推理、计算机视觉项目实战、Automator 快捷操作批量自动化，以及图像/音视频处理的批量工具链。

Apple Silicon 转型是整个实践体系的分水岭。M2 Max 等芯片带来了统一内存架构与 Metal GPU 加速能力，使 macOS 从"开发调试机"进化为"可运行大模型的边缘推理平台"。TensorFlow 的 Metal 插件与 PyTorch 的 MPS 后端构成两大主流框架的 GPU 加速方案；llama.cpp 的 NEON + Metal 路径让 LLaMA 7B/13B 本地推理成为可能；whisper.cpp 以 6 倍于 OpenAI Whisper 的速度实现离线语音识别。

## 实践页链接

- [[practices/macOS-与-Apple-Silicon]] — macOS 与 Apple Silicon 完整实践手册（34 篇文章，2018–2026）

## 关键知识点

1. **系统基础** — 快捷键/window 管理、launchd 后台服务（Daemon/Agent 区别、plist 路径）、登录项清理、权限管理
2. **Homebrew 包管理** — brew/brew cask、镜像源配置（清华/阿里云）、自动更新卡死处理、Portable Ruby 修复
3. **Apple Silicon 适配** — Rosetta 2 转译层、arm64/x86 双架构兼容、M2 Max 开发环境搭建（Miniconda + Docker Desktop）
4. **ML 框架加速** — TensorFlow Metal 插件（tensorflow-metal）、PyTorch MPS 后端（`torch.device("mps")`）、OpenVINO 源码编译
5. **本地 LLM 推理** — llama.cpp（GGUF 格式、4-bit 量化、NEON/MPS 加速）、llama-cpp-python Metal 后端、OpenAI 兼容 REST API
6. **语音识别** — OpenAI Whisper vs whisper.cpp 对比（速度 6 倍、内存 50-60%）、FFmpeg 音频预处理
7. **计算机视觉** — Ultralytics YOLOv8（训练/评估/多格式导出）、Roboflow/Ultralytics Hub 数据管理、FastAPI + ONNXRuntime 推理服务
8. **OpenVINO 推理** — 五步工作流、IR 格式、同步/异步推理、benchmark_app 性能分析、DL Workbench 可视化
9. **Automator 自动化** — Shell 脚本兼容双架构、PNG 转 JPG/PDF2JPG/图像拼接/图像转 WebP、反向选择（AppleScript）
10. **音视频处理** — FFmpeg VideoToolbox 硬编码（CPU 33% vs 软编码 1080%）、GIF 合成、N 倍速快进、ImageMagick 批量处理

## 相关主题链接

- [[topics/Docker-容器化]] — macOS Docker Desktop 实践
- [[topics/计算机视觉与目标检测]] — YOLOv8 目标检测实战
- [[topics/语音与音频处理]] — Whisper 语音识别实践
