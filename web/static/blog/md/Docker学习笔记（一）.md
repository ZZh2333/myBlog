# 一、Docker学习笔记（一）

## 1.1、Docker用户

```bash

# 1、创建名为 docker新用户
sudo adduser docker

# 2、将用户添加到sudo组，获得sudo权限
sudo usermod -aG sudo docker

# 3、将用户添加到docker组
sudo usermod -aG docker docker

```

## 1.2、Docker安装(手动)

```bash
# 1. 先修复apt仓库的GPG密钥问题
# 密钥来自于DeepSeek
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7EA0A9C3F273FCD8

# 2. 更新包列表
sudo apt-get update

# 3. 安装Docker
sudo apt-get install -y docker.io

# 4. 安装Docker Compose
sudo apt-get install -y docker-compose

# 5. 启动Docker服务
sudo systemctl start docker
sudo systemctl enable docker

# 6. 验证安装
docker --version
sudo systemctl status docker
```
