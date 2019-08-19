# -*- encoding: utf-8 -*-
'''
@File : solrunautho.py
@Time : 2019/08/03 23:12:13
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com

Apache Solr 未授权访问PoC
'''
from  lib import * 
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def apachesolr(url):
  print('\n')
  print(Vcolors.OKBLUE + "正在对目标url进行Apache Solr 未授权访问漏洞探测~~" + Vcolors.ENDC)
  try:
    url = url + '/solr/'
    g = requests.get(url, timeout=5, verify=False)
    if g.status_code is 200 and 'Solr Admin' in g.content and 'Dashboard' in g.content:
      print(Vcolors.RED +  "存在Apache Solr 未授权访问漏洞" + Vcolors.ENDC)
    else:
      print(Vcolors.OKGREEN +  "不存在Apache Solr 未授权访问漏洞" + Vcolors.ENDC)
  except :
    print(Vcolors.OKGREEN +  "不存在Apache Solr 未授权访问漏洞" + Vcolors.ENDC)
