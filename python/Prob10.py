#!/usr/bin/python

import math

def sumPrimes(limit):
	sum = 0
	for cur_num in range(2,limit):
		isprime = True
		for x in range(2, int(sqrt(cur_num) + 1)):
			if cur_num % x == 0: 
				isprime = False
				break
		if isprime:
			sum = sum+cur_num
	print sum

sumPrimes(2000000)
