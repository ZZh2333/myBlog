# 一、CentOS添加用户并设置密码

```shell
# 切换到root用户
su root
# 添加用户，将USERNAME替换成想要创建的用户名
useradd USERNAME
# 设置密码，输入两边，将PASSWORD替换成想要设置的密码
echo 'PASSWORD' | passwd USERNAME --stdin
```

# 二、echo相关
-e参数表示启用转义字符。    
详细可参考[echo -e 命令详解](https://blog.csdn.net/qq_36412526/article/details/111411270)

```bash
# !/bin/bash
# This is my First shell
# By zzh
echo -e '\033[33m----------------------------------\033[0m'
FILE=httpd-2.2.31.tar.gz
URL=http://59.110.230.49/
PREFIX=/root/zzh/
echo -e "\033[36mPlease Select Install Menu:\033[0m"
echo "\033[36mPlease Select Install Menu:\033[0m"
echo
echo "1)官方下载Httpd文件包"
echo "2)解压Httpd源码包"
echo "3)编译安装Httpd服务器"
echo "4)启动Httpd服务器"
echo -e '\033[32m---------------------------------------\033[0m'
```

![20230811143627](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230811143627.png)

# 三、if else

赋值语句中“=”两边不能有空格。  
if后要有空格。  
引用赋值用“$”符号。  

```bash
NUM=1
if (($NUM>4)); then
    echo "The Num $NUM more than 4."
else
    echo "The Num $NUM less than 4."
fi
```

![20230811144405](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230811144405.png)

检查目录是否存在时，"[" 和 "]"中间需要添加一个空格。  
详细参考[-d:找不到命令](https://qa.1r1g.com/sf/ask/1593797341/)

```bash
if [ -d /root/zzh/zzh202308111424/ ]; then
    rm -rf ./zzh202308111424
else
    mkdir zzh202308111424
fi
```

“$1”表示命令中第一个参数

```bash
scores=$1
if [[ $scores -eq 100 ]]; then
    echo "very good!";
elif [[ $scores -gt 85 ]]; then
    echo "good!";
elif [[ $scores -gt 60 ]]; then
    echo "pass!";
elif [[ $scores -lt 60 ]]; then
    echo "no pass!"
fi

```

![20230811153837](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230811153837.png)

# 参考文献

[CentOS添加用户](https://www.python100.com/html/83367.html)  
[echo -e 命令详解](https://blog.csdn.net/qq_36412526/article/details/111411270)  
[-d:找不到命令](https://qa.1r1g.com/sf/ask/1593797341/)