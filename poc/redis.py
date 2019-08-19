# -*- encoding: utf-8 -*-
'''
@File : redis.py
@Time : 2019/07/06 21:22:47
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''


import socket
import sys
from lib import *

PASSWORD_DIC=['redis','root','oracle','password','p@aaw0rd','abc123!','123456','admin']

def redisCheck(ip):
    try:
        print('\n')
        print(Vcolors.OKBLUE + "正在对目标url进行Redis未授权访问漏洞探测~~" + Vcolors.ENDC)
        socket.setdefaulttimeout(4)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = '6379'
        s.connect((ip, int(port)))
        exp = b'*1\r\n$4\r\ninfo\r\n'
        s.send(exp)
        result = s.recv(1024)
        if b"redis_version" in result:
            print(Vcolors.RED + "存在Redis未授权访问漏洞" + Vcolors.ENDC)
        elif b"Authentication" in result:
            for pass_ in PASSWORD_DIC:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, int(port)))
                s.send("AUTH %s\r\n" %(pass_))
                result = s.recv(1024)
                if '+OK' in result:
                    print(Vcolors.YELLOW +"存在弱口令，密码：%s" % (pass_) + Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN + "不存在Redis未授权访问漏洞" + Vcolors.ENDC)

    except:
        print(Vcolors.OKGREEN + "不存在Redis未授权访问漏洞" + Vcolors.ENDC)