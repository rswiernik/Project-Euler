#!/usr/bin/python

import math
import time

def factorPrimes(num):
	highestFactor = 0
	for cur_num in range(2,int(math.sqrt(num)+1)):
		isprime = True
		for x in range(2, int(math.sqrt(cur_num) + 1)):
			if cur_num % x == 0: 
				isprime = False
				break
		if isprime:
			if( isprime and num % cur_num == 0):
				highestFactor = cur_num
	print highestFactor

start = time.time()
factorPrimes(600851475143)
print "Time to calculate: %s seconds" % ((time.time()-start))
