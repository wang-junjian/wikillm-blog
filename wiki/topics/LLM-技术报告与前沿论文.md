---
title: LLM-技术报告与前沿论文
type: topic
topic: LLM-技术报告与前沿论文
domain: 大模型生态与前沿
tags: [llm, benchmark, evaluation, reasoning, post-training, model-editing, model-merging, scaling-laws, swe-bench, cua, sky-t1, bitter-lesson]
last_updated: 2026-07-21
status: complete
---

# LLM-技术报告与前沿论文

> 领域：大模型生态与前沿
> 状态：完整

## 概述

本主题覆盖 2025–2026 年间关于大模型评估、推理优化、模型编辑与合并、以及缩放法则的核心技术报告与前沿论文，勾勒出一条从"评测驱动"到"算力驱动"的技术演进脉络。大模型研究在 2025 年前后进入深水区，四条主线交织推进：基准评估的精细化、推理效率的再思考、模型知识的微创更新、缩放法则的哲学回归。

## 核心概念页

- [[concepts/LLM-技术报告与前沿论文]]——大模型前沿研究的完整综述，涵盖 SWE-bench/CUA 基准评估、Sky-T1 推理优化、模型编辑与合并、惨痛的教训缩放法则

## 关键知识点

1. **[[SWE-bench]]**——真实软件工程试金石，从 12 个 Python 仓库筛选 2,294 个任务，考察跨文件、跨函数的仓库级补丁生成能力
2. **[[CUA-评估]]**——OpenAI 的计算机使用代理评测，覆盖 WebArena、OSWorld、WebVoyager 三个基准
3. **[[Sky-T1-32B-Flash]]**——针对推理模型"过度思考"症结，三阶段训练方案在保持准确性同时将生成长度削减最高 57%
4. **[[Sky-T1-7B]]**——SFT→RL→SFT→RL 四步训练，仅用 5K 蒸馏样本在 7B 规模上达到 SOTA 水平
5. **[[模型编辑]]（Model Editing）**——不重新训练的前提下精准植入特定事实，ROME 方法通过秩一修改实现知识植入
6. **[[模型合并]]（Model Merging）**——在参数空间中对模型进行加减运算，任务向量（Task Vector）编码微调带来的能力增量
7. **[[惨痛的教训]]（The Bitter Lesson）**——Rich Sutton 的经典论述：依托算力的通用方法最终效果远超基于人类知识的专用方法
8. **[[SimPO]]**——在 DPO 基础上引入长度归一化的隐式奖励，无需参考模型，计算开销更低
9. **[[ARC-AGI]]**——通过抽象推理任务测试模型的流体智力，剥离记忆效应测得真实推理水平
10. **[[Chatbot Arena]]**——借助 Elo 评分系统在真实用户互动中对模型进行大规模排序

## 重要来源

- CUA 评估方法与 SWE-bench 基准分析
- Sky-T1-32B-Flash 与 Sky-T1-7B 推理优化论文
- 模型编辑（ROME/Hypernetwork）与模型合并（Task Vector）综述
- 惨痛的教训（Rich Sutton）哲学反思
- 李宏毅 2025 生成式 AI 时代下的机器学习课程

## 相关主题

- [[topics/LLM-推理优化]]——推理框架、引擎与加速技术
- [[topics/微调与模型训练]]——参数高效微调与训练框架
- [[topics/AI-Agent-编排]]——智能体框架与多智能体协作
- [[topics/主流-LLM-与厂商]]——大模型竞争格局
- [[topics/数据集标注与模型评估]]——数据构建与评估实践
