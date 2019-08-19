# -*- encoding: utf-8 -*-
'''
@File : portscan.py
@Time : 2019/07/07 01:14:29
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''

from socket import *
import threading
from lib import *

threads = []
 
#端口扫描函数
def portScanner(host,port):
    try:
        port = int(port)
        s = socket(AF_INET,SOCK_STREAM)
        s.settimeout(1)
        result = s.connect((host,port))
        if result:
            pass
        else:
            print(Vcolors.RED + "发现开放端口，端口为:"+str(port) + Vcolors.ENDC)
        s.close()
    except :
        pass
        
 
def portScan(ip):
    print('\n')
    print(Vcolors.OKBLUE + "正在对目标常用端口探测~~" + Vcolors.ENDC)
    print(Vcolors.YELLOW + "检测中，请稍候~~" + Vcolors.ENDC)
    portll(ip)

def portll(ip):
    setdefaulttimeout(1)
    #扫描1-1024端口
    portList = ["21","22","23","80","161","389","443","445","512","513","514","873","1025","111","1433","1521","5560","7778","2601","2604","3128","3306","3312","3311","3389","4440","5432","5900","5984","6082","6379","7001","7002","7778","8000","8001","8080","8089","8090","9090","8083","8649","8888","9200","9300","10000","11211","27017","27018","28017","50000","50070","50030","33891"]
#    portList = ["80","443"]
    for p in portList:
        p= int(p)
        t = threading.Thread(target=portScanner,args=(ip,p))
        threads.append(t)
        t.start()     
 
    for t in threads:
        t.join()
