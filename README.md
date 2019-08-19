# README

## 简介：

<b>平时的测试总是千篇一律，对于很多的小检测项还要一项一项的检测，正好学习python，写写工具练练手，持续更新~</b><br>
## 说明

脚本使用Python3编写

## 使用方法

### 安装依赖
<code>python3 -m pip install -r requirements.txt<br></code>

### 用法

<code>python3 VayneScan.py -h 获取使用方法<br></code>

![image](https://github.com/JE2Se/VayneScan/raw/master/2.png)

## 本脚本目前集成了以下poc

IP地址探测<br>
.GIT信息泄露<br>
.SVN信息泄露<br>
.DS_Store信息泄露<br>
Weblogic漏洞扫描<br>
ThinkPHP漏洞<br>
不安全的HTTP请求<br>
RIDES未授权访问<br>
CORS跨域资源共享<br>
HTTP.sys远程命令执行漏洞<br>
Apache样例文件泄露<br>
敏感目录/文件爆破<br>
风险端口探测<br>
主机头攻击<br>
Host头注入<br>
ElasticSearch漏洞<br>
Struts漏洞<br>
Jenkins未授权访问漏洞<br>
Docker未授权访问漏洞<br>
Apache Solr 未授权访问漏洞<br>
Rsync未授权访问漏洞<br>

## 扩展性

可自行进行扩充，在主文件VayneScan.py进行导入执行函数。<br>

## 说明

脚本内小部分漏洞的poc使用了其他大佬现成的脚本<br>
weblogic利用，大佬们写的非常好，向大佬学习<br>
引用地址：https://github.com/rabbitmask/WeblogicScan<br>


## 问题

依赖不知道都写全了没，提示的再手动安装<br>
ssl协议问题有的没处理，会报错异常，没时间弄，后期修改<br>

## 时间

2019-08-04 01:27:41

