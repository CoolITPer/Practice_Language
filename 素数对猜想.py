# import math
#
# if __name__ == '__main__':
#     a=[]
#     count=0
#     data=int(input("请输入整数"))
#     for i in range(1,100000):
#         for j in range(2,int(math.sqrt(i))+1):
#             if i%j==0:
#                 break
#         else:
#             if i<=data:
#                 a.append(i)
#     for i in range(len(a)-1):
#         if (a[i+1]-a[i])==2:
#             count=count+1
#     print(count)
#
#

'''找素数最优代码'''
import time
def prime(n):
    flag = [1]*(n+2)
   # print(flag)
    p=2
    while(p<=n):
        print(p)
        for i in range(2*p,n+1,p):
            flag[i] = 0  #p是素数则p的倍数不可能是倍数
        while 1:
            p += 1
            if(flag[p]==1):
                break
start = time.time()
prime(100000)
end = time.time()
print(end-start)