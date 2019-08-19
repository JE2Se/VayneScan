# -*- encoding: utf-8 -*-
'''
@File : getip.py
@Time : 2019/07/05 14:53:32
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''

import dns.resolver
from bs4 import BeautifulSoup
import requests
from lib import *
import re

def ip2domain(ip):
    c = re.compile(r'^(((25[0-5]|2[0-4]\d|1\d{2})|([1-9]?\d))\.){3}((25[0-5]|2[0-4]\d|1\d{2})|([1-9]?\d))$')
    s = c.search(ip)
    if s:
        print('\n')
        print(Vcolors.OKBLUE + "正在对目标url进行归属地探测~~" + Vcolors.ENDC)
        matchIP (ip)
        print(Vcolors.OKGREEN + "具体命令请查看 '-h'~~~" + Vcolors.ENDC)
    else:
        print('\n')
        print(Vcolors.OKBLUE + "正在对目标url进行归属地探测~~" + Vcolors.ENDC)
        domainToip(ip)

def ipNew(old_ip):
    c = re.compile(r'^(((25[0-5]|2[0-4]\d|1\d{2})|([1-9]?\d))\.){3}((25[0-5]|2[0-4]\d|1\d{2})|([1-9]?\d))$')
    s = c.search(old_ip)
    if s:
        return old_ip
    else:
        domain = old_ip
        data = dns.resolver.query(domain,'A')
        for i in data.response.answer:
            for j in i.items:
                if j.rdtype == 1:
                    newip = j.address
                    return newip

def domainToip(old_ip):
    domain = old_ip
    data = dns.resolver.query(domain,'A')
    for i in data.response.answer:
        for j in i.items:
         if j.rdtype == 1:
            matchIP(j.address)

def matchIP (new_ip):
    url = "http://ip.tool.chinaz.com/"
    try:
        url = url+str(new_ip)
    except:
        pass
    wbdata = requests.get(url).text
    soup = BeautifulSoup(wbdata, 'lxml')
    for tag in soup.find_all('span', class_='Whwtdhalf w50-0'):
        tag_extractl = tag.get_text().encode('utf-8')
        if tag_extractl.find(b"IP\xe7\x9a\x84\xe7\x89\xa9\xe7\x90\x86\xe4\xbd\x8d\xe7\xbd\xae"):     #过滤掉【IP的物理位置】这个字符
            print(Vcolors.OKGREEN + '被测域名的IP为：' +new_ip+ '\n' +'被测域名的归属地为：'+ tag.get_text() + Vcolors.ENDC) 