a = input("enter the operation to be performed(+,-,*,/): ")
if a == "+" :
    a1 = float(input("Enter first number to be added: "))
    a2 = float(input("Enter second number to be added: "))
    print (a1,"+",a2,"=",a1+a2)
elif a == "-":
    a3 = float(input("Enter number : "))
    a4 = float(input("Enter number: " ))
    print (a4,"-",a3,"=",a4-a3)
elif a == "*":
    a5 = float(input("Enter number : "))
    a6 = float(input("Enter number: "))
    print (a5,"*",a6,"=",a5*a6)
elif a == "/":
    a7 = float(input("Enter number : "))
    a8 = float(input("Enter number: "))
    print (a7,"/",a8,"=",a7/a8)
else:
    print("Invalid operation!")

