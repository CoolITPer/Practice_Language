import  threading

g_number=0

def work1(lock):
    global g_number
    for i in range(1000000):
        # 尝试获取并且加锁　如果没有被锁定　就可以被我锁定；　
        # 如果已经被锁定　阻塞等待　直到成功获取并且锁定　
        lock.acquire()
        g_number += 1

        # 释放锁资源　解锁　　未锁定　－－－－> 未锁定状态
        lock.release()
        # print(g_number)

def work2(lock):
    global g_number
    for i in range(1000000):
        # 尝试获取并且加锁　如果没有被锁定　就可以被我锁定；　
        # 如果已经被锁定　阻塞等待　直到成功获取并且锁定　
        lock.acquire()
        g_number += 1

        # 释放锁资源　解锁　　未锁定　－－－－> 未锁定状态
        lock.release()
        # print(g_number)

if __name__=='__main__':
    g_lock=threading.Lock()

    wo1_thd=threading.Thread(target=work1,args=(g_lock,))
    wo1_thd.start()

    wo2_thd = threading.Thread(target=work2, args=(g_lock,))
    wo2_thd.start()

    wo1_thd.join()
    wo2_thd.join()
    print("最终数据是：%d"%(g_number))
