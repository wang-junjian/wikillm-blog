---
title: Docker-容器化
type: practice
tags: [docker, container, kubernetes, dockerfile, registry, buildkit, devops, deployment, ai-gateway, npm-registry, verdaccio, higress, kong]
raw_sources:
  - path: raw/posts/2018/2018-12-26-container-based-load-balancing.md
    hash: "sha256:7a5a9393374cea8092af138a9188eef018881491f539f4cf33c445ad9e235b2a"
  - path: raw/posts/2019/2019-02-20-build-a-private-docker-registry.md
    hash: "sha256:ac3aeca012ec3a33dcf72272dcf3d454fe9ab81909ab7d51bf1198a71d296781"
  - path: raw/posts/2019/2019-03-05-dockerfile-jdk-mcr(matlab-compiler-runtime).md
    hash: "sha256:1243d1b1b8f2ba8214ccabe2693815e4a6d2b00f9f4262716c419625bd84e95f"
  - path: raw/posts/2020/2020-09-12-install-harbor.md
    hash: "sha256:3abd0aa595119a3cf21fd69bd01468eec1ffb3b240d1e6dad4a5d6e581c897ab"
  - path: raw/posts/2020/2020-11-05-kubernetes-cluster-joins-worker-node.md
    hash: "sha256:1eda2e7b569a0be484d6d13b3f255c5695ae42fc478bee2ae1419b56af82918f"
  - path: raw/posts/2020/2020-11-06-kubernetes-cluster-build-master-node.md
    hash: "sha256:6c404c1e0a375c405197300250647b61a1157266cb25cc9df6eab0ca3c2f2758"
  - path: raw/posts/2020/2020-12-02-download-docker-and-nvidia-docker2-offline-installation-package-on-ubuntu.md
    hash: "sha256:1d6112d58e86cfdbb91f3b16a92b4c2212cb51cf3558f5fc4e945b40824abfe9"
  - path: raw/posts/2021/2021-01-09-dockerfile-opencv4-ubuntu2004.md
    hash: "sha256:085835805ce965bcd3bbfa00d6e47ecd01b223c8e110b1902f31add7b9884d2d"
  - path: raw/posts/2021/2021-01-11-docker-practice.md
    hash: "sha256:2b05a95278f77ccb8ff74e804c1158c631bc0c8798475b4dae64a04e852cc742"
  - path: raw/posts/2021/2021-01-12-create-a-private-python-package-repository-based-on-pypiserver.md
    hash: "sha256:cdbcb1615bb372768508b9af3e09f382531ef96f4e9ac0dcd87ad67b73be76b3"
  - path: raw/posts/2021/2021-04-01-inside-the-container.md
    hash: "sha256:3338693079f3ba481d4df3db0acf0f0b20499f4bd2a7390670ec57737e1dead4"
  - path: raw/posts/2021/2021-04-16-ai-model-automatic-builder.md
    hash: "sha256:f8e3b014fd9500389f06e90705c98e359d6d776c5f4f60540bd966ad931778bd"
  - path: raw/posts/2021/2021-06-21-run-the-first-application-on-kubernetes.md
    hash: "sha256:734c934d721b2c4acaf742610719f082815ad5a609b3baa348ecd586bd8c18ff"
  - path: raw/posts/2021/2021-07-04-volume-in-kubernetes-mount-the-disk-to-the-container.md
    hash: "sha256:f8794a6aab995c4d5ab65d069f8455e42cf8a173c657484a6bb1b70044b14546"
  - path: raw/posts/2021/2021-07-05-configmap-and-secret-configure-the-application.md
    hash: "sha256:a339deac0eff902524dcf7086e5603cad0ca402ea4098b723679027bf6102b16"
  - path: raw/posts/2022/2022-02-18-execute-lua-scripts-in-openresty.md
    hash: "sha256:a327963506aff795a50ebc7135e7227c8f08010963e910e9edbc449543c9682c"
  - path: raw/posts/2022/2022-03-18-dockerfile-practice.md
    hash: "sha256:565923352bfa865dc4438027d853a307a881ed1cb9a603d9d4afa18360eb6fa3"
  - path: raw/posts/2023/2023-05-12-speed-up-docker-build-images.md
    hash: "sha256:12d74f3fab43b0f4fb75e193963140aec874eb325cd00e9a1b6cf68028002653"
  - path: raw/posts/2023/2023-05-13-build-containerize-python-application.md
    hash: "sha256:c59b04c074b213529ed2f5c6c1bfc5aca534c9c98ec6d1a7456b3dfb67c32594"
  - path: raw/posts/2023/2023-05-18-macos-docker.md
    hash: "sha256:f8fb188c7045149ad86bc7b45d4acd4218b598efdec128d6dfda6fefabe26710"
  - path: raw/posts/2023/2023-05-21-docker-building-multi-platform-images.md
    hash: "sha256:2e7b697f01cb0542209ae459353f08555e29763e5402b66e36dc7cd072c2d06b"
  - path: raw/posts/2023/2023-10-11-the-scope-of-the-arg-directive-in-dockerfile.md
    hash: "sha256:a68f3e7f1f7dc52b6a6924746cafede23404a4d9b402a5b5d3131e23da53e7a"
  - path: raw/posts/2024/2024-09-10-Higress-AI-Gateway.md
    hash: "sha256:a8abb1229d3592b01935315d2b519361f48940291f2e8e24fe6260a2a8867453"
  - path: raw/posts/2024/2024-09-11-Kong-AI-Gateway.md
    hash: "sha256:65cf88e218179606357a84ee77b5c0d137e99479e8ca55f9908b866c280592b9"
  - path: raw/posts/2025/2025-06-16-Build-a-local-npm-registry-based-on-Verdaccio.md
    hash: "sha256:bd999e251655a1c71ae69e7edd5c24e5a8a6e825467774580a3a702a70741169"
