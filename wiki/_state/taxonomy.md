# 主题分类法（Taxonomy)

本分类法基于 788 篇文章、2347 个标签的聚类分析设计，共包含 32 个主题，分为 8 个领域。
每个主题列出 seed tags（种子标签)供 `tools/wikillm.py assign` 做初版归属；
种子标签不强制覆盖所有文章，LLM 会在 assign 阶段根据标题与正文做二次判定。

设计原则：
1. 主题粒度适中：每个主题预期 10–80 篇文章，避免过大或过小
2. 种子标签优先使用高频标签（频次 ≥ 10)，低频标签作为补充
3. 优先使用已有英文标签作为 seed；中文标签仅在没有对应英文时使用
4. 主题之间允许少量重叠，assign 阶段再做边界仲裁

---

## 领域 1：LLM 与生成式 AI

### LLM-推理优化
- LLM-推理优化 (seed tags: vllm, inference, quantization, kv-cache, speculative-decoding, reasoning-model, deepseek-r1, sglang, eagle3, dflash, dspark, llama.cpp, text-generation-inference, fastchat, inference-serving, inference-acceleration, vram, benchmark, performance, xinference)
- 说明：大模型推理框架、引擎、加速技术与性能优化
- 预期目标页面：LLM-推理框架（concept)、推理优化技术（concept)、推理服务部署（practice)

### RAG-检索增强生成
- RAG-检索增强生成 (seed tags: rag, embeddings, retrieval, vector-search, graphrag, ragflow, privategpt, faiss, 检索增强, knowledge-base, document-qa)
- 说明：RAG 架构、向量检索、知识库构建
- 预期目标页面：RAG-架构与实践（concept)、向量检索技术（concept)

### AI-Agent-编排
- AI-Agent-编排 (seed tags: agent, ai-agent, multi-agent, autogen, crewai, smolagents, langchain, agents-sdk, tool-use, agentic, agentic-engineering, openai-function-calling, langchain-agent, code-generation, computer-using-agent, cua, operator, ui-tars, openclaw, nanoclaw, skill, hermes, workbuddy, codebuddy, pi-agent, jiuwenswarm, a2a, agent2agent, acp, smolagents, elizaos, letta, memgpt)
- 说明：智能体框架、多智能体协作、工具调用
- 预期目标页面：AI-Agent-架构（concept)、多智能体编排（concept)、Agent-工具与协议（practice)

### MCP-协议栈
- MCP-协议栈 (seed tags: mcp, model-context-protocol, mcp-server, mcp-inspector, mcp-python-sdk, fastmcp, create-mcp-server, json-rpc, mcphub, specification)
- 说明：模型上下文协议生态，含服务端、客户端、调试工具
- 预期目标页面：MCP-协议规范（concept)、MCP-服务端开发（practice)

### LLM-编码助手
- LLM-编码助手 (seed tags: ai-coding-assistant, github-copilot, claude-code, cursor, continue, tabby, aider, pi-agent, kilocode, opencode, codegpt, code-llm, code-completion, code-generation, code-assistant, deepseek-coder, cline, copilot-chat)
- 说明：AI 驱动的编码工具与 IDE 插件
- 预期目标页面：AI-编码助手生态（concept)、Claude-Code-深度实践（practice)、Cursor-实践指南（practice)

### LLM-部署与开源生态
- LLM-部署与开源生态 (seed tags: ollama, litellm, text-generation-inference, open-webui, vllm, sglang, fastchat, xinference, siliconflow, together-ai, openai-api, openai-api-compatibility, local-llms, local-ai, model-serving)
- 说明：开源模型部署、本地 LLM 管理、API 代理
- 预期目标页面：本地-LLM-部署（practice)、LLM-API-网关（concept)

### 微调与模型训练
- 微调与模型训练 (seed tags: fine-tuning, lora, qlora, llama-factory, mlx, deeplearning-ai, p-tuning-v2, swift, modelscope, deepspeed, llm-training, text2sql)
- 说明：大语言模型微调方法、训练框架与参数高效微调
- 预期目标页面：LLM-微调技术（concept)、LoRA-与-QLoRA（practice)、主流微调框架对比（practice)

