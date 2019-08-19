# -*- encoding: utf-8 -*-
'''
@File : tomcatexample.py
@Time : 2019/07/06 23:51:40
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''

import requests
from lib import *


def tomcatCheck(url2):
    print('\n')
    print(Vcolors.OKBLUE + "正在对目标url进行Apache样例文件泄露探测~~" + Vcolors.ENDC)
    exp = ['/examples/servlets/servlet/CookieExampleh', '/examples']
    payload = []
    for i in exp:
        s = url2 + i 
        payload.append(s)
    
    for url in payload:
        r = requests.get(url)
        if r.status_code==200:
            print(Vcolors.RED + "存在Apache样例文件泄露泄露漏洞，漏洞地址为:" + url + Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN + "不存在Apache样例文件泄露漏洞" + Vcolors.ENDC)