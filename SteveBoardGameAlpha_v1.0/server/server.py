from socket import *
from time import ctime
import threading
import time
import ast

class Server:
    '''
            socks
              |
    -   -   -   -   -   -
    1   2   3   ...
    |
    -
   sock
    {'type': xxx, 'data': xxx}
    '''
    def __init__(self, HOST, PORT, BUFSIZ):
        self.socks = []
        self.ADDR = (HOST, PORT)
        self.BUFSIZ = BUFSIZ
        self.tcpSerSock=socket(AF_INET,SOCK_STREAM)
        self.tcpSerSock.bind(self.ADDR)
        self.tcpSerSock.listen(6)
        self.clientId = 0
        print('server started.')
        print('waiting for connecting...')

    def newClient(self):
        clientSock,addr = self.tcpSerSock.accept()
        print('connected from:', addr)
        self.socks.append([self.clientId, clientSock])
        self.clientId+=1

    def sendData(self, id, datatype, data):
        self.socks[int(id)][1].send(('{"type": "%s","data": "%s"}' % (datatype, data)).encode())

    def receiveData(self, id):
        data = self.socks[int(id)][1].recv(self.BUFSIZ)
        if data.decode() != '': 
            return self.dataEncoder(data)
            
    def dataEncoder(self,rawdata):
        data = ast.literal_eval(rawdata.decode())
        if data['type'] == 'inputreply':
            return data['data']

    def closeConn(self):
        self.tcpSerSock.close()