---

## 领域 2：AI 硬件与芯片加速

### GPU-与-CUDA-开发
- GPU-与-CUDA-开发 (seed tags: gpu, nvidia, cuda, nvidia-driver, cudnn, tensorrt-llm, gpu-sharing, vram, software-stack)
- 说明：NVIDIA GPU 开发、CUDA 编程、驱动与软件栈
- 预期目标页面：NVIDIA-GPU-软件栈（practice)、CUDA-编程基础（concept)

### 华为昇腾与国产芯片
- 华为昇腾与国产芯片 (seed tags: huawei-atlas, ascend-npu, npu, 昇腾, huawei, atlas, mindie, atlas-a2, atlas-900, cambrian, evalscope, 寒武纪, mxc500, hygon, dcu)
- 说明：华为昇腾（Ascend)NPU 生态、寒武纪 MLU、海光 DCU 等国产 AI 芯片
- 预期目标页面：华为昇腾-部署实战（practice)、国产-AI-芯片生态（concept)

### Jetson-与边缘计算
- Jetson-与边缘计算 (seed tags: jetson, jetson-thor, jetson-agx-orin, isaac-ros, edge, edge-ai, edge-computing, edge-hardware, nano-banana, physical-ai)
- 说明：NVIDIA Jetson 系列边缘计算平台、Isaac ROS
- 预期目标页面：Jetson-边缘部署（practice)、边缘-AI-开发（concept)

---

## 领域 3：大模型与算法研究

### 计算机视觉与目标检测
- 计算机视觉与目标检测 (seed tags: computer-vision, object-detection, yolo, yolov5, yolov8, yolov4, opencv, paddleocr, paddlepaddle, openvino, retinanet, darknet, ultralytics, roboflow, easyocr, ocr, 目标检测, deepseek-ocr)
- 说明：计算机视觉算法、目标检测模型、图像识别
- 预期目标页面：目标检测算法演进（concept)、YOLO-系列实践（practice)、OpenCV-与-OpenVINO（practice)

### 多模态大模型
- 多模态大模型 (seed tags: cogvlm2, glm-4v, qwen2.5-vl, minicpm-v, multimodal, multimodal-llm, phi-3-vision, 多模态, vision, vlm, glm-4.1v-thinking, qwen2.5-omni, janus-pro-7b, deepseek-janus)
- 说明：视觉语言模型、多模态理解与生成
- 预期目标页面：多模态大模型综述（concept)、主流-VL-模型对比（practice)

### 图像生成与扩散模型
- 图像生成与扩散模型 (seed tags: stable-diffusion, diffusion-models, text-to-image, sdxl-turbo, kolors, clip, image-generation)
- 说明：Stable Diffusion 等扩散模型、图像生成与编辑
- 预期目标页面：扩散模型原理（concept)、图像生成实践（practice)

### 语音与音频处理
- 语音与音频处理 (seed tags: whisper, speech, asr, speech-to-text, text-to-speech, vad, funasr, whisperlivekit, sensevoice, cosyvoice, simulstreaming, audio2sub, speech-llm, speech-recognition, speech-to-speech)
- 说明：语音识别、语音合成、音频处理全链路
- 预期目标页面：语音识别技术栈（concept)、Whisper-与-FunASR（practice)、语音合成与克隆（practice)

### Prompt-Engineering-与上下文工程
- Prompt-Engineering-与上下文工程 (seed tags: prompt-engineering, chain-of-thought, context-engineering, few-shot, cot, react, in-context-learning)
- 说明：提示工程方法论、上下文工程、思维链等
- 预期目标页面：Prompt-Engineering-方法论（concept)、上下文工程（concept)

---

## 领域 4：大模型生态与前沿

