class test:
    name = None
    age = None
    # 此时这里面的变量是可以不声明的，因为在下面的__init__中也算是对变量的声明
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"已经创建完一个类对象，他的名字为{self.name},年龄为：{self.age}")

    # 如果不写__str__那么打印出来的都是内存地址
    def __str__(self):
        return f"str返回对象， name={self.name}, age= {self.age}"

    # 比较 魔法方法
    def __lt__(self, other):
        return  self.age < other.age

    # 比较二 魔法方法
    def __le__(self, other):
        return self.age >= other.age
    # 比较三 魔法方法
    def __eq__(self, other):
        return self.age == other.age



# test = test("毛玉琳", 19)
# print(test)
# print(str(test))
# 比较--------------------------------测试时把上面三个给注释了
stu1 = test("毛玉琳", 19)
stu2 = test("杨凯", 21)
print(stu1 == stu2)


# __init__有两个特征1.在程序中自动执行（不用调用名称）2.将传入参数自动传递给 __init__方法使用(传入参数直接给函数中的变量接收)
# __str__控制转换成字符，若不转换回来，那么直接打印的结果会是内存