last_updated: 2026-07-21
---

# Docker-容器化

容器技术彻底改变了软件的构建、分发与运行方式。作为容器生态的事实标准，Docker 通过镜像分层、写时复制与内核级隔离机制，让开发者能够将应用连同依赖打包为轻量、可移植的单元。本页面系统梳理 Docker 容器化的完整知识体系——从底层原理到生产实践，从单机构建到 [[Kubernetes-编排|Kubernetes 集群]] 部署。

## 容器本质：一种特殊的进程

容器并非虚拟机，而是 Linux 内核能力组合出的隔离进程。理解容器需掌握三大支柱：

| 机制 | 职责 | 用户态接口 |
| --- | --- | --- |
| Linux Namespace | 视图隔离（PID、Mount、Network、UTS 等） | `unshare`、`nsenter` |
| Linux Cgroups | 资源限额（CPU、内存、I/O、网络带宽） | `/sys/fs/cgroup/*` |
| chroot / pivot_root | 根目录隔离，构建容器镜像（rootfs） | `chroot`、`pivot_root` |

### Cgroups 资源限制

Cgroups 以文件系统暴露控制接口。以 CPU 子系统为例，`cpu.cfs_period_us` 与 `cpu.cfs_quota_us` 配合，可将某进程的 CPU 带宽约束为 `quota / period`。例如 period=100ms、quota=20ms 即限制为 20% CPU。[[Docker-容器化|Docker 容器]] 的 `--cpu-period` / `--cpu-quota` 参数正是对此的封装。

### chroot 与 rootfs

`chroot` 将进程的根目录切换到指定路径，形成独立的文件系统视图。Docker 优先使用 `pivot_root`，仅在回退场景使用 chroot。容器镜像（Image）本质上就是一个 rootfs，叠加在宿主机内核之上为容器进程提供隔离执行环境。

## Docker 引擎安装与配置

### 在线安装

官方脚本一键安装：

```bash
curl -fsSL https://get.docker.com | sh -
```

### 离线安装（Ubuntu）

无网络环境下，先在与目标机器相同发行版的容器中下载 deb 包，再离线安装：

```bash
docker run -it -v `pwd`/offline:/offline ubuntu:20.04 bash
cd /offline
wget https://download.docker.com/linux/ubuntu/dists/focal/pool/stable/amd64/docker-ce_19.03.14~3-0~ubuntu-focal_amd64.deb
wget https://download.docker.com/linux/ubuntu/dists/focal/pool/stable/amd64/docker-ce-cli_19.03.14~3-0~ubuntu-focal_amd64.deb
wget https://download.docker.com/linux/ubuntu/dists/focal/pool/stable/amd64/containerd.io_1.3.9-1_amd64.deb
```

