#Find the biggest number in the list:
a = [22,44,55,11,33]
b = a[0]
for elem in a[1:]:
    if elem>b:
        b = elem
print("The biggets element is: ",b)

