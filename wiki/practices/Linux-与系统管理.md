---
title: Linux 与系统管理
type: practice
tags: [linux, ubuntu, sysadmin, ssh, networking, command-line, storage, mirror, docker, kubernetes, shell, performance, openvino, edge-computing, model-optimization, fastapi, nvidia]
raw_sources:
  - path: raw/posts/2018/2018-12-26-open-ssh-service.md
    hash: "sha256:6f759cfd8af3b053da8d7f60e660d65d450908a7e4c7db21cb3d9b125c11854b"
  - path: raw/posts/2018/2018-12-26-mac-remote-connect-ubuntu-desktop.md
    hash: "sha256:140e05db1a4b3791d6122039563342d5ca09a05b3c5f2b0a767df6a08d84b81e"
  - path: raw/posts/2019/2019-04-12-linux-system-network-configuration.md
    hash: "sha256:591593a63cbbd9c830eb15fd9bcfab5a370cd5761a24893e8c02f5bb06e3397e"
  - path: raw/posts/2019/2019-05-19-install-input-method-on-linux.md
    hash: "sha256:6f9512f7be0661a71dcb034e1b0211a0806208f78efa43361599d1f669e0d106"
  - path: raw/posts/2020/2020-06-13-ssh-login-with-key.md
    hash: "sha256:84ba9ec8dadc31a5ce1c320e58e600b22b26d4c8394cae6decc159fcb3773fb5"
  - path: raw/posts/2020/2020-06-14-linux-set-time-zone.md
    hash: "sha256:9ff9150b64089c45e167c8c0f34d10ba8a3b09c9ff589be5302f66b2dd1e9586"
  - path: raw/posts/2020/2020-09-03-disk-partition-format-mount.md
    hash: "sha256:4c36fc47e5d832a18916c35619cbbc2b5cb082461a3913f54da423c906ec4481"
  - path: raw/posts/2020/2020-09-10-nfs-configuration.md
    hash: "sha256:43535722308d67a61d14b3b257611c7974ae76a64124b8573c3972325d87fe83"
  - path: raw/posts/2020/2020-10-16-create-local-ubuntu-repository.md
    hash: "sha256:8302e7199e4577f96a4784469c1e45db73f88325fcf5ae21a92c7c00ca535135"
  - path: raw/posts/2020/2020-10-17-install-docker-on-ubuntu.md
    hash: "sha256:9c7a1a4b1f79c17fa7403d56f3934637c59402f585dec814d126c7648d1642c8"
  - path: raw/posts/2020/2020-10-29-modify-user-name-on-linux-system.md
    hash: "sha256:9ac6d9ec26f07a9f1e3c2a0719e641155cf4ac2dbb61795ba7bdd80fc7c23995"
  - path: raw/posts/2020/2020-10-30-linux-system-dns-settings.md
    hash: "sha256:9a2c413165277ad0b7f21733c335c72cf43c8800373d87a8fd80d61fa1adc2dd"
  - path: raw/posts/2020/2020-10-31-disable-devices-and-files-for-paging-and-swapping.md
    hash: "sha256:c7154108aab4d164b1e69078c4cedd8fbca231aa1818dc71566186702e970167"
  - path: raw/posts/2020/2020-11-01-configure-apt-mirror-source-on-ubuntu.md
    hash: "sha256:c07c8a5a9b479d2046e0b404113059234bc22a463aca4d0f5645b06d73f249b3"
  - path: raw/posts/2020/2020-11-02-configure-docker-mirror-source.md
    hash: "sha256:d8988a0b9d068408478c4e950b010659b564f13e495615c346d2c412b358761b"
  - path: raw/posts/2020/2020-11-07-configure-kubernetes-mirror-source.md
    hash: "sha256:8e333f66b4a69dc0ba2da9488bcc1158a2140501f79eabdf77105f7260cc730e"
  - path: raw/posts/2020/2020-11-09-configure-pip-mirror-source.md
    hash: "sha256:2275ade17f8ffc509b23783481bba9c6ef977777b0b738a28a2548c3d42b26f2"
  - path: raw/posts/2020/2020-11-10-github-accelerate.md
    hash: "sha256:333ab5920fae639ea6213a84cbc1d96a6d218acfeb2c630c49caa89498bf5cca"
  - path: raw/posts/2020/2020-11-30-ssh-allows-root-login-with-password.md
    hash: "sha256:ad0dad01b67caff333ca759427f9f01d44253ddb6f037d328f3c4e56a8774f92"
  - path: raw/posts/2020/2020-12-20-command-ls.md
    hash: "sha256:f2bedade45f503c717910c77ecc2f3cd07012ffff86e9b91b2565fba0434800f"
  - path: raw/posts/2020/2020-12-21-command-wget.md
    hash: "sha256:4c7adcd314276c200bc70b453a75ccba4fec296cb516164002e1eb6ebfe16b33"
  - path: raw/posts/2020/2020-12-22-command-sed.md
    hash: "sha256:4960d339954c60db02d75d26fb65dd2364fcf2e5f559524b67c16e7d32d6cf76"
  - path: raw/posts/2020/2020-12-23-image-format-convert-and-resize.md
    hash: "sha256:7511598adbfd7f2d7b3623c31d1c8d4ca5482c262ceb4319b3314faf761c0ce34"
  - path: raw/posts/2020/2020-12-28-command-grep.md
    hash: "sha256:8cd93e556e6aa1b0b3dabea659b8bd362e089285a2c3010e9112330ea44b6176"
  - path: raw/posts/2020/2020-12-29-command-find.md
    hash: "sha256:7c3ac6e88f95afced93b6be000f05b8da11770c6e92f04167e8df534cb6b9885"
  - path: raw/posts/2021/2021-01-17-command-top.md
    hash: "sha256:a8746bd7106383d9b072cb84ed2fd37eb932b30ee33587f4741547e3f4d1e2b2"
  - path: raw/posts/2021/2021-01-18-command-du.md
    hash: "sha256:9cdb46c7c95b05b71fc73db8be76ca50a59c253a582fc72d62ad85642e333b57"
  - path: raw/posts/2021/2021-01-19-command-cp.md
    hash: "sha256:6e67668c627e899b631d032705022e74d850ee5edd64bc4f01f809fbdf71b638"
  - path: raw/posts/2021/2021-01-20-command-tar.md
    hash: "sha256:04a8f4cbde8a60579820c40c5b281e62db82a513a11ecceef2a1f7c2239974b8"
  - path: raw/posts/2021/2021-01-20-command-zip.md
    hash: "sha256:2396860b4d39a41194f2afac4a357cba29c8f38f0aae08a5278983f6cdb0977d"
  - path: raw/posts/2021/2021-01-21-command-ssh.md
    hash: "sha256:7e1bf94f9deb3d937d05ccadc5621193000aac203390663e3f5267e66e70f868"
  - path: raw/posts/2021/2021-01-22-install-ftp-server-based-on-vsftpd.md
    hash: "sha256:043dc1746f88140fb6c0874eac67cbd28b392dd6694a47ec8418472bc241c290"
  - path: raw/posts/2021/2021-01-24-extract-video-key-frames-and-save-zip-file.md
    hash: "sha256:ede867c588aaaba5a9e93b19ed3a554648e48ba5e56e8ca8f50aa317f3e87652"
  - path: raw/posts/2021/2021-01-29-linux-shell-execution-mode.md
    hash: "sha256:778b805e08409a5482ec231073413bde6cb513dd4c93fdf55333cf2e0677ffd2"
  - path: raw/posts/2021/2021-01-30-linux-shell-practice.md
    hash: "sha256:27780c20434f51eca2eb8744a20c1097a2d7c1981ec906d928ca388d03df59df"
  - path: raw/posts/2022/2022-04-04-linux-performance-optimization.md
    hash: "sha256:969c6eeca2a4f229d9fb572fc304adb90defd4b84cd539ef0e77d2cba21ae256"
  - path: raw/posts/2021/2021-01-14-command-chown.md
    hash: "sha256:bec52719e49964e7901e0ad855e2c0e94cda0d4d72e066e42f79127cddef8389"
  - path: raw/posts/2021/2021-01-15-command-ln.md
    hash: "sha256:e3450b3085282cb469ed1a9287ee9384a7bcd082716ebca7304fa36a46ee2da9"
  - path: raw/posts/2021/2021-01-16-vim-practice.md
    hash: "sha256:a8288fa39bd81745e149cf08e799c115e7676a5426cc7a9601d21a9cc4398225"
  - path: raw/posts/2021/2021-05-24-command-man-help-info.md
    hash: "sha256:51d58127139386fa0f5b2ac9642442cd1cd7b2c26873551cd53c4f25bf84d3b0"
  - path: raw/posts/2021/2021-04-06-command-yum.md
    hash: "sha256:46c2688cf8cfa09dfbe3007cd226074ecb2995931311baaf2ace09be69ed3274"
  - path: raw/posts/2021/2021-04-07-command-helm.md
    hash: "sha256:0be7c1b432bfd24587554a2cecaf10c794a257ca11f31073aa2a01e5648b57f6"
  - path: raw/posts/2021/2021-04-09-ssh-login-welcome-message.md
    hash: "sha256:feeb5f3600c50a58e2034354560974a59972f4e007dda82fb18eb3e1384b1991"
  - path: raw/posts/2021/2021-04-10-ssh-x11-forwarding.md
    hash: "sha256:5e3e1e6032014146cad9f7b63d10da2958f50d5fed4f6e545eed645b2b017189"
  - path: raw/posts/2021/2021-04-11-command-base64.md
    hash: "sha256:41e1f42b06e3d1c886092f0b49601cc124a6c7e0c3c65e653abe82e626e41711"
  - path: raw/posts/2021/2021-04-12-fritzing.md
    hash: "sha256:f65e48862a1dea2d77d0d54e8de153963139ea93d1dfd4804ab1ce9329e040a4"
  - path: raw/posts/2021/2021-04-12-thonny-python-ide.md
    hash: "sha256:13b710f90dbb7ab85d9ae1a2cc0599bcc820163dbd7e8fce5164f579d6768a8d"
  - path: raw/posts/2021/2021-04-15-ai-dataset-package-release.md
    hash: "sha256:0fd2d8265ae33c34d2d275f568373011a3ad43b7fa4cbcbcf2dde89a1396a729"
  - path: raw/posts/2021/2021-04-16-ai-model-automatic-builder.md
    hash: "sha256:f8e3b014fd9500389f06e90705c98e359d6d776c5f4f60540bd966ad931778bd"
  - path: raw/posts/2022/2022-01-12-compile-the-embedded-operating-system-of-cambrian-mlu220.md
    hash: "sha256:520c7c50b18c6ed64c9b3b2e1e3c991a6dc6b7ca0da4ca60ed6ca5ec6a322fdb"
  - path: raw/posts/2022/2022-01-13-browse-markdown-and-html-with-terminal.md
    hash: "sha256:64932d32e8e92163cd66b3b13564611e78b2e77aa3e600fb9ddb2cab85fedebf"
  - path: raw/posts/2022/2022-01-24-install-go.md
    hash: "sha256:2ba7f1e002e76cc1a0be60d6ce3ad2337695babecc8e04f3584006591735d686"
  - path: raw/posts/2022/2022-02-23-json-formatter.md
    hash: "sha256:988332085f39fef51cb17e6bb58d016e0bdcf3f1996d361f1b6f0d1ebafc356e"
  - path: raw/posts/2022/2022-03-01-minio-quickstart.md
    hash: "sha256:cae1763deb3fa1c39ff5ed3046ac5bac83ea6cf2e2d958dcfc601866398cfd9d"
  - path: raw/posts/2022/2022-03-21-http-benchmarking-tools.md
    hash: "sha256:c236f16fa0848d01275cbec9629b0385828798c06bb9d7652cd99bcd2322a14c"
  - path: raw/posts/2022/2022-03-27-alibaba-cloud-server-ecs-open-ports.md
    hash: "sha256:33aa0e6ee4794159e44f40f05124e364370be1dfc602d1d04f0a80d64b6c7463"
  - path: raw/posts/2022/2022-03-31-fastapi-benchmarking-for-upload-and-download-files.md
    hash: "sha256:7ee1a7410034f70dcf25f3ab91f1019e7bed6ade9f164eee41e2fcfd8d99b080"
  - path: raw/posts/2022/2022-03-31-install-python3.9-in-ubuntu20.04.md
    hash: "sha256:306d815013921c048f2c951044b44e5fbab29f6a7d4f37fab2838fa2f79f888d"
  - path: raw/posts/2022/2022-04-12-develop-restapi-services-with-fastapi.md
    hash: "sha256:967639e8cf08670e514a6c2017e5cccc1f123a24b0ca19c122bf5bfb0c19578e"
  - path: raw/posts/2022/2022-04-13-get-started-openvino.md
    hash: "sha256:58fd34a74a772eb17014a3a6a1feb841f1a17d715b85340d94caed7f24d5b982"
  - path: raw/posts/2022/2022-04-13-how-openvino-works.md
    hash: "sha256:5af35728ff6aa6052ebcae255385cd6d8f014113f0cf3cf8b4bdf451314219b6"
  - path: raw/posts/2022/2022-04-14-open-model-zoo.md
    hash: "sha256:838538fe15cfd095b23a26c923c8ca29555a6635fbe5418a17dbe9707cdbd563"
  - path: raw/posts/2022/2022-04-15-openvino-image-classification.md
    hash: "sha256:6190b90b8919b938f089b3823d14181916ce3fbca0f357a667f25c02215d4f4d"
  - path: raw/posts/2022/2022-04-16-openvino-object-detection.md
    hash: "sha256:64f2ba021950c9b572bed41aa8bc165f6c6141d13cd550be18c28e495741754a"
  - path: raw/posts/2022/2022-04-17-openvino-neural-network-performance-profiling.md
    hash: "sha256:ad9ab885515e6ff790a6ee95aefbe6e68a4565e7d319621a998e7888cb3a1e17"
  - path: raw/posts/2022/2022-05-01-get-started-yolov5.md
    hash: "sha256:ec96579c482dc1c6dadbf1ee4666a2b58034d1f52b821f71549ee69c7b2b0eee"
  - path: raw/posts/2022/2022-05-02-nvidia-software-stack-build.md
    hash: "sha256:0c37ac424375bccc53aae03d95b3c418ef08627f1788b6be996bebba9f450c63"
  - path: raw/posts/2022/2022-05-03-switch-nvidia-gpu-to-intel-integrated-graphics-idg-on-ubuntu.md
    hash: "sha256:00fb7f31017e638fbfbe8c9274744cbf52479c17132241b9069e890013f9d96d"
  - path: raw/posts/2022/2022-06-07-fusing-convolution-and-batch-normalization-in-pytorch.md
    hash: "sha256:039cfa4131cdf614ea77ec01d56059e5cf3de399a38b791ef1934571981c1261"
  - path: raw/posts/2022/2022-06-09-onnx-simplifier.md
    hash: "sha256:ee017e942025adf0ae74b2b52dc1ba7e56ad81b969a65d2bb63b4ba64dba5cb3"
  - path: raw/posts/2022/2022-06-29-install-tvm-from-source.md
    hash: "sha256:47445ea7d596c3e94b631486b43aa48d31ed4ec491f02f122b811ff75675c9e3"
  - path: raw/posts/2022/2022-06-29-tvm.md
    hash: "sha256:f90de850433073fa5db9283dd7274d2185ac7151d7de43a02abd37b241d5c325"
  - path: raw/posts/2022/2022-07-13-workload-evaluation-using-python.md
    hash: "sha256:fa2a5ee579715c717ae9b43b226a63e72323776624de0539c3484c9fd1bf3dd0"
  - path: raw/posts/2022/2022-07-21-easyedge.md
    hash: "sha256:4bfff60b492b9f7227937b743c746a3c66fbd3386fd480dcf54b53177b80ff6b"
  - path: raw/posts/2022/2022-07-25-edge-hardware.md
    hash: "sha256:5d1f4dedb6fad78a4045d1d6d9ca3471d5578cd47024ca96d01da214580a9bd9"
  - path: raw/posts/2022/2022-08-16-openvino-dl-workbench.md
    hash: "sha256:96b419197aea7d2a0722b1301fbff736e3cefd74c398302529aba752fe5c4704"
