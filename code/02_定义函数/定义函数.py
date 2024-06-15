
# 函数定义格式-------------------def 函数名 (传入参数)：
#  ------------------------------- 函数体（时间）
# ----------------------------------return返回值
def my_len (data):
    control = 0
    for i in data:
        control += 1
    print(f"字符串{data}的长度为{control}")


str1 = "ghaskdfhgh"
str2 = "ajshgdfkjasgdkfaghdfk"
str3 = "ajkhfdkajsghfkasgdfjkasgdfjkHSGDA"


my_len(str1)
my_len(str2)
my_len(str3)

print(end="")
print(end="")


print(len(str1))
print(len(str2))
print(len(str3))
# -------------------------案例二------------------------------

def my_computation(x,y) :
    solution = x + y
    print(f"{x}+{y}的答案是{solution}")


my_computation(6,7)
                #此案例中 def my_computation(x,y) :  中的（x，y）是形参
                #============== =my_computation(6,7) 中的（6，7）是实参
                #当然  def my_computation(x,y)中可以不止一个的形参  形参可以是无限个  也可以是0个


#----------------------------------------------------------------------------------------------------------------------------
# 
# 				
my_computation(6,7,8)       
my_computation(6)
                #由此看出形参与实参必须是对应关系   要不都会报错




#-------------------------------案例三-----------------------------------------------------
def hs(x):
    if x < 37.5 :
        print(f"欢迎来到python!请出示您的健康码以及72小时核酸证明,并配合测量体温!体温测量中，您的体温是:{x}，体温正常请进!")
    else:
        print(f"欢迎来到python!请出示您的健康码以及72小时核酸证明,并配合测量体温!体温测量中，您的体温是:{x},需要隔离!")



hs(int(input("请输入你的体温")))


