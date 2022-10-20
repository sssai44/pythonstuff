#Create a list of squares of numbers from 1 to n:
a = int(input("ENte the value of n: "))
list=[]
for i in range (1,a+1):
    list.append(i**2)
print(list)