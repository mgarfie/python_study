my_list=[0,1,2,3,4,5,6,7,8,9]
result1=my_list[1:4]            #切片1，从1开始到4结束，步长默认为1
print(f"结果1：{result1}")

my_tuple=(0,1,2,3,4,5,6,7,8,9)
result2=my_tuple[::2]            #切片2，从头到尾，步长为2
print(f"结果2：{result2}")


my_str="0123456789"
result3=my_str[::-1]               #切片2，从头到尾，步长为-1
print(f"结果3：{result3}")