#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

n = 5
runsum = 0
factorial = 1

for i in range(1, n+1):
	runsum += i # computes the running sum from 1 to 5 (we set the range 1, n+1)
	factorial *= i # computes factorial of n = 5
print(n, runsum, factorial)

"""
5 15 120
"""
