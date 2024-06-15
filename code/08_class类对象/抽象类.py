class App():
    def clike(self):
        pass

    def move(self):
        pass
    def get_mouse(self):
        pass

class from1(App):
    def clike(self):
        print("这里是clike")

class mouse(App):
    def move(self):
        print("这里是move")
    def get_mouse(self):
        print("这里是get_mouse")


my_from = from1()
my_mose = mouse()

my_from.clike()
my_mose.move()
my_mose.get_mouse()

# 抽象结构的概念就是父项定义需求（设计标准），子项根据多姿来完成要求（实现标准）
