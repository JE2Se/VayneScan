# -*- encoding: utf-8 -*-
'''
@File : VayneScan.py
@Time : 2019/08/19 13:46:14
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''


from urllib.parse import urlparse
from script import *
from poc import *
from lib import *
import pyfiglet
import argparse
import sys
import time
from socket import *

if sys.version_info.major < 3:
    sys.stdout.write("Sorry, VayneScan requires Python 3.x\n")

if __name__ == "__main__":
    try:
        #头部信息部分
        ascii_banner = pyfiglet.figlet_format("VayNe.Scan")
        print(Vcolors.OKGREEN + ascii_banner)
        print(Vcolors.OKBLUE + "\t\t\t\tPower by JE2Se" +"   "+ Vcolors.RED + "V1.1" +"\n" +Vcolors.ENDC)
        parser = argparse.ArgumentParser()
        #脚本执行帮助部分
        print(Vcolors.PURPLE + "\t\t~请输入 -h 获取命令帮助~" + "\n" + Vcolors.ENDC + Vcolors.OKGREEN)
        parser.add_argument("-u", "--url", help = '添加 -u 参数，指定待测的地址，请务必添加  "http(s)://"   ~~')
        parser.add_argument("-a", "--auto", help = '添加 -a 参数，将默认执行所有漏洞的检测  ~~', action='store_true')
        parser.add_argument("-s", "--struts", help = '添加 -s 参数，将进行struts漏洞检测  ~~', action='store_true')
        parser.add_argument("-w", "--weblogic", help = '添加 -w 参数，将进行weblogic漏洞检测  ~~', action='store_true')
        parser.add_argument("-l", "--leak", help = '添加 -l 参数，将仅检测泄露漏洞，如.git漏洞，.svn漏洞等等  ~~',action='store_true')
        parser.add_argument("-p", "--port", help = '添加 -p 参数，将仅检测开放的风险端口，如22，23，3389，445等  ~~',action='store_true')
        parser.add_argument("-d", "--dir", help = '添加 -d 参数，将仅对目标URL进行敏感目录探测  ~~',action='store_true')
        parser.add_argument("-v", "--vuln", help = '添加 -v 参数，将仅对目标URL进行WEB，主机，中间件漏洞探测  ~~',action='store_true')
        parser.add_argument("-q", "--questions", help = '添加 -q 参数，对部分漏洞进行解释说明  ~~',action='store_true')
        #取参赋值部分
        args = parser.parse_args()
        params = vars(args)
        if args.url:
            url1 = urlparse(args.url)
            domain = args.url
            domainorip = url1.netloc
            url = domainorip.split(':')[0]
            potorl = url1.scheme      #        params=url1.params
            path = url1.path          #        query=url1.query
            port = url1.port          #        fragment=url1.fragment
            urlAll = potorl + '://' + domainorip  + path[:path.rfind("/")] + '/'   # https://ip/path/
            newurl = potorl + '://' + url 
            ip = ipNew(url)
            #https://www.je2se.com/search.php\?id\=1

            #  urlall :  https://www.je2se.com/
            #  ip :  121.42.119.195
            #  domain :  https://www.je2se.com/search.php?id=1
            #  newurl :  https://www.je2se.com
        
            #攻击部分
#            print(urlAll)
            ip2domain(url)

            if args.auto:    #全部POC执行
                svnCheck(urlAll)
                gitCheck(urlAll)
                dsCheck(urlAll)
                thinkphp(urlAll)
                options(urlAll)
                redisCheck(ip)
                corsCheck(urlAll)
                httpsys(urlAll)
                hostinject(domain)
                tomcatCheck(newurl)
                portScan(ip)
                dirburte(newurl)
                elasticsearch(newurl)
                esCheck(newurl)
                jenkins(urlAll)
                dockercheck(ip)
                apachesolr(urlAll)
                rsyncheck(ip)
                StrutsCheck(domain)
                print("\n")
                print(Vcolors.OKBLUE + "正在对目标url进行Weblogic漏洞探测~~" + Vcolors.ENDC)
                s = socket(AF_INET,SOCK_STREAM)
                s.settimeout(2)
                try:
                    result = s.connect((ip,7001))
                    if result:
                        print(Vcolors.OKGREEN + "目标未开放weblogic服务，为防止端口被修改，请手动测试~" + Vcolors.ENDC)   
                    else:
                        weblogicScan(ip,port=7001) 
                    print('\n' + Vcolors.YELLOW + '漏洞检测结束~~~' + Vcolors.ENDC)  
                    s.close()
                except:
                    print(Vcolors.OKGREEN + "目标未开放weblogic服务，为防止端口被修改，请手动测试~" + Vcolors.ENDC)                
                
            
            if args.leak:   #泄露类POC执行
                svnCheck(urlAll)
                gitCheck(urlAll)
                dsCheck(urlAll)
                print('\n' + Vcolors.YELLOW + '信息泄露检测结束~~~' + Vcolors.ENDC)
            
            
            if args.port:   #端口类POC执行
                portScan(ip)
                print('\n' + Vcolors.YELLOW + '风险端口检测结束~~~' + Vcolors.ENDC)
            
            
            if args.dir:  #目录破解POC执行
                tomcatCheck(newurl)
                dirburte(newurl)
                print('\n' + Vcolors.YELLOW + '风险目录/文件检测结束~~~' + Vcolors.ENDC)
            
            
            if args.vuln:    #漏洞扫描POC执行
                thinkphp(urlAll)
                redisCheck(ip)
                corsCheck(urlAll)
                options(urlAll)
                httpsys(urlAll)
                hostinject(domain)
                elasticsearch(newurl)
                esCheck(newurl)
                jenkins(urlAll)
                dockercheck(ip)
                apachesolr(urlAll)
                rsyncheck(ip)
            
            if args.weblogic:   #weblogic检测模块
                print("\n")
                print(Vcolors.OKBLUE + "正在对目标url进行Weblogic漏洞探测~~" + Vcolors.ENDC)
                s = socket(AF_INET,SOCK_STREAM)
                s.settimeout(2)
                try:
                    result = s.connect((ip,7001))
                    if result:
                        print(Vcolors.OKGREEN + "目标未开放weblogic服务，为防止端口被修改，请手动测试~" + Vcolors.ENDC)   
                    else:
                        weblogicScan(ip,port=7001) 
                    print('\n' + Vcolors.YELLOW + '漏洞检测结束~~~' + Vcolors.ENDC)  
                    s.close()
                except:
                    print(Vcolors.OKGREEN + "目标未开放weblogic服务，为防止端口被修改，请手动测试~" + Vcolors.ENDC)

            
            if args.struts:
                StrutsCheck(domain)
                print('\n' + Vcolors.YELLOW + '漏洞检测结束~~~' + Vcolors.ENDC) 

        if args.questions:
            print('\n' + Vcolors.RED + 'Weblogic目前仅支持7001，7002端口，如已修改需要改源码' + Vcolors.ENDC) 
            print(Vcolors.RED + '端口扫描仅扫描未修改的风险端口' + Vcolors.ENDC)
            print(Vcolors.RED + '部分SSL协议异常未解决' + Vcolors.ENDC) 
            print(Vcolors.RED + '部分struts没有环境，直接按照poc去写的，不知道有无问题' + Vcolors.ENDC)  
        
    except Exception as e:
        pass
    