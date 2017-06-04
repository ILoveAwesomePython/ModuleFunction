#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu
import socket
import os,json
import optparse

STATUS_CODE = {
    250 : "invalid cmd format, eg: {'action':'get','filename':'test.py','size':344}",
    251 : "Invalid cmd",
    252 : "Invalid auth data",
    253 : "Wrong user name or password",
    254 : "passed authenticate"
}

class FTPClient(object):
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option("-s","--server", dest="server",help="ftp server IP")
        parser.add_option("-P", "--port", type="int", dest="port", help="ftp server port")
        parser.add_option("-u", "--username", dest="username", help="username")
        parser.add_option("-p", "--password", dest="password", help="password")
        self.options , self.args = parser.parse_args()
        self.verify_args(self.options,self.args)
        self.make_connection()

    def make_connection(self):
        self.sock = socket.socket()
        print(self.options.server,self.options.port)
        self.sock.connect((self.options.server,self.options.port))


    def verify_args(self,options,args):
        """校验参数合法类型"""
        if options.username and options.password:
            pass
        elif options.username is None and options.password is None:
            pass
        else:
            print(options.username,options.password)
            exit("Err: username and password must be provide together")

        if options.server and options.port:
            if options.port >0 and options.port <65535:
                return True
            else:
                exit("Err: server port must in 0-65535")


    def authenticate(self):
        """用户验证"""
        if self.options.username:
            print(self.option.username,self.option.password)
        else:
            retry_count = 0
            while retry_count < 3:
                username = input("username").strip()
                password = input("password").strip()
                print(username,password)
                return self.get_auth_result(username,password)


    def get_auth_result(self,user,password):
        print("123131231")
        data = {'action':'auth',
                'username':user,
                'password':password}

        self.sock.send(json.dumps(data).encode())
        print("server res", data)
        response = self.get_response()
        if response.get('status_code') == 254:
            print("Passed authentication!")
            self.user = user
            return True
        else:
            print(response.get("status_msg"))




    def get_response(self):
        "得到服务器端回复"
        data = self.sock.recv(1024)
        print("server res", data)
        data = json.loads(data.decode())
        return data



    def interactive(self):
        if self.authenticate():
            print("__-start -__interactive I with you")
            while True:
                choice = input("[%s]:"%self.user).strip()
                if len(choice) == 0:continue
                cmd_list = choice.split()
                if hasattr(self,cmd_list[0]):
                    func = getattr(self,"_%s"%cmd_list[0])
                    func = getattr(self,"_%s"%cmd_list[0])
                    func(cmd_list)
                else:
                    print("Invalid cmd")

    def _get(self,cmd_list):
        print("get--",cmd_list)
        if len(cmd_list) == 1:
             print("no filename follows...")
             return
        data_header = {
            'action':'get',
            'filename': cmd_list[1]
        }

        self.sock.send(json.dump(data_header).encode())
        response = self.get_response()
        print(response)
        if response["status_code"] == 257: #ready to receive
            base_filename = cmd_list[1].split('/')[-1]
            received_size = 0
            file_obj = open(base_filename,'wb')
            while received_size < response['file_size']:
                data = self.sock.recv(4096)
                received_size += len(data)
                file_obj.write(data)
            else:
                print("----->file rece done-----")
                file_obj.close()





if __name__ == '__main__':
    ftp = FTPClient()
    ftp.interactive()
