import  threading
from time import sleep


def sing():
    for i in range(3):
        print("正在唱歌...%d"%i)


def dance():
    for i in range(3):
        print("正在跳舞...%d"%i)
        sleep(1)

if __name__=='__main__':
    sin_thred=threading.Thread(target=sing)
    sin_thred.start()

    dance_thred=threading.Thread(target=dance)
    dance_thred.start()

    while True:
        if len(threading.enumerate()) == 1:
            print("只剩下主线程了")
            break


    sin_thred.join()
    dance_thred.join()

    print("主线程打印完这句话也要退出了")