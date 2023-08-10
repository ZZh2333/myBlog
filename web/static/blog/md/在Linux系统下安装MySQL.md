# 一、查看是否已安装mysql

```shell
rpm -qa | grep mysql
```

![20230810135241](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230810135241.png)  

# 二、安装mysql

```shell
sudo apt update
sudo apt upgrade
sudo apt install mysql-server -y
```
  
# 三、mysql配置

## 3.1、启动mysql服务

```shell
sudo service mysql start
```

有时会出现以下警告  
![20230810141901](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230810141901.png)

处理方法

```shell
sudo service mysql stop
sudo usermod -d /var/lib/mysql/ mysql
sudo service mysql start
```

## 3.2、初始化配置

```shell
sudo mysql_secure_installation
```

![20230810142031](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230810142031.png)

## 3.3、测试登录

```shell
mysql -u root -p
```

按提示输入步骤二设置的密码即可登录，如果提示如下错误，  

![20230810142521](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230810142521.png)

可按如下步骤解决

> 1、停止mysql服务
>
> ```shell
> sudo service mysql stop
> ```
>
> 2、编辑配置文件，添加 skip-grant-tables 禁用登录校验，保存并退出vim。
>
> ```shell
> sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
> ```
>
> ![20230810142703](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230810142703.png)
> 3、启动mysql服务
>
> ```shell
> sudo service mysql start
> ```
>
> 4、登录mysql,由于已禁用密码校验，此时直接回车即可登录
>
> ```shell
> mysql –u root
> ```
>
> 5、查看root的验证方式， 如果是auth_socket则将其修改为mysql_native_password
>
> ```shell
> use mysql;
> ```
>
> ![20230810142835](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230810142835.png)
>
> ```sql
> update user set plugin='mysql_native_password' where user='root';
> flush privileges;
>
> ```
>
> ![20230810144228](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230810144228.png)
>
> 6、设置新密码
>
> ```sql
> update user set Host='%' where User='root';
> ALTER user 'root'@'%' IDENTIFIED BY 'root的新密码';
> flush privileges;
> ```
>
>![20230810154124](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230810154124.png)
>
> 7、退出MySQL
>
> ```sql
> quit
> ```
>
> 8、停止MySQL服务
>
> ```shell
> sudo service mysql stop
> ```
>
> 9、注释步骤2添加的skip-grant-tables，然后再启动mysql服务使用root登录测试新密码是否生效
>
> ```shell
>  sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
> ```
>
> ![20230810143155](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230810143155.png)
>
> ```shell
> sudo service mysql start
> mysql -u root -p
> ```

# 四、远程连接问题

将bind-address注释掉或改成0.0.0.0就行

```shell
cd /etc/mysql/mysql.conf.d
vim mysqld.cnf
```

重启mysql服务

```shell
sudo service mysql stop
sudo service mysql start
```

![20230810153533](https://raw.githubusercontent.com/ZZh2333/picgoResource/main/img/20230810153533.png)

# 参考文献

[Ubuntu(20.04)安装mysql8.0——知乎](https://zhuanlan.zhihu.com/p/525510043)  
[MySQL远程连接失败总结|Ubuntu——CSDN](https://blog.csdn.net/Pluton_1/article/details/128107753)  
[Linux 安装Mysql（图文教程）](https://zhuanlan.zhihu.com/p/404076008)