### 主流-LLM-与厂商
- 主流-LLM-与厂商 (seed tags: openai, anthropic, claude, deepseek, qwen, chatgpt, gemini, llama, glm, kimi, yi, spark-desk, ernie-bot, longcat-flash-thinking-2601, microsoft, copilot, copilot-studio, pangu, 混元, hunyuan)
- 说明：国内外主流大模型厂商与旗舰模型
- 预期目标页面：主流大模型对比（concept)、OpenAI-生态（practice)、Claude-与-Anthropic（practice)、DeepSeek-系列（practice)、Qwen-通义千问（practice)

### LLM-技术报告与前沿论文
- LLM-技术报告与前沿论文 (seed tags: leaderboard, benchmark, evaluation, paper, swe-bench, mhc, deep-spec, deepspec, survey, paper-interpretation, technical-report, sky-t1, model-evaluation, model-editing, model-merging, speech-llm, 2025生成式AI时代下的机器学习)
- 说明：前沿技术解读、论文精读、模型评估
- 预期目标页面：大模型评估体系（concept)、重要论文精读（source)

### 具身智能与机器人
- 具身智能与机器人 (seed tags: embodied-ai, vla, vision-language-action, lerobot, reachy-mini, robot, robotics, ros, isaac-groot-n1, 具身智能)
- 说明：具身智能、VLA 模型、机器人操作系统
- 预期目标页面：具身智能综述（concept)、VLA-模型架构（concept)、Reachy-Mini-开发实践（practice)

---

## 领域 5：工程与基础设施

### Docker-容器化
- Docker-容器化 (seed tags: docker, containers, dockerfile, harbor, docker-compose, nvidia-docker2, buildx, buildkit, container, containerization)
- 说明：容器技术、Docker 镜像、容器网络
- 预期目标页面：Docker-容器化基础（concept)、Dockerfile-最佳实践（practice)

### Kubernetes-编排
- Kubernetes-编排 (seed tags: kubernetes, kubectl, helm, minikube, kubeadm, ingress, storageclass, configmap, namespace, velero, prometheus, grafana, elasticsearch, kibana, mysql, statefulset, daemonset)
- 说明：K8s 集群管理、工作负载、存储、监控
- 预期目标页面：Kubernetes-核心概念（concept)、K8s-部署实践（practice)

### Linux-与系统管理
- Linux-与系统管理 (seed tags: linux, ubuntu, sysadmin, shell, command-line, networking, iptables, dns, ssh, ssh-keygen, lvm, nfs, cron, base64, fdisk, fstab, disks, filesystems)
- 说明：Linux 系统管理、命令行工具、网络配置
- 预期目标页面：Linux-系统管理（practice)、Shell-脚本编程（practice)、常用命令速查（practice)

### macOS-与-Apple-Silicon
- macOS-与-Apple-Silicon (seed tags: macos, apple-silicon, macbookpro, homebrew, automator, quick-actions, finder, terminal, launchd, xquartz)
- 说明：macOS 实践、Apple Silicon 适配、自动化
- 预期目标页面：macOS-开发环境（practice)、Apple-Silicon-AI-开发（practice)

### IDE-与编辑器
- IDE-与编辑器 (seed tags: vscode, vim, neovim, intellij-idea, pycharm, jetbrains, vscode-extension, jupyter, jupyterlab, remote-development, keyboard-shortcut)
- 说明：主流 IDE 与编辑器的深度使用
- 预期目标页面：VS-Code-深度实践（practice)、Vim-与终端编辑（practice)

---

## 领域 6：数据、存储与 Web

### 向量数据库与语义搜索
- 向量数据库与语义搜索 (seed tags: qdrant, faiss, fastembed, lance, vector-database, vector-search, reranker-retrieval-pipeline, sqlite, fts5)
- 说明：向量数据库技术、语义搜索、重排序
- 预期目标页面：向量数据库选型（concept)、Qdrant-与-FAISS（practice)

