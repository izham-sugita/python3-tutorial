#! /usr/bin/env python3

from numpy import mean, arange

total = 10000000

a = arange(total)

for i in range(10):
	avg = mean(a)
	
print("Average is %f"%(avg))
