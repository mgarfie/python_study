#=======================基本捕捉语法==================================
try:
    f=open("E:\\code_python\\错误捕捉\\bas.txt","r",encoding="UTF-8")
except:
    print("出现异常,文件不存在,已将模式改为w")
    f=open("E:\\code_python\\错误捕捉\\bas.txt","w",encoding="UTF-8")
#=======================捕捉指定异常========================================

try:
    print(name)
except NameError as e:                      #捕获异常代码为：NameError的异常
    print("出现未定义的变量")                #e为异常的别名  记录着异常信息
    print(e)

#========================捕捉多个异常===========================================
try:
    1/0
except(NameError,ZeroDivisionError) as m:
    print("组合错误")


#=================捕获所有异常=======================================
try:
    f=open("E:\\code_python\\错误捕捉\\bas.txt","r",encoding="UTF-8")
except Exception as total:
    print("捕获所有异常")
#================================完全体===============================

try:
    f=open("E:\\code_python\\错误捕捉\\bas.txt","r",encoding="UTF-8")                           #可能错误的语句
except Exception as total:
    print("捕获所有异常")                                                                       #捕获到执行的代码
else:
    print("正常运行")                                                                           #没捕获到执行的代码
finally:
    print("是否异常都执行")                                                                      #是否都执行的代码