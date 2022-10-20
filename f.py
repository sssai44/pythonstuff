#Find the first occurance of the even number  in the list: 
#using flag variables

a = [11,22,33,44,55]
found = False
i = 0
while not found and (i < len(a)):
    if a[i] % 2 == 0:
        found = True
    else:
        i += 1
if found:
    print("Even number found: ", a[i])
else:
    print("Even number not found!")

