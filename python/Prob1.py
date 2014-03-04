#!/usr/bin/python

import time

i = 1000
sum = 0

start = time.time()

for x in range(0,i):
	if(x%3==0 or x%5==0):
		sum = sum + x

end = time.time()

print("<Python> Sum of digits less than %d: %d  (found in %s)" % (i,sum,str(end-start)))
