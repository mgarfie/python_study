def str_reverse(s):
    if len(s)<1:
        return s
    return str_reverse(s[1:])+s[0]

#return str_reverse(s[1:])+s[0]讲解：返回 自己 调用自己然后取第二个，写0是因为外国人从0开始，":"后面不写是默认为到最后一个，+s[0]是把第一个给粘出来
#原理：len(s)取长度,一开始长度大于，所以返回 return str_reverse(s[1:])+s[0]这一句，然后去除一位再开始，


#疑问  那返回时数据在哪？s[0]是怎么拼接的？


result=str_reverse('asdfghjkl')
print(result)
#=============================================================================================================================

def substr(s,x,y):
    return s[x:y]

                                        #viual运行不出来，但是pythoncharm可以运行出来
substr("啊手机打开就",2,3)
print(substr)


#疑问  为什么返回<function substr at 0x00000221661711B0>
