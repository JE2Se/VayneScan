# -*- encoding: utf-8 -*-
'''
@File : corscheck.py
@Time : 2019/07/06 22:42:55
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''
import requests
from lib import *

def corsCheck(url):
    try:
        print('\n')
        print(Vcolors.OKBLUE + "正在对目标url进行CORS跨域资源共享漏洞探测~~" + Vcolors.ENDC)
        orgin = 'www.je2se.com'
        headers = {
                    'Origin':orgin,
                    'Cache-Control':
                    'no-cache',
                    'User-Agent':
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
                }
        r = requests.get(url, headers = headers, timeout=10, allow_redirects=False)
        if r.headers['Access-Control-Allow-Origin'] == orgin and r.headers['Access-Control-Allow-Credentials'] == "true":
            print(Vcolors.RED + "存在CORS跨域资源共享漏洞" + Vcolors.ENDC)

        else:
            print(Vcolors.OKGREEN + "不存在CORS跨域资源共享漏洞" + Vcolors.ENDC)
    except Exception:
        print(Vcolors.OKGREEN + "不存在CORS跨域资源共享漏洞" + Vcolors.ENDC)