### NVIDIA GPU 支持（nvidia-docker2）

AI 训练与推理场景依赖 GPU 透传。离线安装需额外下载 `nvidia-docker2` 及其依赖：

```bash
apt download libcap2 libnvidia-container-tools libnvidia-container1 \
  nvidia-container-runtime nvidia-container-toolkit nvidia-docker2
```

运行时通过 `NVIDIA_VISIBLE_DEVICES` 环境变量指定可见 GPU，实现多卡隔离（详见 [[GPU-与-CUDA-开发|GPU 开发]]）。

### 镜像源加速

在 `~/.docker/daemon.json`（Linux）或 Docker Desktop Engine 配置（macOS）中设置 `registry-mirrors`：

```json
{
  "registry-mirrors": [
    "https://75oltije.mirror.aliyuncs.com",
    "http://hub-mirror.c.163.com",
    "https://docker.mirrors.ustc.edu.cn"
  ]
}
```

## 镜像与仓库管理

### 私有 Registry

使用官方 `registry:2` 镜像快速搭建私有仓库：

```bash
docker run -d -p 5000:5000 -v /home/ailab/docker-registry:/var/lib/registry \
  --restart=always --name docker-registry registry:2
```

客户端需配置 `insecure-registries` 以支持 HTTP 访问。为仓库搭配 Frontend（如 `docker-registry-frontend` 或 `docker-registry-web`）可提供 Web UI 浏览镜像。

### Harbor：企业级镜像仓库

[[Docker-容器化|Harbor]] 在 Registry 基础上增加 RBAC、漏洞扫描、镜像签名与垃圾回收等能力。部署流程包括：

1. 下载离线安装包（`harbor-offline-installer-vX.X.X.tgz`）
2. 生成 CA 证书与服务器证书（OpenSSL）
3. 编辑 `harbor.yml` 配置 hostname、证书路径、admin 密码
4. 执行 `./prepare` 与 `./install.sh`

Harbor 强制 HTTPS 访问，证书需同时部署到 `/etc/docker/certs.d/<hostname>/` 供 Docker 客户端信任。

### PyPI 私有仓库

除镜像仓库外，Python 生态同样需要私有包管理。[[Docker-容器化|PyPIServer]] 容器化部署后，客户端通过 `pip.conf` 配置 `index-url` 指向私有源，结合 `htpasswd` 实现上传鉴权，适用于内网加速与自建包分发。

## Dockerfile 编写实践

Dockerfile 定义镜像构建流程，掌握其指令与优化技巧是容器化的核心能力。

### 基础指令

| 指令 | 作用 |
| --- | --- |
| `FROM` | 指定基础镜像 |
| `RUN` | 执行命令并提交为新层 |
| `COPY` / `ADD` | 复制文件到镜像 |
| `ENV` | 设置环境变量 |
| `ARG` | 构建时参数 |
| `ENTRYPOINT` | 容器启动命令 |
| `CMD` | 默认参数（可被 `docker run` 覆盖） |
| `WORKDIR` | 设置工作目录 |

### ARG 作用范围

`ARG` 的作用域极易混淆：

- **FROM 之前定义**：仅在 FROM 指令中可用，跨阶段有效。
- **FROM 之后定义**：仅作用于当前 Stage，跨 Stage 需重新声明。

```dockerfile
ARG BASE_IMAGE=python:3.10.9
FROM ${BASE_IMAGE} AS builder
# 此处 ${BASE_IMAGE} 可用，其他 ARG 未定义

FROM ${BASE_IMAGE}
ARG APP_HOME=/app       # 必须重新声明
WORKDIR ${APP_HOME}
```

### 多阶段构建

多阶段构建（Multi-stage Build）将编译环境与运行环境分离，显著缩小最终镜像体积：

```dockerfile
FROM python:3.10 AS builder
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.10-slim
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY . /app
CMD ["python", "main.py"]
```

以 Ultralytics Serving 为例，从 `python:3.10`（861MB）切换到 `python:3.10-slim`（114MB），应用镜像从 1.93GB 降至 1.18GB。

### 缓存加速构建

[[BuildKit]] 的 `RUN --mount=type=cache` 将宿主机目录挂载为构建缓存，跨构建保留 pip、apt、Go 等下载缓存：

```dockerfile
FROM python:3.10
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt
```

apt 缓存同理：

