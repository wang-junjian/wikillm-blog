---
title: QLoRA
type: concept
tags: [qlora, lora, quantization, fine-tuning, peft, low-rank, memory-efficient, llm-training]
last_updated: 2026-07-21
---

# QLoRA

QLoRA（Quantized Low-Rank Adaptation）是一种将模型量化（Quantization）与低秩适应（LoRA）相结合的高效微调方法，由 Dettmers 等人于 2023 年在论文《QLoRA: Efficient Finetuning of Quantized LLMs》中提出。它能够在保持 LoRA 微调效果的同时，将预训练模型的显存占用降低至原来的 1/4 甚至更低，使得在单张消费级 GPU 上微调 65B 参数规模的大模型成为可能。

QLoRA 的核心思想是"用更少的比特存储预训练权重，同时保持可训练的参数精度"。具体而言，它将预训练模型量化为 4-bit（NF4 格式），然后在此基础上添加 LoRA 适配器进行微调。推理时，量化权重被动态反量化为 BF16 进行计算，而 LoRA 适配器始终保持 BF16 精度。

这一方法的提出极大地降低了大模型微调的硬件门槛，推动了开源社区的微调民主化。从 Llama、Mistral 到 Qwen、DeepSeek，几乎所有主流开源模型都有基于 QLoRA 的微调版本。QLoRA 也是 Hugging Face PEFT 库的核心功能之一，被广泛应用于学术研究、企业应用和个人开发中。

## 核心概念

### 4-bit 量化（NF4）

QLoRA 使用 NormalFloat4（NF4）量化格式，专为正态分布权重设计：

- **非均匀量化**：不同于传统的均匀量化（INT4），NF4 根据权重的统计分布设计量化区间，在密集区域使用更多量化级别。
- **分块量化**：每 64 个权重为一组，每组独立计算量化参数（缩放因子和零点），减少量化误差。
- **双量化（Double Quantization）**：对量化参数本身再次量化，进一步节省显存。

NF4 量化在保持模型精度方面显著优于 INT4 和 FP4，是 QLoRA 性能的关键保障。

### 分页优化器（Paged Optimizer）

微调过程中，优化器状态（如 Adam 的动量和方差）通常占用大量显存。QLoRA 引入分页优化器解决这一问题：

- **统一内存管理**：利用 NVIDIA Unified Memory 机制，在 GPU 显存不足时将优化器状态自动转移到 CPU 内存。
- **按需加载**：仅在需要计算时将对应页面加载回 GPU，类似操作系统的虚拟内存机制。
- **避免 OOM**：有效防止因显存不足导致的训练中断，使得在 24GB 显存的 RTX 3090/4090 上微调 65B 模型成为可能。

### LoRA 适配器

QLoRA 在量化模型的基础上添加 LoRA 适配器：

- **低秩分解**：将权重更新 ΔW 分解为两个低秩矩阵 A 和 B 的乘积（ΔW = BA），秩 r 通常为 8-64。
- **适配器位置**：通常应用于注意力层的 Query 和 Value 投影矩阵（q_proj、v_proj），也可扩展到所有线性层。
- **参数高效**：LoRA 参数通常仅为原模型参数的 0.1%-1%，大幅减少训练显存和计算量。
- **精度保持**：LoRA 适配器始终保持 BF16 精度，确保微调质量。

### 显存节省效果

QLoRA 相比全精度微调（FP16）的显存节省：

| 模型规模 | 全精度微调 | QLoRA 微调 | 节省比例 |
|---------|-----------|-----------|---------|
| 7B | ~40 GB | ~6 GB | ~85% |
| 13B | ~80 GB | ~10 GB | ~87% |
| 33B | ~160 GB | ~20 GB | ~87% |
| 65B | ~320 GB | ~32 GB | ~90% |

## 技术架构

```mermaid
graph LR
    subgraph 预训练模型（冻结）
        Base[BF16 预训练权重] --> Quant[4-bit NF4 量化]
        Quant --> Dequant[动态反量化到 BF16]
    end

    subgraph 可训练参数（LoRA）
        A[低秩矩阵 A<br/>BF16] --> Multiply[×]
        B[低秩矩阵 B<br/>BF16] --> Multiply
    end

    Dequant --> Add[加权求和]
    Multiply --> Add
    Add --> Output[输出]

    Optimizer[分页优化器<br/>CPU/GPU 交换] -.-> A
    Optimizer -.-> B
```

QLoRA 的计算流程：预训练权重以 4-bit 存储 → 推理时动态反量化为 BF16 → 与 LoRA 适配器的 BF16 输出相加 → 得到最终结果。优化器状态在 CPU 和 GPU 间动态交换。

## 应用场景

- **开源模型微调**：在消费级 GPU 上微调 Llama、Mistral、Qwen 等大模型，适配特定任务或领域。
- **指令微调（Instruction Tuning）**：使用指令数据集微调模型，提升遵循指令的能力。
- **领域适配**：将通用模型适配到医疗、法律、金融等垂直领域。
- **角色扮演与个性化**：微调模型以特定风格、语气或人设进行对话。
- **多语言扩展**：在单语模型基础上扩展多语言能力。

## 相关技术

- [[微调与模型训练]]
- [[LoRA]]
- [[LLM-推理优化]]
- [[Hugging-Face-生态]]

## 主要页面

- [[微调与模型训练]] - 大模型微调技术与训练范式
- [[LoRA]] - 低秩适应微调方法
