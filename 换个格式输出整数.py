data=input("请输入数字")
if int(data) == 999:
    exit()
while 1:
    value=int(data)
    if value>=100:
        B=value//100
        for i in range(B):
            print('B',end='')
        S=(value%100)//10
        for i in range(S):
            print('S',end='')
        G=(value%100)%10
        for i in range(G):
            print(i+1,end='')
    if value<100:
        S=value//10
        for i in range(S):
            print('S',end='')
        G=(value%10)
        for i in range(G):
            print(i+1,end='')
    print()
    data = input("请输入数字")
    if int(data)==999:
        exit()