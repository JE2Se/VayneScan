# -*- encoding: utf-8 -*-
'''
@File : platform.py
@Time : 2019/07/06 01:31:35
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''
from lib import *


class ManageProcessor(object):
    PLUGINS = {}

    def process(self,ip,port,plugins=()):
        if plugins is ():
            for plugin_name in self.PLUGINS.keys():
                try:
                    print(Vcolors.YELLOW+"[*]开始检测",plugin_name+Vcolors.ENDC)
                    self.PLUGINS[plugin_name]().process(ip,port)
                except:
                    print(Vcolors.WARNING+"[-]{} 未成功检测，请检查网络连接或或目标存在负载中间件".format(plugin_name)+Vcolors.ENDC)
        else:
            for plugin_name in plugins:
                try:
                    print("[*]开始检测 ",self.PLUGINS[plugin_name])
                    self.PLUGINS[plugin_name]().process(ip,port)
                except:
                    print ("[-]{}未成功检测，请检查网络连接或或目标存在负载中间".format(self.PLUGINS[plugin_name]))
        return

    @classmethod
    def plugin_register(cls, plugin_name):
        def wrapper(plugin):
            cls.PLUGINS.update({plugin_name:plugin})
            return plugin
        return wrapper




