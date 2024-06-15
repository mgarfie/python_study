ygj_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
ygg_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
zgz=1000000
for i in range(0,20):
        import random
        ygj_list[i]=random.randint(1,10)
        ygg_list[i]=0
while zgz != 0 :
    for y in range(0,20):
        if zgz == 0 :
            break 
        if ygj_list[y] > 5 :
            ygg_list[y]=ygg_list[y]+1000
            zgz=zgz-1000
            print(f"员工{y}的绩效为{ygj_list[y]}应当发工资1000米")
        else :
            print(f"员工{y}的绩效为{ygj_list[y]}没超过5,不发工资下一位")
            continue
        print(f"员工{y},绩效为{ygj_list[y]},工资为{ygg_list[y]}总工资剩余{zgz}")

        
        





    
  