last_updated: 2026-07-21
---

# Linux 与系统管理

面向 Ubuntu 生态的 Linux 系统管理实战手册，覆盖远程访问、网络配置、存储管理、镜像源加速、Shell 脚本、性能调优、边缘 AI 推理与模型部署。掌握这些基础能力后，可平滑过渡到 [[Docker-容器化|Docker 容器化]] 与 [[Kubernetes-编排|Kubernetes 编排]] 等上层平台。

---

## 一、远程访问与 SSH

SSH 是 Linux 运维的核心入口。日常维护应同时管理 [[开启SSH服务|SSH 服务]] 本身和客户端连接方式，并权衡便利性与安全性。

### 1.1 SSH 服务端管理

在 Ubuntu 上通过 `openssh-server` 提供远程登录能力：

```bash
# 安装
sudo apt-get install openssh-server

# 启动 / 停止 / 重启
sudo service ssh start | stop | restart

# 状态查询
service ssh status

# 配置文件（修改后需重启）
sudo vi /etc/ssh/sshd_config

# 开机自启
sudo update-rc.d ssh defaults
```

连接命令遵循 `ssh username@ip -p 22` 形式，更多细节见 [[开启SSH服务|开启SSH服务]]。

### 1.2 密钥认证登录

相比密码，密钥对提供更高的安全性。在客户端使用 `ssh-keygen -t rsa` 生成 `id_rsa`（私钥）与 `id_rsa.pub`（公钥），再把公钥复制到服务端的 `~/.ssh/authorized_keys` 即可免密登录：

