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
            return "https://apponear.appspot.com"

    def apiAddr(self):
        if self.isDev():
            return "http://localhost:8085/"
        else:
            return "https://api-dot-apponear.appspot.com/"

    def aeAddr(self):
        if self.isDev():
            return "http://localhost:8090/"
        else:
            return "https://ae-dot-apponear.appspot.com/"
