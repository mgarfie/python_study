mystr="woshi and gaomengying tadie"
astr="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
      #012
print(mystr[2])                       #打印出来变量中下表为2的元素，所以是s。正反下标相同
value=mystr.index("gao")                #index，查找该字符串在变量中所占下标位置
print(value)
r=astr.replace("a","c")                #替换关键字，将"a",更换为"c"，在赋值给变量C，替换并不是改变字符串本身，而是创建一个新的字符串
print(r)

#===========================================================================================================
split_list="hello python and maoyulin"
my_split_list=split_list.split(" ")                    #字符串分割函数split
print(my_split_list)                                   #以空格为分割

#==================================================================================================================
cstrip="   sahjkh   "
astrip="2112sahjkh11212"
print(cstrip.strip())                                 #去除前后空格，不给参数默认去除前后空格
print(astrip.strip("12"))                             #传入的是12，其实是”1“和”2“，是按照单个字符

#===================================================================================================================
astr_count="aaaccaaaaaaaaccaaaaaaccaaaaaacccaaaaaa"
count=astr_count.count("c")
print(f"astr_coun中{astr_count}现c的次数共有{count}")             #计数函数，统计出现的次数



