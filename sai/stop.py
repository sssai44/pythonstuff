count = 0
su = 0
while True:
	num = input("Enter the number: ")
	if num == "stop":
		break
	count = count+ 1
	su = su + int(num)

print("Sum is: ", su)
print("The number of numbers are: ", count)