### 数据集、标注与模型评估
- 数据集、标注与模型评估 (seed tags: datasets, evaluation, accuracy-checker, evalscope, roboflow, ultralytics-hub, data-labeling, model-deployment)
- 说明：数据集构建、标注、模型评估方法
- 预期目标页面：数据集构建实践（practice)、模型评估方法（concept)

### Web-开发与在线工具
- Web-开发与在线工具 (seed tags: typescript, next-js, react, frontend, html, css, javascript, nodejs, web, vue, bootstrap, github-pages, vite, vercel-ai-sdk, web-scraping, browser)
- 说明：Web 前端技术栈开发与本博客在线工具
- 预期目标页面：Web-前端实践（practice)、Next.js-实践（practice)、博客在线工具集（practice)

### 网络与分布式存储
- 网络与分布式存储 (seed tags: networking, nginx, reverse-proxy, load-balancing, minio, s3, nfs, haproxy, verdaccio, ceph, glusterfs, distributed-storage)
- 说明：网络代理、负载均衡、分布式存储系统
- 预期目标页面：Nginx-与反向代理（practice)、MinIO-对象存储（practice)

---

## 领域 7：操作系统、脚本与自动化

### 浏览器扩展与桌面应用开发
- 浏览器扩展与桌面应用开发 (seed tags: chrome-extension, vscode-extension, desktop-extension, dxt, manifest-json, browser, web-extension, extension, html, javascript)
- 说明：浏览器插件、桌面扩展、VS Code 扩展开发
- 预期目标页面：浏览器扩展开发（practice)、DXT-桌面扩展（practice)

### 办公自动化与效率工具
- 办公自动化与效率工具 (seed tags: automation, office-automation, python, excel, powershell, scripting, batch-operations, shell, zsh)
- 说明：Python 办公自动化、批处理脚本、效率提升
- 预期目标页面：Python-办公自动化（practice)、Shell-脚本编程（practice)

### 物联网与嵌入式开发
- 物联网与嵌入式开发 (seed tags: iot, micropython, esp32, esp8266, raspberry-pi, openwrt, mqtt, smart-home, home-assistant, tencent-cloud, nodemcu, respeaker, neopixel)
- 说明：物联网硬件、嵌入式开发、智能家居
- 预期目标页面：IoT-开发实践（practice)、MicroPython-与-ESP32（practice)

---

## 领域 8：个人成长与跨领域

### 引用、链接与科技评论
- 引用、链接与科技评论 (seed tags: quote, link, note, andrej-karpathy, paul-graham, peter-steinberger, simon-willison, ai, generative-ai, llms, software, software-3.0, vibe-coding, agentic-engineering, tech-radar, thoughtworks, ai-weekly, ai-index-report, stanford-hai)
- 说明：科技圈引用、链接分享、AI 评论、技术雷达
- 预期目标页面：AI-技术雷达（concept)、科技圈引用集（practice)

### 个人理财与投资
- 个人理财与投资 (seed tags: investment, finance, stock, value-investing, 投资, 股票, 基金, 个人养老金, stablecoin, crypto, 加密货币, spacex, jd-health, meituan, popmart)
- 说明：个人投资分析、股票研报、理财规划
- 预期目标页面：投资分析方法（concept)、个股与行业研读（source)

### 语言学习与教育
- 语言学习与教育 (seed tags: english, vocabulary, language-learning, education, 高中英语, 课程标准, 词汇表, 输入法)
- 说明：英语学习、词汇记忆、教育工具
- 预期目标页面：英语词汇学习（practice)、高中英语词汇工具（practice)

---

## 未分类 / 边缘案例

以下标签群因文章数量过少或跨领域难以归入单一主题，暂不单独建主题：
- 健康、医疗、运动
- 摄影、视频剪辑
- 游戏开发（tank-battle, minesweeper, chinese-chess 等浏览器游戏归入 Web-开发)
- 家庭装修、汽车、旅行

assign 阶段对无法匹配上述任何主题的文章标记为 `UNASSIGNED`，由 LLM 人工仲裁。
