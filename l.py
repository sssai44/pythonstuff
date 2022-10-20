#Modify the elements in the list, Add 100 to all the elements:
a = [10,20,30]
print("Before modification: ",a)
for elem in range(len(a)):
    a[elem] = a[elem] + 100
print("Ater modification: ",a)
