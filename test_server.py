
from config import socket,host,port

def Main(message):


    mySocket = socket.socket()
    mySocket.connect((host, port))

    while message != 'q':
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()

        return (data)


    mySocket.close()