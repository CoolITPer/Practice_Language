from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    N=int(raw_input().split())
    M=int(raw_input().split())
    a=[]
    for i in range(N):
        number=int(raw_input().split())
        a.append(number)
    # print(a)
    index=N-M
    for i in range(index,N):
        print(a[i])
    for i in range(0,index):
        print(a[i])
    exit(0)

