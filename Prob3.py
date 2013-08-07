# Work in Progress

#x = 600851475143
x = 13195
p = []

for n in range(2, x/2):
	for i in p:
		if(n%i==0):
			break
	else:
		#print "added " + str(n)
		p.append(n)
	#n += 1

highest = 0
for i in p:
	#print "Prime: " + str(i)
	try:
		index = p.index(x%i)
		if(i%1==0 and (x%i)%1==0):
			#print "Updated highest > " + str(i)
			highest = i
	except ValueError:
		break
		#print str(i) + " is not a factor"
			

print highest
