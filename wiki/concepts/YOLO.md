---
title: YOLO
type: concept
tags: [yolo, object-detection, computer-vision, real-time, cnn, darknet, ultralytics, yolov3, yolov4, yolov5, yolov8, gpu-computing]
last_updated: 2026-07-21
---

# YOLO

YOLO（You Only Look Once）是单阶段（one-stage）目标检测算法的开创者和代表性系列，由 Joseph Redmon 于 2015 年首次提出。其核心思想是将目标检测视为单一的回归问题——在一次前向传播中同时预测目标的边界框坐标和类别概率，从而实现极高的推理速度。YOLO 系列从 v1 发展到 v8，经历了从学术原型到工业级工具的完整演进，已成为实时目标检测领域的事实标准。

YOLO 的革命性在于它颠覆了传统的"先定位后分类"两阶段检测范式。以 [[R-CNN]] 系列为代表的两阶段方法先生成候选区域再逐一分类，精度高但速度慢；而 YOLO 将整张图像输入网络，一次性输出所有检测目标的位置和类别，在保持可接受精度的同时实现了实时检测。YOLOv5 之后由 [[Ultralytics]] 团队接管开发，提供了极其易用的 Python API 和命令行接口，进一步推动了 YOLO 在工业界的普及。

## 核心概念

### 单阶段检测范式

YOLO 将输入图像划分为 S×S 的网格，每个网格单元负责预测以该单元为中心的多个边界框。每个边界框包含 5 个预测值：中心坐标 (x, y)、宽高 (w, h) 和置信度（confidence score），再加上各类别的条件概率。这种"一步到位"的设计使得 YOLO 只需一次前向传播即可完成检测，推理速度远超两阶段方法。在 Titan X GPU 上，YOLOv1 可达 45-155 FPS，而 YOLOv8 在保持高精度的同时仍能满足实时需求。

### 系列演进

YOLO 系列经历了多个版本的迭代，每个版本在精度和速度之间取得了不同的平衡：

- **YOLOv1-v3**（Redmon 等）：奠定基础架构，引入多尺度预测（v3）和 Darknet 骨干网络
- **YOLOv4**（Bochkovskiy 等）：引入 CSPDarknet53 骨干、PANet neck、Mosaic 数据增强等"免费午餐"（bag of freebies）技术
- **YOLOv5**（Ultralytics）：工程化程度极高，提供 n/s/m/l/x 五种规模，支持自动锚框计算、混合精度训练、多平台导出
- **YOLOv8**（Ultralytics 2023）：采用 Anchor-Free 设计、C2f 模块、解耦头（decoupled head），支持检测、分割、姿态估计、分类、跟踪五大任务
- **YOLOv9-v10**：引入 GELAN 架构、PGI（可编程梯度信息）、NMS-Free 端到端检测等前沿技术

### Anchor-Free 演进

早期 YOLO 版本（v2-v5）依赖预定义的 Anchor Box 来预测目标尺寸，需要根据数据集进行聚类分析确定最优锚框。YOLOv8 开始转向 Anchor-Free 设计，直接预测目标中心点和宽高，简化了超参数调优，提升了模型对不同尺寸目标的泛化能力。这一演进反映了目标检测领域从 Anchor-Based 到 Anchor-Free 的整体趋势。

### 多任务统一架构

YOLOv8 将目标检测、实例分割、姿态估计、图像分类和目标跟踪统一在同一框架下。用户只需切换任务模式（detect/segment/pose/classify/track），即可使用相同的 API 完成不同类型的视觉任务。这种统一架构降低了多任务系统的开发和维护成本，使 YOLO 从单一检测工具演进为通用的视觉 AI 平台。

### 工程化与部署

Ultralytics 为 YOLO 提供了极其完善的工程化支持：

- **训练**：`yolo train data=coco128.yaml model=yolov8n.pt epochs=100 imgsz=640`
- **推理**：`yolo predict source=image.jpg model=yolov8n.pt`
- **导出**：支持导出为 [[ONNX]]、TensorRT、[[OpenVINO]]、CoreML、TFLite、PaddlePaddle 等 10+ 种格式
- **多平台**：支持 CPU、GPU（CUDA）、Apple Silicon、Edge TPU 等硬件
- **数据增强**：内置 Mosaic、MixUp、HSV 调整、随机翻转等增强策略

## 技术架构

```mermaid
flowchart LR
    A[输入图像] B[Backbone 特征提取] C[Neck 特征融合] D[Head 预测输出] E[后处理/NMS] F[检测结果]
    A --> B --> C --> D --> E --> F
    G[Darknet/CSPDarknet/GELAN] --> B
    H[PA-FPN/BiFPN] --> C
    I[Anchor-Based/Anchor-Free] --> D
```

## 应用场景

- **实时视频监控**：在安防场景中对人脸、行人、车辆进行实时检测与跟踪
- **自动驾驶**：检测道路上的车辆、行人、交通标志，要求毫秒级响应
- **工业质检**：检测产品表面缺陷、尺寸偏差，配合机械臂自动分拣
- **医学影像分析**：识别 X 光、CT、病理切片中的病灶区域
- **无人机巡检**：电力线路、光伏面板、桥梁结构的缺陷检测
- **零售与物流**：货架商品识别、包裹分拣、库存盘点

## 相关技术

- [[计算机视觉与目标检测]]——YOLO 所属的计算机视觉技术体系
- [[GPU-与-CUDA-开发]]——YOLO 训练与推理的核心加速技术
- [[ONNX]]——YOLO 模型导出的标准交换格式
- [[OpenVINO]]——Intel 平台的 YOLO 推理加速工具包
- [[TensorRT]]——NVIDIA 平台的推理优化引擎

## 主要页面

- [[计算机视觉与目标检测]] - 目标检测算法体系与 YOLO 的技术定位
- [[GPU-与-CUDA-开发]] - GPU 加速计算与 YOLO 训练推理实践
