#Write a python program that receives one float number from the user and 
#print the number with two decimal places.

#For the following input: 
    #3.141592
#The output should be: 
    #3.14

#For the following input: 
    #13
#The output should be: 
    #13.00

#Receive the number
a = int(input("Please insert a number: "))
b = int(input("Please insert a number: "))
c = float(a/b)


#Print the result
print("%.6f" % c)
