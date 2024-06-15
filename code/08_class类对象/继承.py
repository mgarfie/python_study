
class phon:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"已经创建完一个类对象，他的名字为{self.name},年龄为：{self.age}")
    def a(self):
        print("这里是def1")

# ----------------------单继承----------------------------------
class phon2(phon):
    def __init__(self, sex):
        self.sex = sex
        print(f"性别{sex}")

    def b(self):
        print("这里是def2，单继承")


# 此处就可以看出来继承效果，但是在使用继承时，方法叫的是最新的
# a = phon2("男")
# a.a()
# a.b()


# ---------------------------多继承-------------------------------------

class phon3():

    def c(self, aa):
        print(f"这里是def3，多继承，外带{aa}")

class phon4():

    def __init__(self, bb):
        print(f"def4,的__init__测试，参数为{bb}")




    def d(self):
        print("这里是def4，多继承")




class phon5():

    def e(self):
        print("这里是def5，多继承")


class phon6(phon, phon3, phon4, phon5):
    pass
# pass代表空，因为语法要求，class中不允许为空

# 由此看出，如果继承的父项__init__有必须传递的参数时，需要在调用时把参数写子项里
    # 1.若继承中有两个及以上__init__时，会优先将参数传入  class phon5(phon, phon3, phon4):   中第一个需要参数传递的父项
    # 2.相同的，若重名也是按左边顺序来，左边优先级高
a = phon6("n", 18)
a.a()
a.d()
a.c("as")
a.e()

