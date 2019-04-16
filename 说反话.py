word=input("请输入字符串")
# print(word.split()) #按空格划分，并返回列表形式
word_list=word.split()
word_list=word_list[::-1]#字符串最好处理啦，直接取反
# print(word_list)
for i in range(len(word_list)):
    # 先顺序输出
    if i!=len(word_list)-1:
        print(word_list[i],end=' ')
    else:
        print(word_list[i])
'''
字符串的取反 str=str[::-1]
列表的取反 list=list.reverse()
'''
