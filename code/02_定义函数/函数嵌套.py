
#===========================================函数嵌套==========================================================================================

#-----------定义函数2--------------------------
def i_2():                          

    print("---2---")

    i_3()#---------------在函数2里面，嵌套函数3

#------------定义函数1-------------------------
def i_1():
    print("---1---")

    i_2()#---------------在函数1里面，嵌套函数2

#------------定义函数3----------------------------

def i_3():
    print("---3---")

i_1()
##==============================================变量的作用域======================================================


unm=200


def i(x):
    unm=522
    print(f"在函数中变量unm为{unm}")



print(f"在全局变量中的unm为{unm}")

#从运行结果来看，变量unm并没有因为函数里的声明而变化，则函数里面的为局部变量

#----------------------------------------------global语句---------------------------------------------------------------------------------------

unml=200

def a(x):
    global unml
    unml=500
    print(f"在函数中变量unml为{unml}")


a(1)
print(f"在局部中变量unml为{unml}")
                                                #此时从结果来看变量unml在函数中通过global关键字加已经成为了全局变量，因此结果为500.500