```bash
ssh-keygen -t rsa
scp .ssh/id_rsa.pub username@hostname:/home/username/.ssh/authorized_keys
ssh username@hostname
```

完整流程参考 [[SSH使用密匙登录|SSH 使用密钥登录]]。

### 1.3 允许 root 密码登录

Ubuntu 默认禁止 root 密码登录（`PermitRootLogin prohibit-password`）。某些场景下（如初始装机调试）需要临时放开：

```bash
sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
systemctl restart sshd
```

> **权衡（Trade-off）**：开启 root 密码登录会显著增大被暴力破解的风险，建议调试完成后立即关闭，或改用密钥方案（参见 [[SSH使用密匙登录|SSH 密钥登录]]）。详见 [[SSH允许使用密码进行root登录|SSH 允许 root 密码登录]]。

### 1.4 图形化远程桌面

当需要操作 GUI 应用时，可在 Ubuntu 上部署 `x11vnc`，在 Mac 上用「屏幕共享」连接：

```bash
sudo apt-get install x11vnc
x11vnc -storepasswd
x11vnc -forever -shared -rfbauth ~/.vnc/passwd
```

Mac 端通过 `IP:5900` 访问。详见 [[MAC远程连接Ubuntu桌面|MAC 远程连接 Ubuntu 桌面]]。

---

## 二、网络配置

Linux 网络栈的配置直接影响服务可达性与名称解析，是系统管理员必须掌握的基础能力。

### 2.1 静态 IP（netplan）

Ubuntu 18.04+ 使用 [[Linux系统网络配置|netplan]] 管理网络。编辑 `/etc/netplan/00-installer-config.yaml`：

```yaml
network:
  ethernets:
    eno1:
      addresses:
      - 172.16.33.1/24
      gateway4: 172.16.33.254
      nameservers: {}
  version: 2
```

应用并验证：

```bash
sudo netplan apply
ip a | grep eno1
```

### 2.2 DNS 设置

在 systemd 主导的系统中，`/etc/resolv.conf` 由 `systemd-resolved` 自动生成，直接编辑会被覆盖。正确做法是修改 `/etc/systemd/resolved.conf`：

```ini
[Resolve]
DNS=8.8.8.8
```

然后重启服务：

```bash
sudo systemctl restart systemd-resolved
```

详见 [[Linux系统DNS设置|Linux 系统 DNS 设置]]。

### 2.3 NFS 文件共享

NFS 提供跨主机的目录共享，适合内网存储场景。

**服务端**：

```bash
sudo apt install nfs-kernel-server
sudo nano /etc/exports
# /data/nfs  172.16.33.0/24(rw,sync,fsid=0,crossmnt,no_subtree_check)
sudo exportfs -ra
sudo systemctl restart nfs-server
```

**客户端**：

```bash
sudo apt install nfs-common
showmount -e 172.16.33.157
sudo mount -t nfs 172.16.33.157:/ $(pwd)/nfs
```

协议版本可通过 `cat /proc/fs/nfsd/versions` 查看。详见 [[NFS配置|NFS 配置]]。

---

## 三、磁盘与存储

### 3.1 分区、格式化与挂载

新增块设备时，典型流程为：

1. **查看设备**：`lsblk` 列出所有块设备。
2. **分区**：`sudo fdisk /dev/sdb`，使用 `n` 新建分区，`w` 写入。大于 2 TiB 的磁盘应使用 GPT 格式。
3. **格式化**：`sudo mkfs.ext4 /dev/sdb1`。
4. **挂载**：`sudo mount /dev/sdb1 /data`。
5. **持久化**：在 `/etc/fstab` 中使用 UUID 挂载，避免设备名变化导致启动失败：

