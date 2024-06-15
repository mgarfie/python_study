class Animal:
    def speak(self):
        print(1)

class makey(Animal):
    pass
    # print("这里是makey")


class Dog(Animal):
    pass
    # print("这里是Dog")


def test(animal):
    animal.speak()

Dog = Dog()
makey = makey()

test(makey)
test(Dog)


#
# # --------------------类方法的多态：---------------------------------
#
# class China():
#     def capital(self):
#         print("Beijing is the capital of China.")
#
#     def language(self):
#         print("Mandarin is the primary language of China.")
#
#     def type(self):
#         print("China is a developing country.")
#
# class USA():
#     def capital(self):
#         print("Washington, D.C. is the capital of USA.")
#
#     def language(self):
#         print("English is the primary language of USA.")
#
#     def type(self):
#         print("USA is a developed country.")
#
# obj_china = China()
# obj_usa = USA()
# for country in (obj_china, obj_usa):
#     country.capital()
#     country.language()
#     country.type()
#
#
#
#
#
#
#
#
#
# # -------------------函数和对象的多态---------------------------
# class a:
#     def a1(self):
#         print("a的a1")
#     def a2(self):
#         print("a的a2")
#     def a3(self):
#         print("a的a3")
#     def a4(self):
#         print("a的a4")
#
#
# class b:
#     def a1(self):
#         print("b的a1")
#     def a2(self):
#         print("b的a2")
#     def a3(self):
#         print("b的a3")
#
#
# def fun(c):
#     c.a1()
#     c.a2()
#     c.a3()
#
#
# fun_a = a()
# fun_b = b()
#
# fun(fun_a)
# fun(fun_b)
#
# # -----------------------类继承时的多姿------------------------------------------
# class a:
#
#     def a1(self):
#         print("a,a1")
#
#     def a2(self):
#         print("a,a2")
#
#
# class b(a):
#     def a2(self):
#         print("b,a2")
#
#
# class c(b):
#     def a2(self):
#         print("c,a2")
#
#
# obj_a = a()
# obj_b = b()
# obj_c = c()
#
# obj_a.a1()
# obj_a.a2()
#
# obj_b.a1()
# obj_b.a2()
#
# obj_c.a1()
# obj_c.a2()
# obj_a.a1()              # 由此看出，继承多姿，名字相同，但内容不同，并且不会改变父文件的被内容