```dockerfile
RUN rm -f /etc/apt/apt.conf.d/docker-clean
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    apt update && apt-get install -y libgl1-mesa-glx
```

配合 `--no-cache-dir`（pip）与 `--no-install-recommends`（apt）进一步压缩镜像。实验表明 `pip install --no-cache-dir` 可避免将下载包缓存到镜像层，减少约 200MB 体积。

### 依赖分层优化

代码变动频率远高于依赖。将 `COPY requirements.txt` 与 `RUN pip install` 置于 `COPY . /app` 之前，可充分利用层缓存——仅当 `requirements.txt` 变化时才重装依赖，日常代码修改只需复制应用层。

## 容器运行与管理

### 重启策略

| 策略 | 行为 |
| --- | --- |
| `no` | 默认，不自动重启 |
| `on-failure` | 非零退出码时重启 |
| `always` | 总是重启（手动停止后仅 Docker 重启时生效） |
| `unless-stopped` | 总是重启，除非手动停止 |

启动后可通过 `docker update --restart=always <container>` 动态更新。

### GPU 隔离

```bash
docker run --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=0,1 gouchicao/yolov5:train
```

`NVIDIA_VISIBLE_DEVICES` 默认值为 `all`，指定序号实现多卡分配。

### 容器清理

```bash
# 删除 dangling 镜像
docker rmi --force $(docker images -q --filter "dangling=true")
# 删除 Exited 容器
docker rm -f $(docker ps -qa --filter status=exited)
# 按名称模式删除
docker rm -f $(docker ps -a | grep face-service- | awk '{print $1}')
```

### 镜像归档迁移

```bash
docker save -o name.tar name:tag    # 导出
docker load -i name.tar             # 导入
```

## 数据持久化：卷与挂载

容器内数据随容器删除而丢失。Kubernetes 提供多种卷类型应对不同场景：

| 卷类型 | 生命周期 | 典型用途 |
| --- | --- | --- |
| `emptyDir` | 与 Pod 绑定 | 容器间临时共享、缓存 |
| `hostPath` | 节点级 | 访问节点日志、设备插件 |
| `NFS` | 持久化 | 多 Pod 共享持久数据 |
| `configMap` | 配置 | 暴露配置文件 |
| `secret` | 敏感配置 | 证书、密钥（内存存储） |

`emptyDir` 可设置 `medium: Memory` 使用 tmpfs，适用于高频写入的临时数据。`hostPath` 常用于 DaemonSet 访问节点资源（如 NVIDIA 设备插件挂载 `/var/lib/kubelet/device-plugins`）。

## Kubernetes 编排

当容器数量增长，[[Kubernetes-编排|Kubernetes]] 负责调度、伸缩与自愈。

### 集群搭建

kubeadm 是官方推荐的集群部署工具。Master 节点初始化流程：

1. 安装 `kubelet`、`kubeadm`、`kubectl`（版本严格一致，如 1.18.3-00）
2. 预拉取控制面镜像（kube-apiserver、etcd、coredns 等）
3. `kubeadm init` 生成 join 命令
4. 安装 Pod 网络插件（如 Weave Net）
5. Worker 节点执行 `kubeadm join` 加入集群

> 注意：Docker 默认 cgroup driver 为 `cgroupfs`，而 Kubernetes 推荐 `systemd`，生产环境需对齐以避免不稳定。

### 应用部署

Kubernetes 通过 Deployment 管理 Pod 副本，Service 暴露访问入口。NodePort 类型 Service 将容器端口映射到节点端口（30000-32767），便于集群外访问：

```yaml
apiVersion: v1
kind: Service
metadata:
  name: kubia
spec:
  type: NodePort
  ports:
  - port: 8080
    targetPort: 8080
    nodePort: 30088
  selector:
    app: kubia
```

### 配置管理：ConfigMap 与 Secret

硬编码配置导致不同环境需定义不同 Pod。ConfigMap 将配置解耦为独立资源，支持三种注入方式：

1. **环境变量**：`env.valueFrom.configMapKeyRef` 逐项注入，或 `envFrom.configMapRef` 批量注入。
2. **卷文件**：ConfigMap 条目暴露为文件挂载到容器，应用按文件路径读取。
3. **命令行参数**：通过 `args` 引用。

