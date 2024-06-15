def user1():                        #定义一个有错误的函数
    print("这里是user1开始")
    1/0                             #这里一定出错
    print("这里是user1结束")


def user2():                        #定义正常的函数当传递者
    print("这里是user2开始")
    user1()                                 #传递者
    print("这里是user2结束")



user2()                              #调用会出错的函数





# def main():                         #错误捕捉
#     try:
#         user2()                                 
#     except Exception as e:
#         print(e)


                                                            #先调用user2.
                                                            # user2里调用user1
                                                            # user1中开始报错,被main中的错误捕捉捕捉带走