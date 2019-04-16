import  multiprocessing
import os
import random
import time

'''
创建进程池：pool=multiprocessing.Pool()
阻塞方式添加进程：pool.apply(func=worker,args=('111',))
非阻塞方式添加进程：pool.apply_async(func=worker, args=('333',))
关闭进程池： pool.close()
'''
def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d" % (msg,os.getpid()))
    # random.random()随机生成0~1之间的浮点数
    time.sleep(random.random()*5)
    t_stop = time.time()
    print(msg,"执行完毕，耗时%0.2f" % (t_stop-t_start))

if __name__=='__main__':
    pool=multiprocessing.Pool()

    #阻塞方式添加任务--等一个任务完成后再去执行下一个任务
    pool.apply(func=worker,args=('111',))
    pool.apply(func=worker,args=('222',))

    #费阻塞方式添加任务--按时间片来执行任务，多个任务可以并发执行
    pool.apply_async(func=worker, args=('333',))
    pool.apply_async(func=worker, args=('444',))
    # 3 关闭进程池 ----  不再允许添加新的任务
    pool.close()

    # 4 阻塞等待所有任务执行完成
    # 只要主进程一退出 所有正在执行的任务全部终止
    pool.join()
    print("所有任务都执行完成了")