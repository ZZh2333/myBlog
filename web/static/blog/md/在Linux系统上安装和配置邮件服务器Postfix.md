# 一、Postfix安装

```shell
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install postfix
```

安装完成后，会提示您选择邮件服务器配置类型。  
选择“Internet Site”并按照提示进行设置名称（目前未知名称作用）。  
完成安装后，接下来需要进行一些配置以确保邮件服务器能够正常运行。  

首先，打开Postfix的主配置文件：  

```shell
sudo vim /etc/postfix/main.cf
```

以下是一些常用的配置选项示例：  

```shell
myhostname = yourdomain.com
mydomain = yourdomain.com
myorigin = $mydomain
inet_interfaces = all
inet_protocols = all
mynetworks_style = subnet
mynetworks = 192.168.0.0/24
```

在上述示例中，将“yourdomain.com”替换为您拥有的域名，并根据需要进行其他更改。  
保存并关闭文件后，重新启动Postfix以使更改生效：

```shell
sudo systemctl restart postfix
```