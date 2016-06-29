import socket

import subprocess #для запуска программ

import game

cmdImgStrimer = './video.sh' # команда для запуска

p = 0

def runCMD():
    global p

    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmdImgStrimer, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT, close_fds=True)

    return 1

def endCMD():
    proc1 = "killall mjpg_streamer"
    subprocess.Popen(proc1, shell=True)
    return 1

def Main():
    host = ''
    port = 5001

    mySocket = socket.socket()
    try:mySocket.bind((host, port))
    except OSError:
        return 0
    else:
        mySocket.listen(1)
        conn, addr = mySocket.accept()
        print("Connection from: " + str(addr))
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print("from connected  user: " + str(data))
            if data == 'runcmd':
                print('run cmd')
                runCMD()

            if data == 'endCMD':
                print('endCMD')
                endCMD()

            if data == 'left':
                print('endCMD')
                game.left()

            if data == 'right':
                print('endCMD')
                game.right()

            data = str(data).upper()

            print("sending: " + str(data))
            conn.send(data.encode())

        conn.close()


if __name__ == '__main__':
    while 1:
        Main()
