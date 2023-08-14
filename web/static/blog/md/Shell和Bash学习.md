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
#!/bin/bash
#This is my First shell
#By zzh
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
#!/bin/bash
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
#!/bin/bash
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


# **四、exec命令参数**
exec命令参数能够在不创建新的子进程的前提下，转去执行指定的命令，当指定的命令执行完毕后，该进程（也就是最初的Shell）就终止了。  

```shell
exec date
```

![20230814151734](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230814151734.png)

当使用exec打开文件后，read命令每次都会将文件指针移动到文件的下一行进行读取，直至文件的末尾。利用这个特性可以实现处理文件内容。

```bash
#!/bin/bash
exec <./tmp.log
while read line
do
        echo $line
done
echo ok      
```

![20230814152539](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230814152539.png)

# 五、expr命令的使用
expr（evaluate expression 求值表达式）命令既可以用于整数计算，也可以用于相关字符串长度、匹配等的运算处理。

## 1、expr用于计算

+ 运算符及用于计算的数字左右都至少有一个空格。  
+ 使用乘号时，必须用反斜杠屏蔽其特定的含义，因为Shell可能会误解星号的含义。  

```shell
expr 2 + 2
expr 2 - 2
# *号需要用'\'来转义
expr 2 \* 2
expr 2 / 2
```

![20230814161716](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230814161716.png)

## 2、expr判断变量值或字符串是否为整数

```shell
i=5
# 把i和整数相加，&>/dev/null表示不保留任何输出。
expr $i + 6 &>/dev/null
# 输出上一次的返回值，若为0，则i为整数，反之i不为整数。
echo $i
```

![20230814163357](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230814163357.png)

## 3、expr判断文件扩展名是否符合要求

```bash
#!/bin/bash
if expr "$1" : ".*\.txt" &>/dev/null; then
        echo "you are using $1"
else
        echo "pls use *.txt file"
fi
```

![20230814164556](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230814164556.png)


## 4、通过expr计算字符串长度

```shell
char="I am a robot"
#利用expr的length函数计算字符长度
expr length "$char"
#计算变量字串长度的方法
echo ${#char}
#wc方法
echo ${char}|wc -L
#利用awk的length函数来计算字符串长度
echo ${char}|awk '{print length($0)}'
```

![20230814170408](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230814170408.png)

# 参考文献

[CentOS添加用户](https://www.python100.com/html/83367.html)  
[echo -e 命令详解](https://blog.csdn.net/qq_36412526/article/details/111411270)  
[-d:找不到命令](https://qa.1r1g.com/sf/ask/1593797341/)