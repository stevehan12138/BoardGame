from client import *

HOST='192.168.0.108'
PORT=42069
BUFSIZ=1024
stillplaying = True

client = Client(HOST, PORT, BUFSIZ)
while stillplaying:
    stillplaying = client.waitCommand()

client.closeConn()