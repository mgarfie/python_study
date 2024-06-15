class phon:
    __a = 1
    b = 2                   # 定义私有变量
    def __v(self):          # 定义私有方法
        print("aakjhsfj")
    def w(self):
        print("1546")


    def call(self):

        b = self.b
        if b > 1 :
            self.__v()
aa = phon()
print(aa.b)
print(aa.w())
print(aa.call())    # 但是可以使用别的方法调用私有方法与私有变量
# # 没办法直接调用私有成员和私有变量
# print(aa.__a)
# print(aa.__v)





# ----------------案例---------------------------------



class App:
    __is5G = False


    def __check(self):
        if self.__is5G == True:
            print("5g开启，正在使用5g")
        else:
            print("5g关闭，正在使用4g")
    def call(self):
        self.__check()

aa = App()
aa.call()

