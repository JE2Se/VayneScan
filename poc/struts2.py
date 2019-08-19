# -*- encoding: utf-8 -*-
'''
@File : struts2.py
@Time : 2019/08/03 22:22:16
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''

from lib import *
from app2.s2_006 import s2_006
from app2.s2_009 import s2_009
from app2.s2_013 import s2_013
from app2.s2_016 import s2_016
from app2.s2_016_2 import s2_016_2
from app2.s2_019 import s2_019
from app2.s2_032 import s2_032
from app2.s2_045 import s2_045
from app2.s2_052 import s2_052
from app2.s2_053 import s2_053
from app2.s2_057 import s2_057
from app2.s2_dev import s2_dev

def StrutsCheck(url):
    print('\n')
    print(Vcolors.OKBLUE + "正在对目标url进行Struts漏洞探测~~" + Vcolors.ENDC)
    s2_006(url)
    s2_009(url)
    s2_013(url)
    s2_016(url)
    s2_016_2(url)
    s2_019(url)
    s2_032(url)
    s2_045(url)
    s2_052(url)
    s2_053(url)
    s2_057(url)
    s2_dev(url)