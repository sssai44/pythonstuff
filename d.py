#Find the difference between successive elements of a lilst:
a = [10,50,100,145,150,175]
b=[]

for i in range (0,len(a)-1) :
    b.append(a[i+1]-a[i])
print(b)

