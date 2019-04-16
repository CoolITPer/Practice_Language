import  multiprocessing
import os
import time

'''
1.创建子进程 proc=multiprocessing.Process
2.获得子进程的编号 os.getpid()
3.获得子进程的父进程 os.getppid()
多进程之间不共享全局变量
'''
def proc_func(number,age):
    print(age)
    print("这是子进程%d PID:%d 父进程的PID:%d" % (number,os.getpid(),os.getppid()))
    for i in range(3):
        print("这是子进程")
        time.sleep(1)

if __name__=='__main__':
    proc=multiprocessing.Process(target=proc_func,args=(999,),kwargs={'age':18})
    proc.start()

    '''
    当数字大了时候，操作系统会自动替换两个进程
    '''
    for i in range(5):
        print("这是主进程：%d"%os.getpid())