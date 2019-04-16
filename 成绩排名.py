if __name__ == '__main__':
    list1=[]
    max=0
    min=100
    n=input("请输入一个整数")
    for i in range(int(n)):
        name=input("请输入姓名")
        id=input("请输入学号")
        grades=input("请输入成绩")
        if len(name)>10 or len(id)>10:
            print("输入的姓名学号都不可以超过10个字符串")
            break
        if int(grades)<0 or int(grades)>100:
            print("成绩只能在0到100之间")
            break
        dict1=dict(name=name,id=id,grades=grades)
        list1.append(dict1)
    for i in range(len(list1)):
        value=list1[i].get('grades')  #按键取值
        # print(value,type(value))
        if int(value)>max:
            max_i=i
            max=int(value)
        if int(value)<min:
            min_i=i
            min=int(value)
    print(list1[max_i].get('name'),' ',list1[max_i].get('id'),' ',list1[max_i].get('grades'))
    print(list1[min_i].get('name'),' ',list1[min_i].get('id'),' ',list1[min_i].get('grades'))
        # print(value)
    # print(list1)