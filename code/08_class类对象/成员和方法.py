class myl:
    name = "毛玉琳"
    age = 19
    def a(self):
        print("你好，我是", {self.name})
# 当中函数中的self是一个关键字 用于在类对象中的函数调用此内的变量
m = myl()
m.a()


# -----------------------------------------------------------
class total:
    name = None
    age = None
    def b(self,msg):
        print(f"你好，我是{self.name},今年{self.age}岁,我是{msg}")

y =total()
y.name = "杨凯"
y.age = 21
y.b("男生")

# -----------------------------
l =total()
l.name = "毛利伟"
l.age = 21
l.b("女生")

# -----------------------------------------------------------------