```
/dev/disk/by-uuid/63112c70-92fb-4e36-b118-67004e77158b /data ext4 defaults 0 0
```

详见 [[磁盘分区格式化挂载|磁盘：分区－格式化－挂载]]。

### 3.2 交换分区管理

Kubernetes 等对延迟敏感的平台要求禁用交换分区，以避免内存页换出带来的性能抖动：

```bash
# 查看
swapon --show

# 临时禁用（重启失效）
sudo swapoff -a

# 永久禁用
sudo sed -i '/swap/s/^/#/' /etc/fstab
```

详见 [[Linux系统禁用交换分区|Linux 系统禁用交换分区]]。

---

## 四、用户与身份管理

### 4.1 修改用户名与主机名

直接编辑系统文件的方式（需 root）：

- `/etc/passwd`：用户基本信息
- `/etc/shadow`：密码哈希
- `/etc/group`：组成员
- `/etc/hostname`：主机名
- `/etc/hosts`：本地解析

或使用命令：

```bash
usermod -l new_username -d /home/new_username old_username
groupmod -n new_groupname old_groupname
mv /home/old_username /home/new_username
```

### 4.2 用户增删

```bash
# 创建用户并加入 sudo、docker 组
useradd -m -s /bin/bash -g ai -G sudo,docker username

# 删除用户（含 home）
userdel -rf username

# 追加组
usermod -a -G group_name username
```

详见 [[Linux系统上修改用户名|Linux 系统上修改用户名]]。

---

## 五、输入法与区域设置

### 5.1 时区

```bash
# 列出可用时区
timedatectl list-timezones

# 设置为上海时区
timedatectl set-timezone Asia/Shanghai

# 验证
ll /etc/localtime
```

详见 [[Linux设置时区|Linux 设置时区]]。

### 5.2 输入法

在 CentOS 与 Ubuntu 上安装 ibus 五笔：

```bash
# CentOS
yum install ibus ibus-table ibus-table-wubi

# Ubuntu
apt install ibus ibus-table ibus-table-wubi
```

详见 [[在Linux上安装输入法|在 Linux 上安装输入法]]。

---

## 六、镜像源与加速

国内网络环境下，镜像源配置能显著提升包管理器和仓库的访问速度。

### 6.1 apt 镜像源

备份 `/etc/apt/sources.list` 后替换为国内源：

```bash
sed -i 's/cn.archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list
sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list
apt-get update
```

常见国内源包括阿里云、清华 TUNA、中科大、网易 163 等。详见 [[在Ubuntu上配置apt镜像源|在 Ubuntu 上配置 apt 镜像源]]。

### 6.2 本地仓库（Apt-Cacher NG）

在多机构建中，使用 [[基于Apt-Cacher-NG创建本地Ubuntu存储库|Apt-Cacher NG]] 作为缓存代理可大幅减少外网流量：

```bash
sudo apt install apt-cacher-ng
sudo systemctl enable apt-cacher-ng
sudo service apt-cacher-ng start
```

客户端在 `/etc/apt/apt.conf.d/00aptproxy` 中配置代理地址。

### 6.3 Docker 镜像源

编辑 `/etc/docker/daemon.json`：

```json
{
  "registry-mirrors": ["https://75oltije.mirror.aliyuncs.com"]
}
```

重启生效：`sudo systemctl restart docker`。详见 [[配置Docker镜像源|配置 Docker 镜像源]]。

### 6.4 Kubernetes 镜像源

```bash
apt-get update && apt-get install -y apt-transport-https
curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | apt-key add -
cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main
EOF
apt-get update
```

详见 [[配置Kubernetes镜像源|配置 Kubernetes 镜像源]]。

### 6.5 pip 镜像源

```bash
# 临时使用
pip install -i https://mirrors.aliyun.com/pypi/simple/ package

# 永久设置
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
```

国内可选阿里云、清华、豆瓣、中科大等。详见 [[配置pip镜像源|配置 pip 镜像源]]。

### 6.6 GitHub 加速

常用手段包括：

- 在 URL 中插入 `.cnpmjs.org`：`git clone https://github.com.cnpmjs.org/...`
- 通过 `gh-check` 脚本测速后写入 `/etc/hosts`
- 使用网游加速器（网易 UU、Steam++）

详见 [[GitHub加速|GitHub 加速]]。

---

## 七、命令行工具

命令行是 Linux 系统管理的高频入口，熟练使用文本处理与下载工具能大幅提升效率。

### 7.1 ls — 目录列表

```bash
ls -lh        # 可读大小
ls -lR        # 递归子目录
ls -lt        # 按时间降序
ls -lrt       # 按时间升序
ls -lS        # 按大小降序
ls -lrS       # 按大小升序

# 统计文件 / 目录数
ls -l | grep "^-" | wc -l
ls -l | grep "^d" | wc -l
ls -lR | grep "^-" | wc -l
```

详见 [[命令ls|命令 ls]]。

### 7.2 wget — 网络下载

```bash
wget -i urls.txt -b        # 批量下载 + 后台
wget -i urls.txt -P output # 指定输出目录
wget -c <url>              # 断点续传
```

详见 [[命令wget|命令 wget]]。

### 7.3 sed — 流编辑器

`sed` 擅长基于正则的批量文本替换，分隔符可自由选用（`/`、`#`、`-`）：

```bash
echo "Hi, John." | sed 's/Hi/HI/g'

# 原地编辑文件
sed -i 's/release .*$/CentOS Linux/g' /etc/system-release

# 与 find 批量配合
find labels/ -name '*.txt' -exec sed -i 's/^1 /0 /g' {} +

# 多模式匹配（需 -E）
find labels/ -name '*.txt' -exec sed -i -E 's/^1|2 /0 /g' {} +
```

详见 [[命令sed|命令 sed]]。

### 7.4 grep — 文本搜索

```bash
grep 'text' hello.txt          # 单文件
grep -i 'text' hello.txt       # 忽略大小写
grep -R 'text' *               # 递归搜索
grep -RnH "index-url" ~/.config  # 显示行号与文件名

# 统计目录数
ll | grep '^d' | wc -l
```

详见 [[命令grep|命令 grep]]。

### 7.5 ImageMagick — 图像处理

基于 [[图像格式转换与尺寸调整|ImageMagick]] 可完成格式转换、缩放、灰度化与批量处理：

```bash
# 格式转换
convert test.jpg test.png

# 等比缩放（宽 640）
convert test.jpg -resize 640 test.jpg

# 强制尺寸
convert test.jpg -resize 640x640! test.jpg

# 批量缩放 50%
mogrify -resize 50% images/*.jpg

# 批量转换格式并输出到新目录
mogrify -path new_dir -format jpg images/*.png
```

---

## 八、文件与归档管理

本节覆盖日常运维中文件查找、复制、压缩打包及文件传输等基础操作，这些命令构成了 Linux 系统管理的基石。

### 8.1 find — 文件查找

`find` 支持按名称、修改时间、文件大小等多维度定位文件：

