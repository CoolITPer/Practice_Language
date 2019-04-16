list1=list(input())
#在输入的同时将字符串转化为列表
sum=0
for value in list1:
    value=int(value)#将list1这个列表中的元素由str变成int
    sum=sum+value#计算每一位数字的和
list2=['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
list3=list(str(sum))#将sum变成str，再把每一位数字拆分成list3中的元素
lenth=len(list3)#计算列表长度
for value1 in list3:
    if lenth>1:
        print(list2[int(value1)],end=' ')
    else:
        print(list2[int(value1)], end='')#最后一个输出末尾无空格
    lenth=lenth-1

'''遍历列表'''
if __name__ == '__main__':
    list = ['html', 'js', 'css', 'python']

    # 方法1
    # print '遍历列表方法1：'
    for i in list:
        print ("序号：%s   值：%s" % (list.index(i) + 1, i))

    # print '\n遍历列表方法2：'
    # 方法2
    for i in range(len(list)):
        print ("序号：%s   值：%s" % (i + 1, list[i]))

'''按key取value'''
# data_dict[key]
