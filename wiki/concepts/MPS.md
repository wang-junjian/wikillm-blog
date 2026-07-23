---
title: MPS
type: concept
tags: [mps, metal, apple-silicon, gpu-computing, machine-learning, tensorflow, pytorch, 苹果芯片, GPU计算, 机器学习加速]
last_updated: 2026-07-21
---

# Apple Metal Performance Shaders（MPS）

Metal Performance Shaders（MPS）是 Apple 为其平台（macOS、iOS、iPadOS、tvOS）提供的 GPU 计算和图形渲染框架。MPS 提供了一套高度优化的图像处理、机器学习和数学计算内核，让开发者能够充分利用 Apple Silicon 芯片的统一内存架构和 GPU 计算能力。在 AI 和机器学习领域，MPS 是 macOS 平台上 TensorFlow 和 PyTorch 的 GPU 加速后端，使 Mac 从"开发调试机"进化为"可运行大模型的边缘推理平台"。

Apple Silicon（M1/M2/M3/M4 系列芯片）采用统一内存架构（Unified Memory Architecture, UMA），CPU 和 GPU 共享同一块物理内存，消除了传统独立 GPU 架构中 CPU-GPU 数据拷贝的开销。MPS 充分利用这一架构特性，为机器学习推理和训练提供了高效的 GPU 加速能力。

## 核心功能

**图像处理**是 MPS 最基础的能力。MPS 提供了大量预优化的图像处理内核：卷积、池化、归一化、图像缩放、色彩空间转换、直方图均衡等。这些内核针对 Apple GPU 的 Tile-based 延迟渲染架构深度优化，执行效率远超手写 Metal Shader。

**神经网络推理**是 MPS 在 AI 领域的核心应用。MPS Graph API 支持构建和执行神经网络图，涵盖卷积网络（CNN）、循环网络（RNN）、Transformer 等主流架构。MPS 自动进行算子融合（Operator Fusion）、内存优化和精度调整，在 Apple GPU 上实现高效推理。

**矩阵运算**是 MPS 的底层能力。MPSMatrixMultiplication、MPSMatrixSum 等原语为机器学习计算提供高性能的矩阵运算基础。这些原语针对 Apple GPU 的并行计算单元优化，支持 FP32、FP16 和 INT8 精度。

**光线追踪**是 MPS 在图形渲染领域的能力。MPSRayIntersector 提供硬件加速的光线追踪计算，支持实时渲染和物理仿真。

## 在 ML 中的应用

**TensorFlow Metal 插件**让 TensorFlow 在 macOS 上使用 Apple GPU 加速。通过 `tensorflow-metal` 包，TensorFlow 的计算图自动调度到 MPS 后端执行，训练速度相比 CPU 提升数倍。Metal 插件支持大多数 TensorFlow 操作，但部分高级操作可能回退到 CPU 执行。

**PyTorch MPS 后端**让 PyTorch 在 macOS 上利用 Apple GPU。通过 `torch.device("mps")` 将张量和模型移动到 MPS 设备，即可使用 Apple GPU 进行训练和推理。PyTorch 的 MPS 后端持续完善中，已支持大多数常用操作。MPS 后端特别适合：本地模型微调（Fine-tuning）、中小规模模型推理、计算机视觉任务、原型验证和教学。

**MLX 框架**是 Apple 专为 Apple Silicon 设计的机器学习框架。MLX 采用延迟计算（Lazy Computation）和统一内存设计理念，API 风格类似 NumPy 和 PyTorch。MLX 底层使用 Metal GPU 计算，支持统一内存模型下的 CPU/GPU 无缝切换。MLX 已成为 macOS 上 LLM 推理的首选框架之一。

## 与 CUDA 对比

| 维度 | CUDA (NVIDIA) | MPS (Apple) |
|------|---------------|-------------|
| 生态成熟度 | 最成熟，20+ 年历史 | 较新，持续完善中 |
| 硬件范围 | NVIDIA GPU 专用 | Apple 全平台统一 |
| 内存架构 | CPU-GPU 分离内存 | 统一内存架构 |
| 编程模型 | CUDA C/C++ / Python | Metal Shader / Swift / Python |
| 分布式训练 | 成熟（NCCL） | 有限（MPSG） |
| 适用场景 | 大规模训练和推理 | 中小规模推理和训练 |

MPS 的优势在于统一内存架构带来的零拷贝特性，以及 Apple 生态的垂直整合。CUDA 的优势在于更成熟的生态、更广泛的硬件支持和更完善的分布式训练能力。对于个人开发者和小型团队，MPS 提供了零额外成本的 GPU 加速方案。

## 应用场景

MPS 在 macOS 平台上支撑了丰富的 AI 应用：**本地 LLM 推理**（通过 MLX、llama.cpp 的 Metal 后端）、**图像生成**（Stable Diffusion 的 MPS 加速）、**视频处理**（FFmpeg VideoToolbox 硬编码）、**计算机视觉**（YOLO 目标检测、图像分割）、**语音识别**（whisper.cpp 的 Metal 加速）、**模型微调**（LoRA 微调中小模型）。

## 相关概念

- [[macOS-与-Apple-Silicon]] — Apple Silicon 平台与 ML 加速生态
- [[LLM-推理优化]] — 本地 LLM 推理的 MPS 加速路径
- [[MLX]] — Apple 原生机器学习框架
- [[GPU-与-CUDA-开发]] — NVIDIA GPU 计算生态对比

## 主要页面

- [[topics/macOS-与-Apple-Silicon]] — Apple Silicon 平台上的 ML 加速实践
- [[topics/LLM-推理优化]] — MPS 在 LLM 推理中的应用
- [[topics/GPU-与-CUDA-开发]] — GPU 计算生态全景
