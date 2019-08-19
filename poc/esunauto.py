# -*- encoding: utf-8 -*-
'''
@File : esunauto.py
@Time : 2019/07/15 11:00:45
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''

import requests
from lib import *

def elasticsearch(ip):
    print('\n')
    print(Vcolors.OKBLUE + "正在对目标url进行Elasticsearch未授权漏洞探测~~" + Vcolors.ENDC)
    try:
        port=9200
        url = ip+str(port)+"/_cat"
        response = requests.get(url,timeout=5) 
        if "/_cat/master" in response.content:
            print(Vcolors.RED + "存在Elasticsearch未授权漏洞" + Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN + "不存在Elasticsearch未授权漏洞" + Vcolors.ENDC)
    except:
        print(Vcolors.OKGREEN + "不存在Elasticsearch未授权漏洞" + Vcolors.ENDC)