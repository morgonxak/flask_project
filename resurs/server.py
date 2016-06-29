ip = '172.27.240.66'# raspberry

img_streamer = 0
vpn_proc = 0

import subprocess  # для запуска программ

cmdImgStrimer = './start.sh'  # команда для запуска

def runCMD():
    global img_streamer
    global vpn_proc
    ex = 0

    print("runOK")

    PIPE = subprocess.PIPE
    img_streamer = subprocess.Popen(cmdImgStrimer, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT,
                                    close_fds=True)

    return 1


def endCMD():
    print("закрываем программу")
    proc1 = "killall -s 9 mjpg_streamer"
    subprocess.Popen(proc1, shell=True)
