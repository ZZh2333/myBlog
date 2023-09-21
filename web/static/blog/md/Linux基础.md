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

# 四、top命令详解

![20230816135200](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230816135200.png)

> 1. 第一行为服务器基础信息，包括top命令的刷新时间为13:51:55，系统已经运行5天21分钟，当前有一个用户登录，系统的负载（load average）为：最近1分钟内的平均系统负载为0.05，最近5分钟内的平均系统负载为0.01，最近15分钟内的平均系统负载为0.05。
> 2. 第二行是当前系统进程概况，一共有83个进程，其中1个正在运行，82个处于休眠状态，没有停止的进程，没有讲时进程。
> 3. 第三行是CPU信息，us代表用户空间占用的CPU百分比，sy代表内核空间占用的CPU百分比，ni代表改变过优先级的进程占用的CPU百分比，id代表空闲CPU百分比，wa代表I/O等待百分比，hi代表硬中断占用的CPU百分比，si代表软中断占用的CPU百分比。对于多核CPU，可以在top显示界面中按数字键1查看每个逻辑CPU的使用情况。
> 4. 第四行是物理内存的使用情况，从左到右分别表示物理内存总量、已使用内存、空闲内存、缓存使用的内存。
> 5. 第五行是虚拟内存的使用状态，前三个与物理内存相同，最后一个代表缓冲区的交换区总量。

进程信息区中的信息默认显示11个字段，按f可以自行勾选想要显示的字段。  
默认情况top现实的进程是按照CPU使用率来进行排序的，按大写字母O可以进入排序选择页。

|字段|含义|
|---|---|
|PID|进程id|
|USER|进程所有者|
|PR|进程优先级|
|NI|nice值，负值表示高优先级，正值表示低优先级|
|VIRT|进程使用的虚拟内存总量，单位为Kb，VIRT=SWAP+RES|
|RES|进程使用的未被换出的物理内存大小，单位为Kb，RES=CODE+DATA|
|SHR|共享内存大小，单位为Kb|
|%CPU|上次更新到现在的CPU时间占用百分比|
|%MEM|进程使用的物理内存百分比|
|TIME+|进程使用的CPU时间总计，单位为1/100秒|
|COMMAND|进程名称（命令名/命令行）|

# 五、kill命令

kill语法

```shell
#kill [信号代码] 进程ID
kill -9 2877
```

kill后可以跟的信号代码一共有64中，使用kill -l可以查看。  
常用信号代码为HUP(1)、KILL(9)、TERM(15)。分别代表重启、强行杀掉、正常结束。  
不加信号代码的命令默认为TERM(15)，即缓和关闭。

![20230816143343](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230816143343.png)

由于使用kill命令时要先查询到进程PID，如果杀错PID后果**不堪设想**。事实上更多的使用killall命令，它可以直接使用进程的名字而非PID。killall命令更加**简单、安全**。例如停止系统中所有的httpd进程。

```shell
killall httpd
```

#  六、Crontab命令详解

crontab命令常见于Unix和类Unix的操作系统之中，用于设置周期性被执行的指令。  
该命令从标准输入设备读取指令，并将其存放于“crontab”文件中（是“cron table”的简写），以供之后读取和执行。
通常，crontab储存的指令被守护进程激活，crond常常在后台运行，每一分钟检查是否有预定的作业需要执行。这类作业一般称为cron jobs。

## 6.1、Crontab检查及安装

下面的命令 如果显示 ‘no crontab for root’ 或者 显示当前的任务列表 或者 不报错 那说明已经安装，

```shell
crontab -l
```

![20230817090515](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230817090515.png)

### 6.1.1、安装cron服务

CentOs

```shell
yum -y install vixie-cron crontabs
```

Ubuntu

```shell
apt-get install cron
```

### 6.1.2、cron服务的启动与关闭

CentOs

```shell
#查看cron状态
service crond status

#启动cron
service crond start

#关闭cron
service crond stop

#重启cron
service crond restart
```

Ubuntu

```shell
#查看cron状态
service cron status

#启动cron
service cron start

#关闭cron
service cron stop

#重启cron
service cron restart
```

## 6.2、crontab命令

### 6.2.1、命令格式

```shell
crontab [-u user] file
crontab [-u user] [ -e | -l | -r ]
```

### 6.2.2、命令功能

通过crontab 命令，我们可以在固定的间隔时间执行指定的系统指令或 shell script脚本。时间间隔的单位可以是分钟、小时、日、月、周及以上的任意组合。这个命令非常设合周期性的日志分析或数据备份等工作。

### 6.2.3、命令参数

