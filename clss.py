#Find the first occurance of the even number  in the list: 
a = [11,22,33,44,55]
for i in range (len(a)) :
    if i % 2 == 0 :
        print("First even number found: ", i )
else:
    print("No")

