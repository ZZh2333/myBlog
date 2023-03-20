> 客护端安装登录可以直接跳转到 [第三部分](#Thirdpart)
# 一、服务器环境搭建
### 1.将系统环境更换为Windows Server 2019 数据中心版
### 2.开启ssh server服务
![冒险岛OnLine2023-03-20-09-58-52](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/%E5%86%92%E9%99%A9%E5%B2%9BOnLine2023-03-20-09-58-52.png)  
![冒险岛OnLine2023-03-20-09-59-43](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/%E5%86%92%E9%99%A9%E5%B2%9BOnLine2023-03-20-09-59-43.png)  
安装完成后，启动ssh服务
```shell
net start sshd
```
### 3.传输服务器文件，下载服务端.rar
> 链接：https://pan.baidu.com/s/1tVgJmM5LkPG4qxjS0vhT4A   
> 提取码：suob 
# 二、搭建服务器端
### 1.运行「服务端目录\mSer\Mysql\phpStudy.exe」，注意phpStudy.exe所在路径不能有中文。点启动，两个绿点表示运行正常。
![冒险岛OnLine2023-03-20-10-01-54](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/%E5%86%92%E9%99%A9%E5%B2%9BOnLine2023-03-20-10-01-54.png)  
### 2.运行「服务端目录\mSer\第二步 启动服务端.exe」，点击启动服务端，在弹出的「Gui控制台」中再次点击「启动服务端」，等黑色控制台窗口显示开端成功。这个窗口只能最小化！不能关掉！
![冒险岛OnLine2023-03-20-10-02-19](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/%E5%86%92%E9%99%A9%E5%B2%9BOnLine2023-03-20-10-02-19.png)
# <a id="Thirdpart"></a>三、客户端安装
### 1. 下载除服务端.rar以外的所有内容
> 链接：https://pan.baidu.com/s/1tVgJmM5LkPG4qxjS0vhT4A   
> 提取码：suob 
### 2.双击「079客户端」安装游戏
### 3.将「补丁1.5m」移动到游戏目录并安装
### 4.解压「WIN10专用HShield」，以其中的「HShield」文件夹替换游戏原本的HShield，并将ehsvc.ini中的路径改为
> [ 你的游戏安装目录 ]\冒险岛online\Maplestory.exe
### 5.解压「dlp」到游戏目录\冒险岛online文件夹里，此为登录器
### 6.右键以管理员权限运行【豆豆冒险岛联机登录器V079.exe】
### 7.输入服务器IP连接即可  (47.113.201.210)
> 首次登录用户无需注册，直接输入需要注册的账号密码即可注册登录

# 参考文献
[[1]冒险岛079单机/小范围联机游戏搭建](https://blog.csdn.net/XenonL/article/details/104203356)