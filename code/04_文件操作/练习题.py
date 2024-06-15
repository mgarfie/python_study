f=open("E:\code_python\文件操作\练习题.txt","r",encoding="UTF-8")
list=f.read()
a=list.count("a")                           #积累对文件里出现a的次数
print(list)
print(a)

f.close