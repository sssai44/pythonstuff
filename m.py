# Find common elements - in,not in
c = []
a = [11,33,22,44,55]
b = [33,60,11,70,80,44]
for i in range (len(b)):
    if(b[i] in a):
        c.append(b[i])
print(c)