class data:             # 类似于创建了个对象
    name = None
    gender = None       # 给对象设置属性值
    age = None
    nationality = None


# 将变量赋值为对象
user = data
user.name = "杨凯"
user.age = 20
user.nationality = "中国"
user.gender = "男"

print(user.name)
print(user.age)
print(user.nationality)         # 输出个属性的值
print(user.gender)



