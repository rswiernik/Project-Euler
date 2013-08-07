x = 1
fibonacci = [1,2]
temp = 0

while True:
		temp = fibonacci[x]+fibonacci[x-1]
		if(temp < 4000000):
			fibonacci.append(temp)
			x = x + 1
		else:
			break

total = 0
for x in fibonacci:
	if(x%2==0):
		total = total + x

print total
