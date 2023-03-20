# 一、安装环境

## 1.安装环境依赖

```shell
sudo dpkg --add-architecture i386
sudo apt -y update
sudo apt -y upgrade

sudo apt -y install libsdl2-2.0-0:i386

sudo apt -y install curl wget file tar bzip2 gzip unzip bsdmainutils python util-linux ca-certificates binutils bc jq tmux netcat lib32gcc1 lib32stdc++6 screen
```

## 2.创建steamcmd文件夹

```shell
mkdir steamcmd
cd steamcmd
```

## 3.下载steamcmd

> 直接下载
>
> ```shell
> wget https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz
> ```
>
> 网盘下载  
> todo

## 4.解压steamcmd

```shell
tar -xvzf steamcmd_linux.tar.gz
```

## 5.进入steamcmd

```shell
./steamcmd.sh
```

# 二、安装游戏服务器

## 1.指定安装目录

```shell
force_install_dir ../vhserver
```

## 2.匿名登录

> 也可以用自己的账户登录，登录过程中输入的密码是看不见的，输完回车就行。

```shell
login anonymous
```

## 3.下载游戏

> 896660是英灵神殿服务器的代码，具体游戏代码查阅[第三部分](#ThirdPart)

```shell
app_update 896660
```

> 如果需要更新服务器则在后面加validate
>
> ```shell
> app_update 896660 validate
> ```

## 4.退出steamcmd

```shell
exit
```

# <a id="ThirdPart"></a>三、常用游戏服务器代码

查阅网址：[Steam 游戏信息整合查询](http://steamdb.sinaapp.com/)

# 参考文献

[[1]WeHao的博客](https://blog.wehaox.com/archives/3.html)