```bash
# 按名称查找（不区分大小写）
find . -name "*.pyc"
find . -iname "*.txt"

# 按修改时间查找
find /var/log -mmin -10        # 最近 10 分钟修改
find /var/log -mtime 0 -ls     # 最近 24 小时（详细信息）
find /var/log -mtime -1        # 0-24 小时内修改
find /var/log -mtime +1        # 超过 48 小时前修改

# 按文件大小查找
find . -size +40M
find . -size +40M -exec ls -lh {} \;
```

批量删除与文件类型筛选：

```bash
find . -name ".DS_Store" -type f -delete
find . -name "._*" -type f -delete
find . -name ".DS_Store" | xargs rm -rf
```

详见 [[命令find|命令 find]]。

### 8.2 cp — 文件拷贝

批量拷贝大量文本文件时，`cp -u` 性能最优（仅拷贝更新或缺失的文件），耗时对比：

| 方式 | 耗时 |
|------|------|
| `cp -u` | 0.470s |
| `xargs` | 30.003s |
| `find -exec` | 32.521s |
| `for` 循环 | 41.256s |

```bash
cp -u labels/*/*.txt datasets/yolo/sign/labels/
```

详见 [[命令cp|命令 cp]]。

### 8.3 tar — 归档与压缩

```bash
# 打包（不压缩）
tar cvf filename.tar filename

# gzip 压缩
tar czvf filename.tgz filename

# bzip2 压缩
tar cjvf filename.tbz2 filename

# 解包
tar xvf filename.tar
tar xzvf filename.tgz

# 查看内容
tar tf filename.tar

# 解压到指定目录
tar xf filename.tar -C dir
```

详见 [[命令tar|命令 tar]]。

### 8.4 zip — ZIP 压缩

```bash
# 打包整个目录
zip -r yolov5.zip yolov5/

# 排除特定目录
zip -r yolov5.zip yolov5/ -x "yolov5/.git/*" -x "yolov5/.github/*"

# 查看压缩文件内容
unzip -l yolov5.zip
zipinfo yolov5.zip
zipinfo -1 yolov5.zip   # 仅文件名
```

详见 [[命令zip|命令 zip]]。

### 8.5 抽取视频关键帧并打包

结合 [[命令find|find]]、[[命令ffmpeg|ffmpeg]] 与 [[命令zip|zip]]，可自动化完成视频关键帧抽取。该方案适用于 [[AI-数据集打包发布|AI 数据集]] 预处理场景：

```bash
ffmpeg -y -vsync 0 -i $file -vf select='eq(pict_type\,I)' -f image2 $extract_image_dir/$filename-%04d.jpg
zip -rqj $zip_file $extract_image_dir
```

完整的批量脚本参考 [[抽取视频关键帧保存zip文件|抽取视频关键帧保存 zip 文件]]。

---

## 九、系统监控与性能调优

### 9.1 top — 实时进程监控

`top` 提供动态的系统资源视图，是 [[Linux-性能优化|性能诊断]] 的首选工具。常用快捷键：

- `Shift+p`：按 CPU 使用率排序
- `Shift+m`：按内存使用率排序
- `1`：显示每个逻辑 CPU 的状态

查看指定进程：`top -p $pid`。详见 [[命令top|命令 top]]。

### 9.2 du — 磁盘使用分析

```bash
du -sh        # 当前目录总大小
du -sh *      # 一级子目录/文件大小
```

结合 [[命令find|find]] 可定位大文件：`find . -size +100M -exec du -h {} \;`。详见 [[命令du|命令 du]]。

### 9.3 Linux 性能优化

性能优化的核心在于理解平均负载（Load Average）的概念——单位时间内处于可运行状态和不可中断状态的平均进程数。**当平均负载高于 CPU 数量 70% 时，应分析排查负载高的问题**。

**常用工具链**：

- `uptime` / `top`：查看 1/5/15 分钟平均负载
- `watch -d uptime`：持续监控并高亮变化
- `stress`：系统压力测试（`--cpu`、`-i`、`-c` 选项）
- `sysstat` 包：
  - `mpstat -P ALL 5`：多核 CPU 性能指标
  - `pidstat -u 5 1`：进程级 CPU、内存、I/O 分析

**典型场景分析**：

| 场景 | 模拟命令 | 关键指标 |
|------|----------|----------|
| CPU 密集型 | `stress --cpu 1 --timeout 600` | `%usr` 接近 100% |
| I/O 密集型 | `stress -i 1 --hdd 1 --timeout 600` | `%iowait` 显著升高 |
| 大量进程 | `stress -c 8 --timeout 600` | 负载远超 CPU 核数 |

详见 [[Linux-性能优化|Linux 性能优化]]。

---

## 十、权限与链接管理

### 10.1 chown — 文件所有权

在 [[基于vsftpd安装FTP服务器|FTP 服务器]] 部署或 [[MinIO-Quickstart|MinIO 存储]] 配置中，经常需要调整文件权限：

```bash
sudo chown root filename         # 修改所有者
sudo chown :root filename        # 修改组
sudo chown wjj:wjj filename      # 同时修改
sudo chown -R root:root test     # 递归修改
```

详见 [[命令chown|命令 chown]]。

### 10.2 ln — 符号链接

软链接（Symbolic Link）类似指针，常用于路径映射，例如 [[基于Apt-Cacher-NG创建本地Ubuntu存储库|Apt-Cacher NG]] 的目录映射：

```bash
ln -s /data/apt-mirror/mirror/archive.ubuntu.com/ubuntu /var/www/ubuntu

# 查看
ll /var/www/ubuntu
# lrwxrwxrwx ... /var/www/ubuntu -> /data/apt-mirror/...

# 删除
unlink /var/www/ubuntu
rm /var/www/ubuntu
```

详见 [[命令ln|命令 ln]]。

---

## 十一、Shell 脚本编程

### 11.1 Shell 执行方式

同一脚本在不同执行方式下行为差异显著，理解这些差异对 [[Linux-性能优化|性能脚本]] 和 [[AI-模型打包发布|模型发布]] 至关重要：

| 方式 | 是否创建子进程 | 对当前 Shell 的影响 |
|------|---------------|-------------------|
| `bash script.sh` | 是 | 无 |
| `./script.sh` | 是 | 无 |
| `source script.sh` | 否 | 有（如 `cd`） |
| `. script.sh` | 否 | 有（同 source） |

详见 [[Linux-Shell-执行方式|Linux Shell 执行方式]]。

### 11.2 Shell 实践要点

**快捷键**：`Ctrl+r`（历史搜索）、`Ctrl+l`（清屏）、`Ctrl+a/e`（行首/行尾）。

**重定向**：

```bash
hello 2> log.error        # 错误信息
echo hello &> log.info    # 所有信息
cat > hello.sh << EOF     # 创建文件并写入
```

**变量**：`${var}` 引用、`export` 导出子进程可见、`unset` 移除。

**执行模式与变量作用域**：默认变量仅在当前 Shell 生效；`export` 后子进程可见。结合 [[命令source|source]] 可在当前环境加载配置。

完整 Shell 语法（数组、函数、运算符、表达式）参考 [[Linux-Shell-实践|Linux Shell 实践]]。

