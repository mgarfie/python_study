f=open("bii.txt","r",encoding="UTF-8")
g=open("E:\\code_python\\文件操作\\bbb.txt","w",encoding="UTF-8")                           #此处特别注意，路径要用\\代替，因为\有可能是转义字符
for i in f:                                                                                #其次用相对路径很有可能报错
    a=i.split(",")
    if a[4]=="正式\n":
        g.write(i)  
        print(i)
g.close()
