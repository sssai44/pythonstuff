num1 = int(input("Enter first number  : "))
num2 = int(input("Enter second number  : "))
se = 0
so = 0
if num1 > num2 :
     while(num2 <= num1):
        if num2%2 == 0:
          se = se + num2
          num2 = num2 + 1
        else:
          so = so + num2
          num2 = num2 + 1
else :
  while(num1 <= num2):
        if num1 % 2 == 0:
          se = se + num1
          num1 = num1 + 1
        else:
          so = so + num1
          num1 = num1 + 1
print("Sum of even numbers is : ", se)
print("Sum of odd numbers is : ", so)