---

## 十二、帮助系统与文档

### 12.1 man / help / info

Linux 提供了三层帮助体系：[[命令man-help-info|man]]（完整手册）、[[命令help-info|help]]（Shell 内建命令简述）、[[命令info|info]]（超文本详细文档）：

```bash
man man            # 手册章节说明（1-9 章）
man 7 man          # 查看指定章节
man -a passwd      # 搜索所有匹配
help cd            # 内部命令帮助
ls --help          # 外部命令帮助
info cd            # 更详细的文档
type cd            # 查看命令类型（内部/外部）
```

详见 [[命令man-help-info|命令 man help info]]。

---

## 十三、SSH 进阶配置

### 13.1 连接与端口

SSH 是 [[开启SSH服务|远程管理]] 的核心协议，支持端口指定与密钥认证：

```bash
ssh -p <port> user@hostname
ssh -i <identity_file> user@hostname
```

详见 [[命令ssh|命令 ssh]]、[[SSH使用密匙登录|SSH 使用密钥登录]]。

### 13.2 登录欢迎信息（motd）

通过 `/etc/update-motd.d/` 目录下的脚本自定义登录欢迎信息：

```bash
# 添加静态消息
sudo sh -c 'echo "Hello World!" > /etc/motd'

# 禁用所有动态脚本
sudo chmod -x /etc/update-motd.d/*

# 自定义天气显示
sudo apt install ansiweather
# 创建 /etc/update-motd.d/99-location-weather
#!/bin/sh
ansiweather -l Jinan
```

详见 [[SSH-登录欢迎信息|SSH 登录欢迎信息]]。

### 13.3 X11 Forwarding

在 macOS 上通过 XQuartz 实现远程 GUI 应用显示：

```bash
# 不使用 XAuth（信任模式）
ssh -Y username@hostname

# 使用 XAuth
ssh -X username@hostname
```

配置文件 `~/.ssh/config`：

```
Host *
    XAuthLocation /opt/X11/bin/xauth
```

详见 [[SSH-X11-Forwarding|SSH X11 Forwarding]]。

---

## 十四、包管理与服务部署

### 14.1 yum（CentOS）

在 [[配置Kubernetes镜像源|Kubernetes]] 或 [[配置Docker镜像源|Docker]] 部署前，yum 是 CentOS 环境下的核心包管理工具：

```bash
# 下载软件及依赖（不安装）
yum install docker-ce --downloadonly --downloaddir=docker-ce

# 列出所有版本
yum list docker-ce --showduplicates
```

详见 [[命令yum|命令 yum]]。

### 14.2 helm（Kubernetes 包管理）

```bash
# 安装
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh

# 仓库管理
helm repo add stable https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
helm repo update

# 搜索与安装
helm search repo prometheus
helm install ingress-nginx ingress-nginx/ingress-nginx
helm uninstall ingress-nginx
```

详见 [[命令helm|命令 helm]]。

### 14.3 vsftpd — FTP 服务器

```bash
sudo apt-get install vsftpd
vim /etc/vsftpd.conf        # 配置文件
man vsftpd.conf             # 查看详细文档
sudo systemctl restart vsftpd
```

匿名登录：设置 `anonymous_enable=YES`，文件存放于 `/srv/ftp`。详见 [[基于vsftpd安装FTP服务器|基于 vsftpd 安装 FTP 服务器]]。

---

## 十五、编码与数据格式

### 15.1 base64 编码

base64 在 [[FastAPI-上传和下载文件的基准测试|文件传输]]、[[命令curl|curl]] 请求中广泛使用：

```bash
# Linux（禁用换行）
base64 -w0 file

# 解码
base64 -d

# 避免 echo 追加换行符
printf 'admin' | base64    # YWRtaW4=
echo -n 'admin' | base64   # YWRtaW4=
```

详见 [[命令base64|命令 base64]]。

### 15.2 JSON 格式化

```bash
# jq
jq . test.json
jq . <<< '{ "key": "value" }'

# Python
python -m json.tool test.json

# Vim 内格式化
:%!jq .
:%!python -m json.tool
```

详见 [[Json-Formatter|Json Formatter]]。

### 15.3 终端浏览 Markdown / HTML

```bash
# Markdown
pandoc README.md | lynx -stdin
grip -b README.md && lynx http://localhost:6419/

# HTML
w3m index.html
pandoc index.html | lynx -stdin
```

详见 [[使用终端浏览Markdown和HTML|使用终端浏览 Markdown 和 HTML]]。

---

## 十六、开发工具与 IDE

### 16.1 Vim 编辑器

Vim 是 Linux 下最强大的文本编辑器之一，掌握其四种模式（正常、插入、命令、可视）是高效编辑的基础。在 [[Linux-Shell-实践|Shell 脚本]] 编辑、[[Linux-性能优化|配置文件]] 修改中不可或缺：

- **安装**：`sudo apt install vim-gtk3`（带图形界面）
- **二进制模式**：`vim -b file.txt`
- **比较文件**：`vim -d file1 file2` 或 `vimdiff`
- **十六进制**：`:%!xxd` / `:%!xxd -r`

完整快捷键与配置参考 [[Vim-实践|Vim 实践]]。

### 16.2 Thonny Python IDE

Thonny 是面向 MicroPython 设备的轻量级 IDE，支持直接连接 ESP8266/ESP32 等设备进行开发：

- 菜单「运行 → 选择解释器」选择 MicroPython
- 菜单「文件 → 打开」选择 MicroPython 设备上的文件
- 在 Shell 窗口即时执行 Python 语句

详见 [[Thonny-Python-IDE|Thonny Python IDE]]。

### 16.3 Fritzing 电子设计

Fritzing 是开源电子设计自动化软件，适合绘制电路原理图与 PCB 布局，社区提供 ESP8266/ESP32 等模块的元件库。详见 [[Fritzing-开源电子设计自动化软件|Fritzing 开源电子设计自动化软件]]。

---

## 十七、AI 数据集与模型打包发布

### 17.1 数据集打包

在 [[使用-FastAPI-开发-RESTAPI-服务|REST API]] 或 [[Get-Started-YOLOv5|YOLOv5]] 训练流程中，数据集需标准化打包：

```bash
DATE=$(date '+%Y-%m-%d')
tar cvf sign-yolo-$DATE.tar labelimg/ classes.txt images/ labels data.yaml
scp sign-yolo-$DATE.tar username@ip:/data/datasets
```

详见 [[AI-数据集打包发布|AI 数据集打包发布]]。

### 17.2 模型自动化发布

基于 [[Docker-容器化|Docker]] 的模型打包发布流程，结合 [[命令tar|tar]] 与 [[命令scp|scp]] 实现自动化：

1. 准备 `config.yaml` + `model.onnx`
2. 通过 `docker run --rm -v ... model-package-release model-name` 自动打包
3. 上传到模型服务器（`scp`）

完整脚本与 Dockerfile 参考 [[AI-模型打包发布|AI 模型打包发布]]。

---

## 十八、嵌入式系统编译

### 18.1 编译寒武纪 MLU220 嵌入式操作系统

