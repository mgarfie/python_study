def print_file_info(file_name):
    try:
        f=None
        f=open("file_name","r",encoding="UTF-8")
        count=f.read()
        print(count)
    except Exception as total:
        print(total)
    finally:
        if f:                   #如果变量中是none，则表示false是进不去的，反之则可以执行
            f.close             #关闭文件



if __name__=='__main__':
    print_file_info("E:\\code_python\\04_文件操作\\bbb.txt")


