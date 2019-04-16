import copy
import random
from time import time,strftime,localtime
from datetime import datetime, timedelta, date

a=15**2
b=15//4
(c)=15/6
d=15%7
print("a=%d\nb=%d\nc=%f\nd=%d\n"%(a ,b  ,c  ,d))
print(divmod(28,6))  #(4,4)
print("##############################")
#end=用来控制每组输入之间的间隔
for i in range(10):
    print(random.randint(1,10),end=', ')

print("###################################")
print("{}：计算机{}的CPU 占用率为{}%。".format("2016-12-31","PYTHON",10))
print("{}{} {}".format("圆周率是",3.1415926,"..."))
list1=[1,[2,3,4],(7,9,100)]
print(list1[1][0])
word=['mon','tus','wed']
print(list(enumerate(word,start=0)))

'''
字符串切片
'''
print("######################################")
str1="0123456789"
print(str1[2])
print(str1[0:])
print(str1[0:5])
str2=str1[:]
print(str2)
print(str1[::-1])
print(str1[::2])
print(str1[1::2])
print(str1[1:8:2])
print("hhh",str1[-2:1:-1])
print(str1.find('5',0,7))
# 按照指定字符分割
wda='one two three four'
print(wda.split())
print(wda.split('o'))
price=135884
rate=0.08
print('定价',format(price,'>8d'))
###########################id和内存
c = 2.0
d = 2.0
print(id(c),id(d),id(2.0))
print('c == d:',c==d)
print('c is d:',c is d)
'''
元祖与列表
'''
##################元祖与列表######################
list1='one','two','three'
print(type(list1))
list2=[11,56,23]
print(type(list2))
'''
列表推导式
'''
numb=[]
numb=[(item) for item in range(10,50) if item%9==0]
print(numb)

data=[15,23,34]
number=data
data[0]=100
print(number)
print(id(data),id(number))
n2=55
n3=copy.copy(n2)
print(n2,n3)
n2=999
print(n2,n3)
l=[]
for i in range(21):
    l.append(i)
print(l[0:20:4])
###############eval函数#######################

##############字典集合#########################
dic1={"name":"Tom","gender":"M","age":13}
print(dic1.values())
print(dic1.get("name"))  #按键寻找值
print(dic1.keys())
print(dic1.items())
'''
字典推导式
'''
result={key:value for(key,value) in zip([1,2,3],['one','two','three'])}
#zip 函数，将两个列表进行压缩，前面是key后面是value
print(result,end='')
print("\n")
dic2={1: 'one', 2: 'two', 3: 'three'}
# 输出的是key
for i in dic2:
    print(i)
# 字典的遍历
for key in dic2:
    print('key=%2d,value=%s'%(key,dic2[key]))
list3=[1,1,2,2,3,5,4,4,8,9]
set1=set(list3)
# 集合可以去重
print(set1)
'''函数
'''
def caclu(*value):
    result=1
    for item  in value:
        result*=item
    return result
print("3个参数",caclu(2,3,5))

def score(**value):
    print("score:",value)
score(eng=77,math=110,policy=70)

'''time函数
'''
print(time()) #返回秒
print(strftime('%Y-%m-%d',localtime()))  #获取当前日期
'''天数转化为日期
'''
d1=date.today()
d2=d1+(timedelta(days=7))#将天数转化成日期
print(d2)
print(date.today())  #获取当前日期起
print(date.today().year)  #获取当前年份
print(date.today().month) #获取当前月份
print(date.today().day) #获取当前天数


'''装饰器
'''
