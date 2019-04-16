import  threading
'''
创建全局锁 g_lock = threading.Lock()
获得锁  g_lock.acquire()
解锁    g_lock.release()
'''
gl_number=0
# 创建一把全局互斥锁
g_lock = threading.Lock()
def work1():
    # print("work1")
    global  gl_number
    for i in range(1000000):
        g_lock.acquire()
        gl_number+=1
        g_lock.release()

def work2():
    # print("work2")
    global  gl_number
    for i in range(1000000):
        g_lock.acquire()
        gl_number+=1
        g_lock.release()

if __name__=='__main__':
    wo1_thd=threading.Thread(target=work1)
    wo1_thd.start()
    wo1_thd.join()
    print("work1中最后的数据是：%d" % (gl_number))

    wo2_thd=threading.Thread(target=work2)
    wo2_thd.start()
    wo2_thd.join()
    print("work2中最后的数据是：%d" % (gl_number))

    print("最终结果是：%d"%(gl_number))