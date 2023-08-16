# 一、FHS文件系统层次标准

|目录|目录用途|
|----|----|
|/bin|常见的用户指令|
|/boot|内核和启动文件|
|/dev|设备文件|
|/etc|系统和服务的配置文件|
|/home|系统默认的普通用户的家目录|
|/lib|系统函数库目录|
|/lost+found|ext3文件系统需要的目录，用于磁盘检查|
|/mnt|系统加载文件系统时常用的挂载点|
|/opt|第三方软件安装目录|
|/proc|虚拟文件系统|
|/root|root用户的家目录|
|/sbin|存放系统管理命令|
|/tmp|临时文件的存放目录|
|/usr|存放与用户直接相关的文件和目录|
|/media|系统用来挂载光驱等临时文件系统的挂载点|

# 二、查找文件

## 2.1、find命令

**find常见参数**
|参数|含义|
|---|---|
|-name FILENAME|查找文件名为FILENAME的文件|
|-perm|根据文件权限查找|
|-user USERNAME|根据用户名查找|
|-mtime -n/+n|查找n天内/n天前更改过的文件|
|-atime -n/+n|查找n天内/n天前访问过的文件|
|-ctime -n/+n|查找n天内/n天前创建的文件|
|-newer FILENAME|查找更改时间比FILENAME新的文件|
|-type b/d/c/p/l/f/s|查找块/目录/字符/管道/链接/普通/套接字文件|
|-size|根据文件大小查找|
|-depth|最大查找目录深度|

```shell
#find PATH -name FILENAME
find / -name *.log
```

![20230816094810](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230816094810.png)

## 2.2、which命令

which用于从系统的PATH变量所定义的目录中查找可执行文件的绝对路径。

```shell
which passwd
```

![20230816101802](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230816101802.png)

## 2.3、whereis命令

使用whereis也能查到其路径，但是和which不同的是它不但能找出其二进制文件，还能找出相关的man文件。

```shell
whereis passwd
```

![20230816101957](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230816101957.png)

# 三、网络故障排查

> 1. 确认网卡本身是否能够正常工作，127.0.0.1被称为主机的回环接口，是TCP/IP协议栈正常工作的前提。如果ping不通，一般可以证实为本机TCP/IP协议栈有问题。
>
> ```shell
> ping 127.0.0.1
> ```
>
> 2. 确认网卡是否出现了物理或驱动故障，使用ping本机IP的方式，如果能ping通则说明本地设备和驱动都正常。
> 3. 确认能否ping通同网段的其他主机。这一步主要确认二层网络设备（交换机、HUB等）工作是否正常。如果ping不通说明二层网络出现问题，可能涉及交换机的端口工作模式、vlan划分等因素。
> 4. 确认能否ping通网关IP，如果数据包能正常到达网关，则说明主机和本地网络都工作正常。
> 5. 确认能否ping通公网IP，如果可以则说明本地路由设置正确，否则需要确认路由设备的nat或路由设置是否正确。
> 6. 确认是否能够ping通公网上的某个域名，如果可以则说明DNS部分设置正确。