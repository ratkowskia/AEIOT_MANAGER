import os

class Addr:
    def __init__(self, url, port):
        self.url = url
        self.port = port

    def __repr__(self):
        return "<Test a:%s b:%s>" % (self.url, self.port)

    def __str__(self):
        return self.url+":"+self.port

    def set(self, url, port):
        self.url = url
        self.port = port

class SvcAddress:
    def isDev(self):
        if os.getenv('GAE_DEV', '0') == '1':
            return True
        else:
            return False

    def managerAddr(self):
        if self.isDev():
            return Addr('127.0.0.1', '8080')
        else:
            return Addr('apponear.appspot.com', '80')

    def apiAddr(self):
        if self.isDev():
            return Addr('127.0.0.1', '8085')
        else:
            return Addr('api_service-dot-appspot.com', '80')

    def aeAddr(self):
        if self.isDev():
            return Addr('127.0.0.1', '8090')
        else:
            return Addr('ae_service-dot-appspot.com', '80')
