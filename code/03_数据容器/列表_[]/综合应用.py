#1,定义一个列表
mylist=[21,25,21,23,22,20]
print(mylist)
#2,追加一个元素到尾部
mylist.append(31)
#3,追加一个列表到尾部
extlist=[29,33,30]
mylist.extend(extlist)
#4,取出一个元素
a=mylist.pop(0)
print(a)
#5,取出最后一个元素
print(mylist)
myint=mylist.pop(-1)
print({myint})
#6.查找指定元素的下标
index=mylist.index(31)
print(index)





