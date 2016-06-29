import subprocess #для запуска программ


def runCMD(cmdImgStrimer):

    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmdImgStrimer, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT, close_fds=True)

    return 1

def right():
    runCMD('/')
    return 1


def left():

    return 1

def LedStartStop():

    return 1