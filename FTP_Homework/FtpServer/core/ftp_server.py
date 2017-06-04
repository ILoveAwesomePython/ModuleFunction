#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu

import socketserver
import configparser
import json
import os
from conf import settings


STATUS_CODE = {
    250 : "invalid cmd format, eg: {'action':'get','filename':'test.py','size':344}",
    251 : "Invalid cmd",
    252 : "Invalid auth data",
    253 : "Wrong user name or password",
    254 : "passed authenticate",
    255:  " Filename doesn't provided",
    256:  " File doesn't exist on serve",
    257:  " Ready to send file"
}

class FTPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print(self.client_address[0])
            print(self.data)
            if not self.data:
                print("client closed...")
                break
            data = json.loads(self.data.decode())
            print(data)
            if data.get('action') is not None:
                print("---->", hasattr(self, "_auth"))
                func =  "_%s" % data.get('action')
                print(func)
                if hasattr(self,func ):
                    func = getattr(self,func)

                    func(data)
                else:
                    print("invalid cmd ")
                    self.send_response(251)

            else:
                print("invalid cmd format")
                self.send_response(250)

    def send_response(self,status_code,data=None):
        """向客户端返回数据"""
        response = {'status_code':status_code,'status_msg':STATUS_CODE[status_code]}
        if data:
            response.update(data)
        self.request.send(json.dumps(response).encode())


    def _auth(self,*args,**kwargs):
        print("12314")
        data = args[0]
        if data.get("username") is None or data.get("password") is None:
            self.send_response(252)
        user = self.authenticate(data.get("username"),data.get("password"))
        if user is None:
            self.send_response(253)
        else:
            print("passed authenticate",user)
            self.user = user
            self.send_response(254)

    def authenticate(self,username,password):
        """验证用户数据合法性"""
        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_FILE)
        if username in config.sections():
            _password = config[username]["password"]
            if _password == password:
                print("pass auth..",username)
                config[username]["Username"] = username
                return config[username]


    def _put(self,*args,**kwargs):
        pass

    def _get(self,*args,**kwargs):
        data = args[0]
        if data.get('filename') is None:
            self.send_response(255)
        user_home_dir = "%s/%s"%(settings.USER_HOME,self.user["Username"])
        file_abs_path = "%s/%s"%(user_home_dir,data.get('filename'))
        print("file abs path",file_abs_path)
        if os.path.isfile(file_abs_path):
            print("----ready to send file")
            file_obj = open(file_abs_path,"rb")
            file_size = os.path.getsize(file_abs_path)
            self.send_response(257,data={'File_size':file_size})
            for line in file_obj:
                self.request.send(line)
            else:
                file_obj.close()
                print("send file done...")
        else:
            self.send_response(256)

    def _ls(self,*args,**kwargs):
        pass

    def _cd(self,*args,**kwargs):
        pass




