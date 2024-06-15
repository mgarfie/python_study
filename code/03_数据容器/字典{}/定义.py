#========================================基本定义=================================================
my_list={"杨凯":"http://www.8x4c.com","许光远":"http://www.h8v8.com","毛玉琳":"http://www.4399.com"}  #定义字典
a=input("姓名：")
print(f"{my_list[a]}")

#========================================嵌套定义=================================

my_grades={"高梦莹":{
    "语文":60,
    "数学":70,
    "英语":90
    
},
    "毛玉琳":{
    "语文":50,
    "数学":40,
    "英语":20
    }
}
a=input("姓名：")
b=input("什么成绩？")
print(f"{my_grades[a][b]}")                         #从定义的字典中取出指定数据，a为姓名，b为科目   分开写为：my_grades[姓名][成绩]（my_grades[根][子]）

#===================================================字典的操作===================================================
my_operate={"毛玉琳":60,"任世航":50,"许光远":20}
my_operate["刘涛"]=90                                   #添加新元素
print(my_operate)

my_operate["毛玉琳"]=444                                   #修改元素

print(my_operate)
a=my_operate.pop("毛玉琳")                                      #删除元素
print(a)
print(my_operate)

my_operate.clear()                                      #清除字典
print(my_operate)

my_operate={"毛玉琳":60,"任世航":50,"许光远":20}
kets=my_operate.keys()                              #全部key
print(f"字典全部的为{kets}")

for i in my_operate:                                        #for遍历所有
    print(f"用for进行的遍历{i}")

