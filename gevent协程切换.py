from gevent import  monkey
monkey.patch_all()  # patch就是破解 gevent建议破解在第二行
import  gevent
import  time
'''
1.创建协程 g1=gevent.spawn(函数名，参数)
2.阻塞等待所有进程完 gevent.joinall([g1,g2,g3])
'''
def worker1(n):
    for i in range(n):
        print("in worker %s" % gevent.getcurrent())
        time.sleep(0.3)

# 创建一个协程对象 并且开始运行
g1 = gevent.spawn(worker1,10)
g2 = gevent.spawn(worker1,10)
g3 = gevent.spawn(worker1,10)

gevent.joinall([g1,g2,g3])