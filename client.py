from socket import *

IP = '39.106.188.198'
SERVER_PORT = 9999
BUFLEN = 512

dataSocket = socket(AF_INET, SOCK_STREAM)

dataSocket.connect((IP, SERVER_PORT))

while True:
    toSend = input('>>> ')
    if toSend == 'exit':
        break
    dataSocket.send(toSend.encode())

    recved = dataSocket.recv(BUFLEN)
    if not recved:
        break
    print(recved.decode())

dataSocket.close()