ConfigMap 卷支持热更新——修改 ConfigMap 后，kubelet 同步更新卷内文件（通过符号链接切换实现）。但应用需自行重载配置（如 `nginx -s reload`），且使用 `subPath` 挂载的条目不会自动更新。

Secret 以 Base64 编码存储敏感数据（证书、密钥），挂载到容器后自动解码为明文文件。Secret 卷默认使用 tmpfs（内存），不会落盘。包含敏感数据的配置文件应整体存入 Secret 而非 ConfigMap。

镜像拉取鉴权通过 `imagePullSecrets` 配置：

```yaml
spec:
  imagePullSecrets:
  - name: mydockerhubsecret
```

## 多平台构建

Apple Silicon（arm64）与服务器（amd64）的架构差异要求镜像支持多平台。Docker Buildx 是扩展的构建工具，基于 [[BuildKit]] 实现交叉编译构建。

### 构建器管理

```bash
docker buildx create --name mybuilder --driver docker-container --bootstrap --use
docker buildx inspect mybuilder
```

默认 `docker` 驱动不支持多平台，需切换到 `docker-container` 驱动。

### 构建与推送

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t user/image:latest --push .
```

多平台镜像必须推送到仓库（Docker Hub 或私有 Registry），本地不支持存储多架构清单。`--push` 会生成 manifest list 并推送所有架构镜像。`docker buildx imagetools inspect` 可查看多平台清单详情。

### QEMU 模拟

通过 `tonistiigi/binfmt` 安装 QEMU 模拟器，使 arm64 主机能构建 amd64 镜像：

```bash
docker run --privileged --rm tonistiigi/binfmt --install linux/arm64,linux/amd64
```

## 实战案例

### AI 模型打包发布

结合 Dockerfile 与 shell 脚本，实现模型（ONNX）与配置的自动打包、压缩、上传至模型服务器。通过 `ssh-keygen` 生成密钥对，`scp` 免密传输。Dockerfile 多阶段构建确保发布镜像最小化。

### Python 应用容器化（FastAPI + Gunicorn）

基于 `python:3.10-slim` 构建推理服务镜像。Gunicorn 心跳系统依赖 `/tmp` 目录，容器默认不使用 tmpfs 会导致心跳阻塞，通过 `--worker-tmp-dir /dev/shm` 将心跳目录挂载到共享内存解决。

### OpenResty 内嵌 Lua 脚本

OpenResty 将 LuaJIT 嵌入 NGINX，在请求处理阶段执行 Lua 逻辑。容器化部署时，通过卷挂载 `nginx.conf` 实现配置热更新。`set_by_lua_block` 用于动态计算变量（如根据 URL 重写 Host），`content_by_lua_block` 用于生成响应内容。

### OpenCV 镜像构建

构建 OpenCV 镜像时常见三类问题：
- `libGL.so.1` 缺失 → 安装 `libgl1-mesa-glx`
- `libgthread-2.0.so.0` 缺失 → 安装 `libglib2.0-dev`
- tzdata 安装交互阻塞 → 设置 `ENV DEBIAN_FRONTEND=noninteractive`

### AI 网关容器化部署

AI 网关负责统一管理 [[大模型服务|大模型]] 流量，实现多模型路由、负载均衡与安全治理。Higress 与 Kong 是两款主流的 AI 网关方案，均支持 Docker 快速部署。两者的架构差异反映不同的设计权衡（Trade-off）：Higress 采用单镜像 all-in-one 模式，简化部署；Kong 依赖外部数据库，换取更强的插件生态与企业级治理能力。

#### Higress：基于 Envoy 的云原生网关

Higress 基于阿里内部多年的 Envoy Gateway 实践沉淀，以开源 Istio 与 Envoy 为核心构建。其 all-in-one 镜像将网关、控制台与数据面集成在单一容器中，适合快速体验与中小规模部署。作为 [[云原生]] 网关的代表，Higress 天然适配 [[Kubernetes-编排|Kubernetes]] 生态。

```bash
docker run -d --rm --name higress-ai -v ${PWD}:/data \
    -p 8001:8001 -p 8080:8080 -p 8443:8443 \
    higress-registry.cn-hangzhou.cr.aliyuncs.com/higress/all-in-one:latest
