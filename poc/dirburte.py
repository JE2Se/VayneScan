# -*- encoding: utf-8 -*-
'''
@File : dirburte.py
@Time : 2019/07/07 00:19:28
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''


import requests
from lib import *
from socket import *
import threading

threads = []

def dirburte1(url2,path):
    s = url2 + path
    try:
        r = requests.get(s)
        if r.status_code == 200 or r.status_code == 302:
            print(Vcolors.RED + "发现风险目录/文件，地址为：" + s + Vcolors.ENDC)
        else:
            pass
    except:
        print(Vcolors.YELLOW+"疑似存在防火墙，链接已被拦截"+ Vcolors.ENDC)
        pass

def dirburte(ip):
    print('\n')
    print(Vcolors.OKBLUE + "正在对目标url进行目录/文件泄露探测~~" + Vcolors.ENDC)
    print(Vcolors.YELLOW + "检测中，请稍候~~" + Vcolors.ENDC)
    dirl(ip)

def dirl(ip):
    setdefaulttimeout(1)
    #扫描1-1024端口
    exp = ["/robots.txt", "/README.md", "/crossdomain.xml",
            "/.hg","/CVS/Root", "/CVS/Entries", "/.idea/workspace.xml",
            "/nginx_status", "/.mysql_history", "/login/", "/phpMyAdmin",
            "/pma/", "/pmd/", "/SiteServer", "/admin/", "/Admin/", "/manage",
            "/manager/", "/manage/html", "/resin-admin", "/resin-doc",
            "/axis2-admin", "/admin-console", "/system", "/wp-admin",
            "/uc_server", "/debug", "/Conf", "/webmail", "/service",
            "/memadmin", "/owa", "/harbor", "/master", "/root", "/xmlrpc.php",
            "/phpinfo.php", "/zabbix", "/api", "/backup", "/inc",
            "/web.config", "/httpd.conf", "/local.conf", "/sitemap.xml",
            "/app.config", "/.bash_history", "/.rediscli_history", "/.bashrc",
            "/.history", "/nohup.out", "/.mysql_history", "/server-status",
            "/solr/", "/examples/","/examples/servlets/servlet/SessionExample", "/manager/html",
            "/login.do", "/config/database.yml", "/database.yml", "/db.conf",
            "/db.ini", "/jmx-console/HtmlAdaptor", "/cacti/",
            "/jenkins/script", "/memadmin/index.php", "/pma/index.php",
            "/phpMyAdmin/index.php", "/.git/HEAD", "/.gitignore",
            "/.ssh/known_hosts", "/.ssh/id_rsa", "/id_rsa",
            "/.ssh/authorized_keys", "/app.cfg", "/.mysql.php.swp",
            "/.db.php.swp", "/.database.php.swp", "/.settings.php.swp",
            "/.config.php.swp", "/config/.config.php.swp","/html.rar",
            "/.config.inc.php.swp", "/config.inc.php.bak", "/php.ini","/pwd.rar",
            "/sftp-config.json", "/WEB-INF/web.xml","/www.rar","/www.zip","/www.tar.gz",
            "/WEB-INF/web.xml.bak", "/WEB-INF/config.xml",
            "/WEB-INF/struts-config.xml", "/server.xml","/1.rar","/1.zip","/modules/ssl.zip","/www.war","/shell.war","/1.war",
            "/config/database.yml", "/WEB-INF/database.properties",
            "/WEB-INF/log4j.properties", "/WEB-INF/config/dbconfig",
            "/fckeditor/_samples/default.html", "/ckeditor/samples/",
            "/ueditor/ueditor.config.js",
            "/javax.faces.resource...%2fWEB-INF/web.xml.jsf", "/wp-config.php",
            "/configuration.php", "/sites/default/settings.php", "/config.php",
            "/config.inc.php", "/data/config.php", "/data/config.inc.php",
            "/data/common.inc.php", "/include/config.inc.php",
            "/WEB-INF/classes/", "/WEB-INF/lib/", "/WEB-INF/src/", "/.bzr",
            "/SearchPublicRegistries.jsp", "/.bash_logout",
            "/resin-doc/resource/tutorial/jndi-appconfig/test?inputFile=/etc/profile",
            "/test2.html", "/conf.ini", "/index.tar.tz", "/index.cgi.bak",
            "/WEB-INF/classes/struts.xml", "/package.rar",
            "/WEB-INF/applicationContext.xml", "/mysql.php", "/apc.php",
            "/zabbix/", "/script", "/editor/ckeditor/samples/", "/upfile.php",
            "/conf.tar.gz",
            "/WEB-INF/classes/conf/spring/applicationContext-datasource.xml",
            "/output.tar.gz", "/.vimrc", "/INSTALL.TXT", "/pool.sh",
            "/database.sql.gz", "/o.tar.gz", "/upload.sh",
            "/WEB-INF/classes/dataBase.properties", "/b.php", "/setup.sh",
            "/db.php.bak", "/WEB-INF/classes/conf/jdbc.properties",
            "/WEB-INF/spring.xml", "/.htaccess",
            "/resin-doc/viewfile/?contextpath=/&servletpath=&file=index.jsp",
            "/.htpasswd", "/id_dsa", "/WEB-INF/conf/activemq.xml",
            "/config/config.php", "/.idea/modules.xml",
            "/WEB-INF/spring-cfg/applicationContext.xml", "/test2.txt",
            "/WEB-INF/classes/applicationContext.xml",
            "/WEB-INF/conf/database_config.properties",
            "/WEB-INF/classes/rabbitmq.xml",
            "/ckeditor/samples/sample_posteddata.php", "/proxy.pac",
            "/sql.php", "/test2.php", "/build.tar.gz",
            "/WEB-INF/classes/config/applicationContext.xml",
            "/WEB-INF/dwr.xml", "/readme", "/phpmyadmin/index.php",
            "/WEB-INF/web.properties", "/readme.html", "/key"]
    for p in exp:
        t = threading.Thread(target=dirburte1,args=(ip,p))
        threads.append(t)
        t.start()     
 
    for t in threads:
        t.join()
