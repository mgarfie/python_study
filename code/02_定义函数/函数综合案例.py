name=input("请输入您的名字：")
money=50000


def outside(x):
    global money
    money+=x
    return money

def inside(x):
    global money

    money-=x
    return money


def hom():

    global i
    print("--------------主菜单-------------")

    print(f"{name}您好，这里是ATM机，您的余额为：{money}")
    print("查询余额请输入\t{1}")
    print("存款请输入\t{2}")
    print("取款请输入\t{3}")
    print("退出请输入\t{4}")

    i=input("您要什么操作?")
    return  i
while True:
    i=hom()
    if i=="1":
        print(f"您的余额为：{money}")
        continue
    elif i=="2" :
        a=outside(int(input("请输入要存的金额")))
        print(f"您的余额为：{a}")
        continue
        
    elif i=="3":
        a=inside(int(input("请输入要取的金额")))
        print(f"您的余额为：{a}")
        continue
    elif i=="4":
        print("好的，您已退出")
        break
    else:
        print("请输入有效的数！")
        break



 



