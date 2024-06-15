#1.====================“w”模式1.打开文件时清空里面所有2.文件不存在创建新文件===========================
f=open("E:\code_python\文件操作\写文件.txt","w",encoding="UTF-8")
f.write("hello,world")

f.close  
f=open("E:\code_python\文件操作\写文件.txt","w",encoding="UTF-8")

f.write("ASDASDASD")                              #用心的内容替换了旧的内容
f.close                                     #其中内置了 flush功能
#2.=================“a”模式1.不会创建新文件2.文件后面追加新内容==========================================

f=open("E:\code_python\文件操作\写文件.txt","a",encoding="UTF-8")
f.write("hello,world")
f.write("\n追加下一行")
f.flush