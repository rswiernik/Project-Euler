i = 0
multiples = 0

for x in range(0,1000):
	if(x%3==0 or x%5==0):
		multiples= multiples + x
		i = i + 1

print multiples
