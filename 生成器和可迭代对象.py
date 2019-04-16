from collections import  Iterator,Iterable
import  time

'''
1.# 带有yield关键字的函数就是生成器函数
def hello():
    yield 1
    yield 2
'''

class MyListIter(object):
    def __init__(self, data):
        # 保存 可迭代对象中的数据的引用
        self.data = data
        # 保存用户访问的下一个元素的下标
        self.index = 0

    def __next__(self):
        """next(迭代器对象) =====> 迭代器对象.__next__()"""
        # print("当前的下标是%d" % self.index)
        if self.index < len(self.data):
            data = self.data[self.index]
            self.index += 1
            return data
        else:
            # 抛出一个StopIteration异常
            raise StopIteration

