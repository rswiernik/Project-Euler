answer = 20
found = False

while True:
	if all( answer%x==0 for x in range(10,20) ):
		break
	answer = answer + 20

print answer
