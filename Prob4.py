topscore = 0

for x in range(100,999):
	for i in range(100,999):
		if (str(x*i)==str(x*i)[::-1]) and (x*i>=topscore):
			topscore = x*i
			print str(x) + " x " + str(i) + " = " + str(topscore)

print "topscore: " + str(topscore)
