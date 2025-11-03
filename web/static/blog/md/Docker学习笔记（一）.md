# 一、docker学习笔记（一）

## 1.1、docker用户

```bash

# 1、创建名为 docker新用户
sudo adduser docker

# 2、将用户添加到sudo组，获得sudo权限
sudo usermod -aG sudo docker

# 3、将用户添加到docker组
sudo usermod -aG docker docker

```

## 1.2、docker安装(手动)

```bash
# 1. 先修复apt仓库的GPG密钥问题
# 密钥来自于DeepSeek
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7EA0A9C3F273FCD8

# 2. 更新包列表
sudo apt-get update

# 3. 安装docker
sudo apt-get install -y docker.io

# 4. 安装docker Compose
sudo apt-get install -y docker-compose

# 5. 启动docker服务
sudo systemctl start docker
sudo systemctl enable docker

# 6. 验证安装
docker --version
sudo systemctl status docker

# 7. 验证docker Compose
docker-compose --version

```

## 1.3 解决docker镜像源问题（来源：[解决docker: Error response from daemon: Get “https://registry-1.docker.io/v2/“:连接超时问题](https://blog.csdn.net/y2020520/article/details/144423904)）

```bash
vim /etc/docker/daemon.json
```

添加以下配置：

```json

{
  "registry-mirrors": [
       "http://hub-mirror.c.163.com",
       "https://mirrors.tuna.tsinghua.edu.cn",
       "http://mirrors.sohu.com",
       "https://ccr.ccs.tencentyun.com",
       "https://docker.m.daocloud.io",
       "https://docker.awsl9527.cn"
  ]
}
```

重新加载配置

```bash
# 重新加载配置
systemctl daemon-reload

# 重启docker
systemctl restart docker
```

## 1.4、运行第一个docker案例

```bash
docker run -d -p 81:80 httpd
```

![20251103094225](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20251103094225.png)

## 1.5、构建docker镜像（dockerfile模式）

docker提供了两种方式来构建镜像：docker commit命令与dockerfile构建文件  
docker commit命令存在以下缺陷：  

1. 手工创建镜像的方式，镜像构建过程不透明，镜像构建过程的任何改动，都需要重新执行一遍构建过程  
2. 手工创建镜像的方式，镜像构建过程不利于镜像的复用和维护  

因此，docker提供了dockerfile文件来构建镜像，dockerfile文件是一个文本文件，包含了一条条的指令，每一条指令构建一层，因此每一条指令的内容，就是描述该层应当如何构建。  

以创一个安装vim的镜像为例，首先创建一个dockerfile文件  

```dockerfile
FROM ubuntu
RUN apt-get update && apt-get install -y vim
```

执行docker build命令，构建镜像  

```bash
docker build -t ubuntu-with-vi-dockerfile .
```

通过docker images命令查看镜像  

![20251103101313](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20251103101313.png)

docker history命令会显示镜像的构建历史，也就是dockerfile的执行过程。  
ubuntu-with-i-dockerfile 与 ubunt 镜像相比，只是多了顶部的一层e22afedc94e6，由apt-get命令创建，大小为130MB。  
docker history也向我们展示了镜像的分层结构，每一层由上至下排列。  

![20251103103304](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20251103103304.png)

总结通过dockerfile创建镜像的过程：  

1. 从base镜像运行一个容器  
2. 执行一条命令，对容器进行修改  
3. 执行类似docker commit的操作，生成一个新的镜像层  
4. docker再基于刚刚提交的镜像运行一个新容器  
5. 重复2-4步，直到dockerfile中的所有指令执行完毕  
