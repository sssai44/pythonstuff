import math
a=int(input())
flag = False
for i in range(0,1000):
    if 2**i==a:
        i=i+1
        print("it is",i-1,"th power")
        flag = True
if(flag == False):
    print("not a power")    

         