```

端口分配：
- `8001`：Higress UI 控制台
- `8080`：网关 HTTP 入口
- `8443`：网关 HTTPS 入口

配置流程包括创建服务来源、路由规则与 AI 代理插件。AI 代理插件支持 `modelMapping` 将请求映射到不同模型（如 Qwen2-7B），实现多模型统一入口。Higress 的 AI 代理基于 [[WebAssembly|Wasm]] 插件架构，支持自定义扩展。

#### Kong：企业级 AI 网关

Kong AI Gateway 提供语义缓存、语义路由、提示模板等高级能力。与 Higress 不同，Kong 依赖 PostgreSQL 存储配置数据，部署时需先启动数据库容器并执行迁移。这种架构使 Kong 更适合需要 [[可观测性]] 与 [[流量治理]] 的企业级场景。

Kong 的 AI 插件生态更为丰富，包括 AI Proxy、AI Request/Response Transformer、AI Semantic Cache 等。AI Proxy 插件负责将请求转换并代理到多个 AI 提供者与模型。

两者的权衡（Trade-off）：
- Higress 部署更简单（单镜像），适合云原生场景
- Kong 功能更丰富，适合需要高级流量治理的企业

### Verdaccio：内网 npm 仓库

Verdaccio 是基于 Node.js 的轻量级私有 npm 仓库，适用于内网环境下的包管理与加速。与 [[Docker-容器化|Docker 镜像仓库]] 类似，Verdaccio 通过容器化部署实现快速搭建与迁移。

#### 部署方式

Docker Compose 是推荐的部署方式，通过卷挂载实现配置、存储与插件的持久化：

```yaml
version: '3.8'
services:
  verdaccio:
    image: verdaccio/verdaccio
    container_name: 'verdaccio'
    ports:
      - '4873:4873'
    volumes:
      - './verdaccio/storage:/verdaccio/storage'
      - './verdaccio/conf:/verdaccio/conf'
      - './verdaccio/plugins:/verdaccio/plugins'
```

#### 核心配置

配置文件 `config.yaml` 定义了四大核心模块：

1. **存储**：`storage` 指定包存储路径，`plugins` 指定插件目录
2. **认证**：`auth.htpasswd` 配置用户文件，支持 bcrypt 等哈希算法
3. **上行链路**：`uplinks.npmjs` 指向官方 registry，作为上游代理
4. **包权限**：`packages` 定义访问控制规则，`$all`、`$anonymous`、`$authenticated` 分别对应不同权限级别

`proxy: npmjs` 配置启用自动缓存——当本地不存在某包时，Verdaccio 自动从上游拉取并缓存，后续请求直接命中本地。这种机制与 [[Docker-容器化|Docker 镜像仓库]] 的代理缓存原理一致，都是通过本地缓存加速重复请求。

#### 使用流程

```bash
# 创建用户（自动登录）
npm adduser --registry http://localhost:4873

# 发布包
npm publish --registry http://localhost:4873

# 安装包（自动缓存）
npm install <package> --registry http://localhost:4873

# 设置默认源
npm config set registry http://localhost:4873
```

注意：npm 本地缓存可能导致 Verdaccio 无法记录下载。使用 `npm cache clean --force` 清除缓存后，可确保请求真正经过仓库。

## 故障排查

### macOS Docker Desktop 无法启动

症状：构建时报 `no space left on device`，Docker 无法启动。

根因：Docker.raw 虚拟磁盘膨胀至 60GB，而垃圾回收阈值设为 100GB，导致磁盘已满但 GC 未触发。

解决：彻底删除 Docker 相关目录（`~/Library/Containers/com.docker.docker`、`~/Library/Application Support/Docker Desktop`），重新安装后调整 Virtual disk limit 与 GC 阈值（`defaultKeepStorage: 20GB`）。

诊断工具：

```bash
/Applications/Docker.app/Contents/MacOS/com.docker.diagnose check
```

### 常见运行时问题

- **cgroup driver 不匹配**：Docker 使用 `cgroupfs`，Kubernetes 推荐 `systemd`，需在 `/etc/docker/daemon.json` 中配置 `"exec-opts": ["native.cgroupdriver=systemd"]`。
- **CNI 未初始化**：Worker 节点加入后状态为 NotReady，需确认 Pod 网络插件已部署。
- **ConfigMap 引用缺失**：Pod 调度报 `configMap "xxx" not found`，可设置 `configMapKeyRef.optional: true` 允许引用不存在。
