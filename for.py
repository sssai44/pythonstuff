n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
se = 0
so = 0
if n1 > n2:
    while(n2<=n1):
        if n2%2 == 0:
          se = se +n2
          n2 = n2+1
        else:
          so = so + n2
          n2 = n2 +1
else:
    while(n1<=n2):
        if n1%2 == 0:
          se = se + n1
          n1 = n1 + 1
        else:
          so = so + n1
          n1 = n1 + 1
print("The sum of odd numbers: ",so)
print("The sum of even numbers: ",se)
