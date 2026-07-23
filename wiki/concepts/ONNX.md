---
title: ONNX
type: concept
tags: [onnx, open-neural-network-exchange, model-format, inference, interoperability, onnx-runtime, openvino, tensorrt, model-conversion, deep-learning]
last_updated: 2026-07-21
---

# ONNX

ONNX（Open Neural Network Exchange，开放神经网络交换格式）是由 [[Microsoft]] 和 [[Facebook]]（现 Meta）于 2017 年联合推出的开放标准，用于表示深度学习模型。其核心目标是打破 AI 框架之间的壁垒——让在 [[PyTorch]]、[[TensorFlow]]、[[MXNet]] 等框架中训练的模型能够无缝转换并在不同的推理引擎上运行。ONNX 目前已由 Linux 基金会旗下的 AI & Data 基金会（LF AI & Data）托管，拥有包括微软、Meta、Amazon、Intel、NVIDIA、华为等众多厂商参与的活跃社区。

在 AI 模型的开发生命周期中，训练和推理往往发生在不同的环境中。训练通常使用 PyTorch 或 TensorFlow 等灵活的研究框架，而推理部署则需要高性能的专用引擎（如 [[TensorRT]]、[[OpenVINO]]、[[ONNX Runtime]]）。ONNX 作为"中间表示"（Intermediate Representation, IR）层，充当训练框架和推理引擎之间的桥梁，实现了"一次训练，随处部署"的愿景。

## 核心概念

### 计算图表示

ONNX 使用基于 protobuf 的序列化格式来表示深度学习模型。每个 ONNX 模型本质上是一个计算图（Computational Graph），其中：

- **节点（Node）**：代表一个运算操作（如 Conv、MatMul、Relu、Softmax），每个节点有输入和输出
- **边（Edge）**：代表张量（Tensor），连接不同节点的输出和输入
- **初始化器（Initializer）**：存储模型的权重和偏置等常量参数
- **输入/输出（Input/Output）**：定义模型的外部接口

这种图表示是框架无关的——无论模型是用 PyTorch 还是 TensorFlow 训练的，导出为 ONNX 后都遵循相同的结构规范。

### 算子标准

ONNX 定义了一套标准的算子集合（Operator Schema），涵盖深度学习中常用的操作：

- **基础运算**：Add、Mul、MatMul、Conv、Gemm
- **激活函数**：Relu、Sigmoid、Tanh、GELU、SiLU
- **池化操作**：MaxPool、AveragePool、GlobalAveragePool
- **归一化**：BatchNormalization、LayerNormalization、GroupNormalization
- **形状操作**：Reshape、Transpose、Concat、Split、Slice
- **注意力机制**：Attention、MultiHeadAttention
- **控制流**：If、Loop、Scan（支持动态控制流）

ONNX 通过 Opset（Operator Set）版本管理算子集，每个 ONNX 版本定义了一组算子的行为规范。截至 2024 年，ONNX 已发布到 Opset 21，涵盖 200+ 个算子。

### ONNX Runtime

[[ONNX Runtime]]（ORT）是微软开发的高性能推理引擎，支持 ONNX 模型的跨平台执行。ORT 的核心特性包括：

- **执行提供者（Execution Provider）**：支持 CPU、CUDA、TensorRT、[[OpenVINO]]、DirectML、CoreML 等多种硬件后端
- **图优化**：常量折叠、算子融合、布局优化等
- **量化支持**：支持 INT8/UINT8 量化推理，降低推理延迟
- **跨平台**：Windows、Linux、macOS、Android、iOS
- **多语言 API**：Python、C/C++、C#、Java、JavaScript

ONNX Runtime 已成为 ONNX 生态中最主流的推理引擎，被广泛应用于生产环境。

### 模型转换生态

ONNX 的核心价值在于模型转换能力，主要转换工具包括：

- **torch.onnx.export**：PyTorch 内置的 ONNX 导出功能
- **tf2onnx**：TensorFlow 模型转 ONNX
- **onnxsim（ONNX Simplifier）**：简化 ONNX 计算图，消除冗余算子
- **onnx-tensorrt**：将 ONNX 模型转换为 TensorRT 引擎

转换过程中常见的挑战包括：PyTorch 算子到 ONNX 算子的映射不完全、动态形状支持有限、自定义算子的处理等。onnxsim 通过常量折叠和图变换进一步优化转换后的模型。

### 与 OpenVINO 的关系

[[OpenVINO]] 是 Intel 开发的推理优化工具包，对 ONNX 模型提供原生支持。OpenVINO 可以直接加载 ONNX 模型，并针对 Intel CPU、集成显卡、VPU 等硬件进行优化：

- **模型优化器（MO）**：将 ONNX 模型转换为 IR（Intermediate Representation）格式
- **推理引擎（IE）**：在目标硬件上执行优化后的模型
- **自动设备检测**：自动选择最佳执行设备

这种兼容性使得 ONNX 成为 Intel 平台上部署模型的标准入口格式。

## 技术架构

```mermaid
flowchart LR
    A[PyTorch 模型] B[TensorFlow 模型] C[其他框架] D[ONNX 导出] E[ONNX 模型] F[ONNX Simplifier]
    A --> D
    B --> D
    C --> D
    D --> E --> F
    F --> G[ONNX Runtime]
    F --> H[TensorRT]
    F --> I[OpenVINO]
    F --> J[其他推理引擎]
```

## 应用场景

- **跨框架部署**：将 PyTorch 训练的模型部署到 TensorRT、OpenVINO 等推理引擎
- **边缘设备推理**：在移动端（CoreML）、嵌入式（ONNX Runtime Mobile）等设备上运行模型
- **浏览器推理**：通过 ONNX Runtime Web 在浏览器中运行 AI 模型
- **模型优化与压缩**：通过 ONNX Simplifier 和量化工具减小模型体积
- **异构计算**：同一模型在不同硬件上选择最优执行后端
- **模型交换与合作**：团队间使用统一格式共享和复现模型

## 相关技术

- [[计算机视觉与目标检测]]——ONNX 在视觉模型部署中的核心应用
- [[LLM-推理优化]]——ONNX Runtime 在 LLM 推理中的应用
- [[OpenVINO]]——Intel 平台的 ONNX 推理优化工具包
- [[TensorRT]]——NVIDIA 平台的推理优化引擎
- [[ONNX Runtime]]——微软的跨平台 ONNX 推理引擎

## 主要页面

- [[计算机视觉与目标检测]] - ONNX 在视觉模型部署中的实践
- [[LLM-推理优化]] - ONNX Runtime 在 LLM 推理中的应用
