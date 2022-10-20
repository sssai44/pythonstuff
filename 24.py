i = 1
sum = 1
while i<6:
	for j in range(sum-2*(i-1),sum+1):
		print(chr(64+j),end=" ")
	print()
	sum += 2*i+1
	i+=1
