# 一、docker学习笔记（一）

## 附录-docker常用命令

| CMD命令 | 说明 |
| -- | -- |
| docker ps -a | 查看所有容器，包括未运行的容器 |
| docker stop ${CONTAINER_ID} | 停止指定容器 |  
| docker start ${CONTAINER_ID} | 启动指定容器 |
| docker restart ${CONTAINER_ID} | 重启指定容器 |
| docker rm ${CONTAINER_ID} | 删除指定容器 |
| docker rmi ${IMAGE_ID} | 删除指定镜像 |
| docker volume rm ${VOLUME_ID} | 删除指定卷 |
| docker network rm ${NETWORK_ID} | 删除指定网络 |

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

## 1.6、dockerfile常用指令

| 指令 | 说明 |
| -- | -- |
| FROM | 指定base镜像 |
| MAINTAINER | 设置镜像的作者，可以是任意字符串 |
| COPY | 将文件从build context复制到镜像中 |
| ADD | 将文件从build context复制到镜像中，支持解压缩 |
| ENV | 设置环境变量 |
| EXPOSE | 指定容器中的进程会监听某个端口，docker可以将该端口暴露出来 |
| VOLUME | 将文件或目录声明为volume |
| WORKDIR | 为后面的RUN、CMD、ENTRYPOINT、ADD或COPY指令设置镜像中的当前工作目录 |
| RUN | 在容器中运行指定的命令 |
| CMD | 容器启时运行指定的命令（可以有多个，但仅最后一个生效） |
| ENTRYPOINT | 容器启动时运行指定的命令（可以有多个，但仅最后一个生效） |

## 1.7、构建一个自己的docker镜像

![20251103140850](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20251103140850.png)

![20251103140426](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20251103140426.png)

运行image：

![20251103140552](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20251103140552.png)

## 1.8、docker的长期运行与停止

容器的生命周期依赖于启动时执行的命令，只要命令不结束，容器也就不会退出。  
例如， 我们可以通过运行一个长期命令来保持容器的运行状态：  

```bash
docker run -d ubuntu /bin/sh -c "while true; do echo hello world; sleep 1; done"
```

![20260104145441](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20260104145441.png)

不过这种方法有个缺点：占用了一个终端。  
如果我们希望容器在后台运行，并且不占用终端，可以加上参数-d以后台方式启动容器：  

```bash
docker run -d ubuntu /bin/bash -c "while true; do echo hello world; sleep 1; done"
```

![20260104145801](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20260104145801.png)

容器的停止通过docker stop + CONTAINER ID命令实现：  

![20260104150101](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20260104150101.png)

## 1.9、两种进入容器的方法

我们经常需要到进到容器里去做一些工作，比如查看日志、调试、启动其他进程等。有两种方法进入容器：attach 和 exec  

### 1.9.1、docker attach

通过docker attach命令可以进入容器，并与容器进行交互。  
可以看到该容器每隔20s打印一次“hello world”。  

![20260104151343](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20260104151343.png)

如果要退出容器，可以使用Ctrl+P+Q组合键

### 1.9.2、docker exec

通过docker exec命令进入相同的容器：

![20260104151732](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20260104151732.png)

exec参数说明如下：  

1. -it 以交互模式进入容器，执行bash，其结果就是打开一个bash终端
2. 可以像在普通Linux中一样执行命令。ps -elf显示了容器启动进程weile以及当前的bash进程
3. exit退出容器，但是容器仍然运行

### 1.9.3、docker attach与exec的区别

attach和exec的区别在于：  

1. attach直接进入容器启动命令的终端，不会启动新的进程
2. exec可以启动新的进程，并且可以进入新的进程的终端
3. 如果想直接在终端中查看启动命令的输出用attach，其他情况使用exec
4. 如果知识为了查看启动命令的输出，可以使用docker logs命令，作用与tail类似

![20260104152554](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20260104152554.png)

## 1.10 容器的分类

容器按照用途可以分为两类：服务类容器和工具类容器。  
服务类容器以daemon的形式运行，对外提供服务，比如web server、数据库等，通过-d参数以后台的方式启动这类容器时非常合适的。如果要排查问题，可以通过exec -it进入容器。  
工具类容器通常能够给我们提供一个临时的工作环境，通常以run -it的方式启动，比如验证访问intelnet的能力：

![20260104153239](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20260104153239.png)

## 1.11 stop/start/restart容器

docker stop本质上是向指定的docker进程发送一个SIGTERM信号，然后等待容器进程退出。  
docker kill命令本质上是向指定的docker进程发送一个SIGKILL信号，强制终止容器进程。  
对于处于停止状态的容器，可以通过docker start命令启动容器。  
docker restart可以重启容器，其作用就是依次执行docker stop和docker start。  

![20260106085145](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20260106085145.png)

在实际应用中，容器可能因某种错误而停止运行，对于服务类容器，我们通常希望在这种情况下容器能够自动重启。在启动容器时设置--restart参数，可以实现该效果。  

![20260106085609](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20260106085609.png)

--restart=always意味着无论容器因何种原因退出（包括正常退出），都会立即重启；该参数的形式还可以是--restart=on-failure:3，表示如果容器以非0状态退出，则最多重启3次。

## 1.12 pause/unpause容器

有时我们只是希望让容器暂停运行，比如在调试时，可以使用docker pause命令暂停容器。  
处于暂停状态的容器不会占用CPU资源，直到通过docker unpause命令恢复运行。  

![20260106162018](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20260106162018.png)

## 1.13 容器的删除

使用docker一段时间后，host上可能会有大量已经退出的容器，这些容器依然会占用host的文件系统资源。  
如果确认不会再重启此类容器，可以通过docker rm命令删除容器。  

![20260106162241](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20260106162241.png)

如果希望批量删除所有已经退出的容器，可以执行：docker rm $(docker ps -aq -f status=exited)

![20260106162457](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20260106162457.png)

## 1.14 资源限制

一个docker host上会运行若干容器，每个容器都需要CPU、内存和IO资源。对于KVM、VMware等虚拟化技术，用户可以控制分配多少CPU、内存资源给每个虚拟机。  
对于容器，docker也提供了类似的资源限制功能，避免某个容器因为占用太多资源从而影响其他容器乃至整个host的性能。  

### 1.14.1、内存限额

与操作系统类似，容器可以使用的内存包括两部分：物理内存和虚拟内存swap：  

1. -m 或 --memory：设置内存的使用限额，例如100MB， 2GB。
2. --memory-swap：设置内存加swap的总和。

例如如下命令：

```bash
docker run -m 200M --memory-swap=300M -d ubuntu /bin/sh -c "while true; do echo hello world; sleep 1; done"
```

其含义是允许该容器最多使用200MB的内存和100MB的swap。如果上述值为-1，即对容器内存和swap的使用没有限制。  

使用progrium/stress镜像来学习如何为容器分配内存。该镜像可用于对容器执行压力测试：

```bash
docker run -it -m 200M --memory-swap=300M progrium/stress --vm 1 --vm-bytes 280M
```

* --vm 1：启动1个内存工作线程
* --vm-bytes 280M：每个工作线程分配280MB的内存
