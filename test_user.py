import socket

import subprocess #для запуска программ
cmdImgStrimer = '/home/pi/kiski/mjpg-streamer-master/mjpg-streamer-experimental/start.sh' # команда для запуска

p = 0
p2 = 0
##
pP = 0
p2P = 0


def runCMD():
    global p

    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmdImgStrimer, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT, close_fds=True)
    return 1

def endCMD():
    proc1 = "killall -s 9 mjpg_streamer"
    subprocess.Popen(proc1, shell=True)
    return 1

def Main():
    host = "127.0.0.1"
    port = 5001

    mySocket = socket.socket()
    mySocket.bind((host, port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print("Connection from: " + str(addr))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected  user: " + str(data))
        if data == 'runcmd':
            runCMD()

        if data == 'endcmd':
            runCMD()

        data = str(data).upper()

        print("sending: " + str(data))
        conn.send(data.encode())

    conn.close()


if __name__ == '__main__':
    while 1:
        Main()
