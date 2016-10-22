import os


class SvcAddress:
    def isDev(self):
        if os.getenv('GAE_DEV', '0') == '1':
            return True
        else:
            return False

    def managerAddr(self):
        if self.isDev():
            return "http://localhost:8080/"
        else:
            return "http://apponear.appspot.com"

    def apiAddr(self):
        if self.isDev():
            return "http://localhost:8085/"
        else:
            return "http://api_service-dot-appspot.com/"

    def aeAddr(self):
        if self.isDev():
            return "http://localhost:8090/"
        else:
            return "http://ae_service-dot-appspot.com/"
