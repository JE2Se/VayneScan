# -*- encoding: utf-8 -*-
'''
@File : svn.py
@Time : 2019/07/05 16:59:36
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''

import requests
import re
from lib import *


def svnCheck(url2):
    try:
        print('\n')
        print(Vcolors.OKBLUE + "正在对目标url进行.SVN漏洞探测~~" + Vcolors.ENDC)
        default_url="/.svn/././././././././entries"
        ipList = []
        strList = []
        for i in url2:
            strList.append(i)
        a = strList.count('/')
        for i in range(a-2):
            url2 = url2[:url2.rfind("/")]
            ipList.append(url2+default_url)
        for url in ipList:
            r = requests.get(url,timeout = 3)
            print(r.status_code)
            if r.status_code!=200:
                print(Vcolors.OKGREEN + "不存在.SVN泄露漏洞" + Vcolors.ENDC)
            else:
                print(Vcolors.RED + "存在.SVN泄露漏洞，漏洞地址为:"+ url + Vcolors.ENDC)
    except:
        print(Vcolors.YELLOW+"疑似存在防火墙，链接已被拦截"+ Vcolors.ENDC)