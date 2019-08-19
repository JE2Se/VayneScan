# -*- encoding: utf-8 -*-
'''
@File : main.py
@Time : 2019/07/06 01:14:49
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''

from app.platform import ManageProcessor
from lib import *

def weblogicScan(ip,port):
        processor = ManageProcessor()
#        processed = processor.process(ip,port)
        processor.process(ip,port)