基于 Buildroot 的 OpenIL 项目，通过交叉编译生成嵌入式 Linux 系统，适用于 [[边缘硬件|边缘计算]] 场景：

```bash
git clone https://github.com/openil/openil.git
cd openil/
git branch OpenIL-v1.8-202005              # 切换版本
make nxp_ls1043ardb-64b_ubuntu_defconfig  # 生成配置
LD_LIBRARY_PATH= make                      # 编译（需清空 LD_LIBRARY_PATH）
```

详见 [[编译寒武纪MLU220的嵌入式操作系统|编译寒武纪 MLU220 的嵌入式操作系统]]。

---

## 十九、Go 语言环境

```bash
# 安装
wget https://golang.google.cn/dl/go1.17.7.linux-amd64.tar.gz
sudo tar -C /usr/local/ -xzf go1.17.7.linux-amd64.tar.gz

# 配置代理
export GOPROXY=https://goproxy.cn,direct
export GO111MODULE=on
```

详见 [[安装Go|安装 Go]]。

---

## 二十、MinIO 对象存储

MinIO 是 S3 兼容的分布式对象存储，适合私有云环境：

```bash
# Standalone
docker run --rm -p 9000:9000 -p 9001:9001 \
  -v /data/minio/data:/data \
  -e "MINIO_ROOT_USER=admin" -e "MINIO_ROOT_PASSWORD=12345678" \
  minio/minio server /data --console-address ":9001"

# 客户端
mc alias set minio http://172.17.0.2:9000 admin 12345678
mc mb minio/test
mc cp hello.txt minio/test
```

详见 [[MinIO-Quickstart|MinIO Quickstart]]。

---

## 二十一、HTTP 基准测试

### 21.1 wrk

wrk 是基于 HTTP/1.1 的高性能压测工具，常用于 [[FastAPI-上传和下载文件的基准测试|FastAPI 基准测试]]、[[Linux-性能优化|服务性能评估]]：

```bash
# 安装
git clone https://github.com/wg/wrk.git
make -j $(nproc)

# 测试
wrk -t10 -c100 -d10 http://www.baidu.com/
wrk -c10 -t4 --latency http://www.baidu.com/

# POST 请求（Lua 脚本）
wrk -c1 -t1 -d1 -s post.lua "http://127.0.0.1:8000/users"
```

### 21.2 ab

ab（Apache Bench）使用 HTTP/1.0，适合快速验证 [[使用-FastAPI-开发-RESTAPI-服务|REST API]] 基本性能：

```bash
ab -n200 -c20 http://www.baidu.com/
ab -c100 -t10 http://www.baidu.com/
ab -p postdata.txt -T "application/json" http://127.0.0.1:8000/users
```

详见 [[HTTP-基准测试工具|HTTP 基准测试工具]]。

---

## 二十二、云服务与 FastAPI 服务部署

### 22.1 阿里云 ECS 开放端口

在 [[阿里云ECS开放端口|ECS]] 控制台配置安全组规则（入方向），开放 5000（Flask）/8000（FastAPI）端口。同时确保 Web 服务器绑定 `0.0.0.0`：

```bash
uvicorn --host 0.0.0.0
gunicorn --bind 0.0.0.0
```

详见 [[阿里云ECS开放端口|阿里云 ECS 开放端口]]。

### 22.2 FastAPI 文件上传下载基准测试

基于 [[HTTP-基准测试工具|wrk]] 对 [[使用-FastAPI-开发-RESTAPI-服务|FastAPI]] 多种上传/下载模式进行性能对比（40 核 / 256G / Ubuntu 20.04）：

- **二进制流式上传**效率最高（~4500 req/s）
- `gunicorn + uvicorn` 组合比单独 uvicorn 更稳定
- 流式下载可达 ~4500 req/s

详见 [[FastAPI-上传和下载文件的基准测试|FastAPI 上传和下载文件的基准测试]]。

### 22.3 使用 FastAPI 开发 REST API

FastAPI 是基于 Python 的现代 Web 框架，支持异步、自动文档生成，适合构建 [[AI-模型打包发布|AI 模型]] 推理服务：

```python
from fastapi import FastAPI
app = FastAPI()

@app.get('/')
async def index():
    return {'Hello': 'World!'}
```

部署方式：

```bash
uvicorn app.main:app --host 0.0.0.0 --workers 4
gunicorn app.main:app --bind 0.0.0.0 --workers 4 --worker-class uvicorn.workers.UvicornWorker
```

详见 [[使用-FastAPI-开发-RESTAPI-服务|使用 FastAPI 开发 REST API 服务]]。

---

## 二十三、Python 环境安装

### 23.1 Install Python3.9 in Ubuntu 20.04

```bash
sudo apt install build-essential python3.9 python3.9-dev python3.9-distutils -y
sudo ln -s /usr/bin/python3.9 /usr/bin/python
curl https://bootstrap.pypa.io/get-pip.py | sudo python -
```

> **注意**：必须安装 `python3.9-distutils`，否则 `get-pip.py` 会报 `ModuleNotFoundError: No module named 'distutils.cmd'`。详见 [[Install-Python3.9-in-Ubuntu20.04|Install Python3.9 in Ubuntu20.04]]。

---

## 二十四、OpenVINO 推理引擎

OpenVINO（Open Visual Inference and Neural Network Optimization）是 Intel 推出的深度学习推理优化工具套件，覆盖模型转换、推理加速与部署全流程。

### 24.1 工作流程

完整流程为：**计划与设置 → 训练模型 → 转换与优化 → 调整性能 → 部署应用**。

模型优化器（Model Optimizer）将 TensorFlow、Caffe、ONNX 等格式转换为 IR（`.xml` + `.bin`），推理引擎（Inference Engine）加载 IR 在目标硬件上执行。

详见 [[OpenVINO-的工作原理|OpenVINO 的工作原理]]、[[Get-Started-OpenVINO|Get Started OpenVINO]]。

### 24.2 Open Model Zoo

[[Open-Model-Zoo|Open Model Zoo]] 提供预训练模型与自动化工具，是 [[OpenVINO-的工作原理|OpenVINO 工作流]] 的起点：

```bash
omz_downloader --name googlenet-v1       # 下载模型
omz_converter --name googlenet-v1         # 转换为 IR
omz_quantizer                             # 训练后量化
```

支持人脸检测（MTCNN）、图像分类、目标检测等 Demo。详见 [[Open-Model-Zoo|Open Model Zoo]]。

### 24.3 图像分类

基于 GoogLeNet-v1（Caffe）的同步推理示例，结合 [[OpenVINO-的工作原理|模型优化器]] 完成 IR 转换：

```bash
omz_downloader --name googlenet-v1
omz_converter --name googlenet-v1
# Python 代码加载 IR 并推理
```

详见 [[OpenVINO-图像分类|OpenVINO 图像分类]]。

### 24.4 目标检测

基于 SSD300（PASCAL VOC）的推理示例，流程与 [[OpenVINO-图像分类|图像分类]] 一致。详见 [[OpenVINO-目标检测|OpenVINO 目标检测]]。

### 24.5 神经网络性能分析

通过 [[OpenVINO-的工作原理|OpenVINO]] 的 Profiling API 可获取每层推理耗时，辅助 [[Linux-性能优化|性能调优]]：

