import  threading
import time

'''
1.创建线程   thd=threading.Thread(target=saySorry)
2.启动线程   thd.start()
查看开启的线程数  threading.enumerate()
'''
def saySorry():
    print("what are you doing？")
   # print(threading.enumerate())
    time.sleep(1)

if __name__=='__main__':
    for i in range(5):
        thd=threading.Thread(target=saySorry)
        thd.start()
    print(threading.enumerate())