# -*- encoding: utf-8 -*-
'''
@File : rsyncunauth.py
@Time : 2019/08/03 23:19:38
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''

from lib import *
import socket

timeout = 2


def rsyncheck(ip):
    print('\n')
    print(Vcolors.OKBLUE + "正在对目标url进行Rsync未授权访问漏洞探测~~" + Vcolors.ENDC)
    try:
        payload = b"\x40\x52\x53\x59\x4e\x43\x44\x3a\x20\x33\x31\x2e\x30\x0a"
        socket.setdefaulttimeout(timeout)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (ip, 873)
        sock.connect(server_address)
        sock.sendall(payload)
        initinfo = sock.recv(400)
        if "RSYNCD" in initinfo:
            sock.sendall(b"\x0a")
        modulelist = sock.recv(200)
        sock.close()
        if len(modulelist) > 0:
            print(Vcolors.RED + "存在Rsync未授权访问漏洞" + Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN + "不存在Rsync未授权访问漏洞" + Vcolors.ENDC)
    except:
        print(Vcolors.OKGREEN + "不存在Rsync未授权访问漏洞" + Vcolors.ENDC)
