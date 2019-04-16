'''
1.重写new方法
用类属性记录创建出来的实例对象
2.既然创建的类自始至终只有一个，所以init'初始化也应该只有一次
重写init方法
'''
#单例模式：可以让类“创建”出的对象只有一个
class shoppingCar:
    _instance=None  #类属性
    _has_init=False
    def __new__(cls, *args, **kwargs):
        # 第一次调用new时创建并记录对象
        if cls._instance==None:
            #使用系统方式创建的对象
            new_obj=object.__new__(cls)
            cls._instance=new_obj
            #第2-n次调用new时直接返回记录的对象
            return cls._instance

    def __init__(self):
        if shoppingCar._has_init==False:
            self.total_price=0
            shoppingCar._has_init=True

car1 = shoppingCar()
car1.total_price=100
print(car1.total_price)
car2=shoppingCar()
print(car2.total_price)

