def i(x,y):
    add =x+y
    return add      # retrun关键字的应用


a =i(1,2)
print(a)


#------------------------------------------------------------------------------------------------------------------------------------------------

def i(x,y):
    add=x+y
                    #不写retrun的情况

a=i 
print("没有返回值函数，返回内容为：{a}")        #不写返回值会返回None
print("没有返回值函数，返回内容类型为：{styr}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------


#None的具体应用
def i(x):

    """
    函数说明文档：
    
        1.在此处书写东西不会被运行  可以理解为多行注释
        2.在此处书写，在实参哪里会有提示
    
    """
    if x > 18 :
        return 1                #此处的1没有任何实质意义，只是为了不返回None.因为返回None会于下面的重合影响判断
    else:
        return None             #此处的None效果与false是一样的，因为None可以理解为空，而空一定是false            

a=i(int(input("请输入您的年龄")))

if not a :
    print("您不满18，无法进入")
else:
    print("您已经满18了，游玩愉快")



#========================================函数多返回值===========================================================
def l(x):
    return 1,2,3                              #不管是函数里的还是声明外的，只要不对应就会报错

#x,z=l(1)                                      这里也可以看出来是需要有对应关系的，要不会报错
x,z,y=l(1)
print(x)
print(z)
print(y)