```python
core.set_property(device_name, {"PERF_COUNT": "YES"})
prof_info = request.get_profiling_info()
```

逐层分析最耗时算子，指导优化方向。详见 [[OpenVINO-神经网络性能分析|OpenVINO 神经网络性能分析]]。

### 24.6 DL Workbench

DL Workbench 提供图形化界面（基于 [[Docker-容器化|Docker]]），简化 [[OpenVINO-的工作原理|OpenVINO]] 模型调优流程：

```bash
docker pull openvino/workbench:2022.1
docker run -p 0.0.0.0:5665:5665 --name workbench -it openvino/workbench:2022.1
# 浏览器访问 http://127.0.0.1:5665/
```

详见 [[OpenVINO-DL-Workbench|OpenVINO Deep Learning Workbench]]。

---

## 二十五、NVIDIA 软件栈与 GPU 管理

### 25.1 软件栈搭建

NVIDIA 深度学习软件栈自底向上：**GPU Driver → CUDA Toolkit → cuDNN → TensorRT → NCCL**，是 [[GPU-与-CUDA-开发|GPU 开发]] 的基础：

```bash
# Ubuntu 驱动安装
sudo ubuntu-drivers devices
sudo apt install nvidia-driver-510
sudo reboot
nvidia-smi

# CUDA Toolkit 安装
sudo sh cuda_xx.x.x_xxx.xx.xx_linux.run
```

详见 [[NVIDIA-软件栈搭建|NVIDIA 软件栈搭建]]、[[在Ubuntu上安装NVIDIA-GPU驱动|在 Ubuntu 安装 NVIDIA GPU 驱动]]。

### 25.2 GPU 切换（NVIDIA → Intel IGD）

当独显专用于 [[NVIDIA-软件栈搭建|深度学习计算]] 时，可将集成显卡用于显示输出：

1. **BIOS**：设置为 IGD（集成显卡）
2. **配置 X Window**：编辑 `/etc/X11/xorg.conf`，指定 `Driver "intel"` 与 `BusID "PCI:0:2:0"`
3. **常见问题**：鼠标键盘失灵（`apt install xserver-xorg-input-all`）、无法登录（删除 `.Xauthority`）

详见 [[Ubuntu-上将-NVIDIA-GPU-切换为-Intel-集成显卡-IGD|Ubuntu 上将 NVIDIA GPU 切换为 Intel 集成显卡 IGD]]。

---

## 二十六、模型优化与编译

### 26.1 PyTorch 融合 Conv-BN

在 [[OpenVINO-的工作原理|推理优化]] 阶段将卷积层（Conv）与批量标准化层（BatchNorm）融合，可减少 ~25% 推理时间：

```python
fused_conv = torch.nn.utils.fusion.fuse_conv_bn_eval(conv, bn)
```

原理：将 BN 的缩放/偏移参数合并到 Conv 的权重中，常用于 [[Get-Started-YOLOv5|YOLOv5]] 模型加速。详见 [[在PyTorch中融合卷积和批量标准化|在 PyTorch 中融合卷积和批量标准化]]。

### 26.2 ONNX Simplifier

`onnxsim` 通过常量折叠与图变换优化 ONNX 模型结构，是 [[AI-模型打包发布|模型发布]] 前的关键步骤：

```bash
pip install onnx-simplifier
onnxsim input.onnx output.onnx
```

PyTorch 导出时 `do_constant_folding=True` 已做部分优化，onnxsim 进一步挖掘。详见 [[ONNX-Simplifier|ONNX Simplifier]]。

### 26.3 TVM 深度学习编译器

TVM 是开源的端到端 [[边缘硬件|边缘]] 深度学习编译器栈，支持将模型编译到多种后端（LLVM、CUDA 等）：

```bash
git clone --recursive https://github.com/apache/tvm tvm
# 配置 build/config.cmake（启用 USE_CUDA、USE_LLVM）
mkdir build && cd build && cmake .. && make -j64
export TVM_HOME=/path/to/tvm
export PYTHONPATH=$TVM_HOME/python:${PYTHONPATH}
```

使用 TVMC 高层 API：

```python
from tvm.driver import tvmc
model = tvmc.load('resnet50-v2-7.onnx')
package = tvmc.compile(model, target="llvm")
```

详见 [[Install-TVM-from-Source|Install TVM from Source]]、[[TVM|TVM]]。

---

## 二十七、边缘 AI 平台与硬件

### 27.1 百度 EasyEdge

[[百度-EasyEdge|EasyEdge]] 基于 Paddle Lite，将深度学习模型部署到 [[边缘硬件|边缘设备]]：

- 支持 Caffe、TensorFlow、PyTorch、PaddlePaddle、ONNX 等框架
- 支持 [[OpenVINO-图像分类|图像分类]]、[[OpenVINO-目标检测|目标检测]]、语义分割等任务
- 适配多种 AI 芯片与操作系统（Linux/Windows/Android/iOS）

详见 [[百度-EasyEdge|百度 EasyEdge 端与边缘 AI 服务平台]]。

### 27.2 边缘硬件基础

[[边缘硬件|边缘计算]] 硬件涉及多种接口与存储标准，与 [[编译寒武纪MLU220的嵌入式操作系统|嵌入式系统]] 密切相关：

- **M.2**：取代 mSATA 的新一代接口标准（2242/2260/2280）
- **NVMe**：基于 PCIe 的高速 SSD 协议
- **DDR / LPDDR**：标准内存与低功耗内存
- **Intel Movidius Myriad X**：VPU 神经计算棒（NCS2）

详见 [[边缘硬件|边缘硬件]]、[[Jetson-与边缘计算|Jetson 与边缘计算]]。

---

## 二十八、自动化工具

### 28.1 Python 工作量估算自动化

使用 Python（openpyxl + typer）可自动完成 Excel 工作量估算表的数据填充，适合 [[AI-模型打包发布|AI 项目管理]] 场景：

```bash
pip install typer python-docx
python workload-evaluation.py input.xlsx
```

脚本自动定位"工作量估算"列，拷贝单元格值与样式到目标列。详见 [[使用-Python-自动进行工作量估算|使用 Python 自动进行工作量估算]]。

---

## 二十九、关联阅读

- 上层平台：[[Docker-容器化|Docker 容器化]]、[[Kubernetes-编排|Kubernetes 编排]]
- 开发环境：[[IDE-与编辑器|IDE 与编辑器]]、[[GPU-与-CUDA-开发|GPU 与 CUDA 开发]]
- 边缘场景：[[Jetson-与边缘计算|Jetson 与边缘计算]]、[[边缘硬件|边缘硬件]]
- 模型推理：[[OpenVINO-的工作原理|OpenVINO 的工作原理]]、[[TVM|TVM]]、[[ONNX-Simplifier|ONNX Simplifier]]
- Web 服务：[[使用-FastAPI-开发-RESTAPI-服务|使用 FastAPI 开发 REST API 服务]]、[[FastAPI-上传和下载文件的基准测试|FastAPI 基准测试]]
- 存储方案：[[MinIO-Quickstart|MinIO Quickstart]]、[[NFS配置|NFS 配置]]
