from socket import *
import ast

class Client:
    def __init__(self, HOST, PORT, BUFSIZ):
        self.BUFSIZ = BUFSIZ
        self.ADDR = (HOST, PORT)
        self.tcpCliSock = socket(AF_INET,SOCK_STREAM)
        self.tcpCliSock.connect(self.ADDR)

    def waitCommand(self):
        rec_data = self.tcpCliSock.recv(self.BUFSIZ)
        if rec_data.decode() != '':
            return self.dataEncoder(rec_data)

    def dataEncoder(self, rawdata):
        data = ast.literal_eval(rawdata.decode())
        if data['type'] == 'print':
            print(data['data'])
            return True
        elif data['type'] == 'input':
            inputdata = input(data['data'])
            self.__sendData('inputreply',inputdata)
            return True
        elif data['type'] == 'gameover':
            print(data['data'])
            return False


    def __sendData(self, datatype, data):
        self.tcpCliSock.send(('{"type": "%s","data": "%s"}' % (datatype, data)).encode())

    def closeConn(self):
        self.tcpCliSock.close()