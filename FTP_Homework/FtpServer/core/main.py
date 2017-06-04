#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu
import optparse
from core.ftp_server import FTPHandler
import socketserver
from conf import settings

class ArvgHandler(object):
    def __init__(self):
        parser = optparse.OptionParser()
        # parser.add_option("-s","--host",dest="host",help="server binding server address")
        # parser.add_option("-p","--port",dest="port",help="server binding client" )
        (options,args) = parser.parse_args()
        # print("parser",options,args)
        # print(options.host,options.port)
        self.verifyArgs(options,args)

    def verifyArgs(self,options,args):
        '''校验并调用相应的功能'''
        if hasattr(self,args[0]):
            func = getattr(self,args[0])
            func()
        else:
            print("The action doesn't have")


    def start(self):
        print("---Let's go----")
        print(settings.HOST, settings.PORT)
        server = socketserver.ThreadingTCPServer((settings.HOST, settings.PORT), FTPHandler)
        server.serve_forever()
