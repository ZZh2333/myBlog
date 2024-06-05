# WinRM是一种基于Web服务的协议，允许系统管理员通过远程计算机管理Windows系统  

## 1.启用WinRM服务  

```shell
winrm quickconfig
```

系统会提示确认操作并进行必要配置。按提示完成操作。

## 2.配置防火墙  

需要开放5985（http）、5986（https）端口

## 3.配置WinRM监听器  

配置WinRM监听器，使其监听指定的IP地址和端口。可以使用以下命令配置HTTP和HTTPS监听器：

```shell
# 配置HTTP监听器
winrm create winrm/config/Listener?Address=*+Transport=HTTP

# 配置HTTPS监听器（需要证书）
# 生成证书示例（使用自签名证书）
$cert = New-SelfSignedCertificate -DnsName "yourdomain.com" -CertStoreLocation "Cert:\LocalMachine\My"
$thumbprint = $cert.Thumbprint
winrm create winrm/config/Listener?Address=*+Transport=HTTPS @{Hostname="yourdomain.com";CertificateThumbprint=$thumbprint}

```

## 4.设置信任主机

在客户端计算机上，配置WinRM以信任目标服务器。以管理员身份打开PowerShell，然后运行：

```shell
Set-Item wsman:\localhost\Client\TrustedHosts "remote_server_ip_or_name"
```

## 5.启用Basic身份验证

如果目标服务器在没有域的工作组环境中，可能需要启用Basic身份验证。请注意，启用Basic身份验证时需要配置HTTPS以确保凭据的安全传输。

在目标服务器上以管理员身份打开PowerShell并运行以下命令：

```shell
# 启用Basic身份验证
Set-Item -Path WSMan:\localhost\Service\Auth\Basic -Value $true

# 允许未加密的连接（仅在测试环境中使用，在生产环境中使用HTTPS）
Set-Item -Path WSMan:\localhost\Service\AllowUnencrypted -Value $true
```

## 6.验证配置

在客户端计算机上，以管理员身份打开PowerShell并测试连接：

```shell
Test-WsMan remote_server_ip_or_name
```

如果配置正确，你应该会看到有关WinRM服务的信息。

## 7.使用WinRM进行远程管理

配置完成后，可以使用WinRM进行远程管理。例如，使用PowerShell进行远程命令执行：

```shell
$session = New-PSSession -ComputerName "remote_server_ip_or_name" -Credential (Get-Credential)
Invoke-Command -Session $session -ScriptBlock { Get-Process }
Remove-PSSession -Session $session

```