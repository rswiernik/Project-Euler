#!/usr/bin/python

import math

def nthPrime(n):
	inc = 0
	count = 2
	n+=1
	while count <= n:
		isprime = True
		for x in range(2, int(math.sqrt(inc) + 1)):
			if inc % x == 0: 
				isprime = False
				break
		if count == n:
			print inc
			break
		if isprime:
			print str(count) + " " + str(inc)
			count = count + 1
		inc = inc + 1

nthPrime(10001)
#nthPrime(10)