-u user：用来设定某个用户的crontab服务，例如，“-u ixdba”表示设定ixdba用户的crontab服务，此参数一般有root用户来运行。
file：file是命令文件的名字,表示将file做为crontab的任务列表文件并载入crontab。如果在命令行中没有指定这个文件，crontab命令将接受标准输入（键盘）上键入的命令，并将它们载入crontab。
-e：编辑某个用户的crontab文件内容。如果不指定用户，则表示编辑当前用户的crontab文件。
-l：显示某个用户的crontab文件内容，如果不指定用户，则表示显示当前用户的crontab文件内容。
-r：从/var/spool/cron目录中删除某个用户的crontab文件，如果不指定用户，则默认删除当前用户的crontab文件。
-i：在删除用户的crontab文件时给确认提示。

### 6.2.4、crontab文件格式

每一行都代表一项任务，每行的每个字段代表一项设置，它的格式共分为六个字段，前五段是时间设定段，第六段是要执行的命令段，格式如下：

```shell
minute   hour   day   month   week   command
# For details see man 4 crontabs
# Example of job definition:
.---------------------------------- minute (0 - 59) 表示分钟
|  .------------------------------- hour (0 - 23)   表示小时
|  |  .---------------------------- day of month (1 - 31)   表示日期
|  |  |  .------------------------- month (1 - 12) OR jan,feb,mar,apr ... 表示月份
|  |  |  |  .---------------------- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat  表示星期（0 或 7 表示星期天）
|  |  |  |  |  .------------------- username  以哪个用户来执行 
|  |  |  |  |  |            .------ command  要执行的命令，可以是系统命令，也可以是自己编写的脚本文件
|  |  |  |  |  |            |
*  *  *  *  * user-name  command to be executed
```

### 6.2.5、格式示例

|格式|说明|
|--|--|
|*/1 * * * * service httpd restart|每一分钟 重启httpd服务|
|0 */1 * * * service httpd restart|每一小时 重启httpd服务|
|30 21 * * * service httpd restart|每天 21：30 分 重启httpd服务|
|26 4 1,5,23,28 * * service httpd restart|每月的1号，5号 23 号 28 号 的4点26分，重启httpd服务|
|26 4 1-21 * * service httpd restart|每月的1号到21号 的4点26分，重启httpd服务|
|*/2 * * * * service httpd restart|每隔两分钟 执行，偶数分钟 重启httpd服务|
|1-59/2 * * * * service httpd restart|每隔两分钟 执行，奇数 重启httpd服务|
|0 23-7/1 * * * service httpd restart|每天的晚上11点到早上7点 每隔一个小时 重启httpd服务|
|0,30 18-23 * * * service httpd restart|每天18点到23点 每隔30分钟 重启httpd服务|
|0-59/30 18-23 * * * service httpd restart|每天18点到23点 每隔30分钟 重启httpd服务|
|59 1 1-7 4 * test 'date +\%w' -eq 0 && /root/a.sh|四月的第一个星期日 01:59 分运行脚本 /root/a.sh ，命令中的 test是判断，%w是数字的星期几|

### 6.2.6、小结

+ *表示任何时候都匹配
+ "a,b,c" 表示a 或者 b 或者c 执行命令
+ "a-b" 表示a到b 之间 执行命令
+ "*/a" 表示每 a分钟(小时等) 执行一次
+ crontab 不能编辑系统级的 任务

## 6.3、crontab的配置文件

|文件|说明|
|--|--|
|/etc/crontab|全局配置文件|
|/etc/cron.d|这个目录用来存放任何要执行的crontab文件或脚本|
|/etc/cron.deny|该文件中所列用户不允许使用crontab命令|
|/etc/cron.allow|该文件中所列用户允许使用crontab命令|
|/var/spool/cron/|所有用户crontab文件存放的目录,以用户名命名，比如你是root 用户，那么当你添加任务是，就会在该路径下有一个root文件。|
|/etc/cron.deny|该文件中所列用户不允许使用crontab命令|
|/var/log/cron|crontab 的日志文件|

## 6.4、注意事项

### 6.4.1、环境变量

环境变量的值，在crontab 文件中获取不到，所以要注意，可以写脚本。

### 6.4.2、%

在crontab中%是有特殊含义的，表示换行的意思。如果要用的话必须进行转义\%

```shell
`59 1 1-7 4 * test 'date +\%w' -eq 0 && /root/a.sh `
```


# 7、ssh配置免密登录（A服务器免密登录B服务器）

## 7.1、生成密钥对

```shell
ssh-keygen -t rsa
```
在询问“Enter file in which to save the key (/home/ubuntu/.ssh/id_rsa):”时可以填写需要生成密钥对的名称，以便区分不同的密钥对对应不同登录的服务器。

![20230920150529](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230920150529.png)

![20230920150649](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230920150649.png)

## 7.2、将服务器A上的公钥复制到服务器B上的authorized_keys文件。可以使用ssh-copy-id 命令来完成此操作

该步需要输入一次B服务器的登陆密码

```shell
ssh-copy-id -i id_rsa.pub user_B@server_B
```

[ssh免密配置失败原因排查](https://blog.csdn.net/zhangmingcai/article/details/95734889)

# 参考文献

[Crontab命令详解](https://blog.csdn.net/qq_32923745/article/details/78286385)