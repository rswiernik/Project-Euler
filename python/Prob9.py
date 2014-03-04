#!/usr/bin/python

import math

def isTriple(a,b):
	c = math.sqrt(a**2+b**2)
	return int(c) == c

def findTriple(a,b):
	return int(math.sqrt(a**2+b**2))

for a in range(0,500):
	for b in range(0,500):
		if(isTriple(a,b)):
			c = findTriple(a,b)
			if(a+b+c== 1000):
				print a*b*c
