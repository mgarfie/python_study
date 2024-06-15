#----open打开文件夹-----open(name,mode,encoding)
                # name--打开文件名的字符串(可以包含文件所在的具体路径)
                # mode--设置打开文件的模式(R只读，W覆盖写入，A追加)
                # encoding---文件的编码格式
f=open("E:\code_python\文件操作\python.txt","r",encoding="UTF-8")
print(f"类型为:{type(f)}")


#----------read方法读取数据------------------
print(f"读取10和字节的内容是：{f.read(10)}")
print(f"读取全部的内容是：{f.read()}")                                  #此处注意，因为受第7行代码的影响，当前指针是在第10个字符处的，所以在读取全部，会从 第10个字符以后开始读取

print("=============================================================================================================================")
#-----------------readlines方法读取----------------------
f=open("E:\code_python\文件操作\python.txt","r",encoding="UTF-8")       #此处重新打开就是为了把光标重新锁定一下，定位到开头，以便读取全部
list=f.readlines()                                                      #readlines是读取全部行，在封装到列表里
print(f"readlines读取全部{list}")

print("=============================================================================================================================")
#---------------redline方法读取-------------------------------
f=open("E:\code_python\文件操作\python.txt","r",encoding="UTF-8")       #此处重新打开就是为了把光标重新锁定一下，定位到开头，以便读取全部
list1=f.readline()                                                      #readline是读取一行
print(f"readlines读取第一行{list1}")
list2=f.readline()                                                    
print(f"readlines读取第二行{list2}")
print("=============================================================================================================================")

#-----------------使用for来遍历全部行-----------------------------------------
f=open("E:\code_python\文件操作\python.txt","r",encoding="UTF-8")

for lines in f:                                 #lines中的临时数据，就纪录了每一行的数据
    print(lines)

#--------------文件的关闭-----------------

#time.sleep(50000)
f.close
# with open("E:\code_python\文件操作\python.txt","r",encoding="UTF-8")as f: ==============词语发打开可以自动关闭

 

    