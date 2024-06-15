mylist=[1,2,3,4,5,6,7,8,9]
#print(mylist)
#=====================使用while循环来遍历list=================================
def listwhile(x):
    i=0
    while i < len(mylist):
        mylist[i]=i
        i+=1
    print(mylist)
#=====================使用for循环来遍历list================================
def listfor(x):
   
    for i in mylist:
        print(i)

listfor(1)
listwhile(1)


