# -*- encoding: utf-8 -*-
'''
@File : jenkinsunauto.py
@Time : 2019/08/03 22:55:20
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''


import requests
from lib import *
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def jenkins(url):
    print('\n')
    print(Vcolors.OKBLUE + "正在对目标url进行Jenkins未授权漏洞探测~~" + Vcolors.ENDC)
    try:
        payload = "/securityRealm/user/admin/descriptorByName/org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition/checkScriptCompile"
        r = requests.get(url + payload, timeout=5, verify=False)
        if 'java.lang.NullPointerException' in r.text:  
            print(Vcolors.RED +  "存在Jenkins未授权漏洞" + Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN +  "不存在Jenkins未授权漏洞" + Vcolors.ENDC)
    except:
        print(Vcolors.OKGREEN +  "不存在Jenkins未授权漏洞" + Vcolors.ENDC)