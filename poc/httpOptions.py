# -*- encoding: utf-8 -*-
'''
@File : httpOptions.py
@Time : 2019/07/06 19:45:26
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''


import requests
from lib import *

def options(url):
    try:
        print('\n')
        print(Vcolors.OKBLUE + "正在对目标url进行不安全的HTTP请求探测~~" + Vcolors.ENDC)
        r = requests.options(url)
        s = r.headers['allow']
        if 'OPTIONS' in s:
            print(Vcolors.RED + "目标URL开启了OPTIONS请求~~" + Vcolors.ENDC)
        elif 'PUT' in s:
            print(Vcolors.RED + "目标URL开启了PUT请求~~" + Vcolors.ENDC)
        elif 'TRACE' in s:
            print(Vcolors.RED + "目标URL开启了TRACE请求~~" + Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN + "目标URL未开启不安全的HTTP请求~~" + Vcolors.ENDC)
    except:
        print(Vcolors.OKGREEN + "目标URL的HTTP请求不明~~" + Vcolors.ENDC)
