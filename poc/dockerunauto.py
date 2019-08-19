# -*- encoding: utf-8 -*-
'''
@File : docker_unauthorized_access.py
@Time : 2019/08/03 23:03:54
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''


import socket
from lib import *


def dockercheck(ip):
    print('\n')
    print(Vcolors.OKBLUE + "正在对目标url进行Docker未授权访问漏洞探测~~" + Vcolors.ENDC)
    socket.setdefaulttimeout(2)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 2375))
        payload = "GET /containers/json HTTP/1.1\r\nHost: %s:%s\r\n\r\n" % (ip, 2375)
        s.send(payload.encode())
        recv = s.recv(1024)
        if b"HTTP/1.1 200 OK" in recv and b'Docker' in recv and b'Api-Version' in recv:
            print(Vcolors.RED + "存在Docker未授权访问漏洞"+ Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN + "不存在Docker未授权访问漏洞" + Vcolors.ENDC)
    except:
        print(Vcolors.OKGREEN + "不存在Docker未授权访问漏洞" + Vcolors.ENDC)
