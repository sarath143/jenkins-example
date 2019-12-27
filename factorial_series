import sys
import math

def generate_numbers(number):
	a = 1
	for i in range(1, number+1):
		a *= i
		yield a
		
number = int(sys.argv[1])
for x in generate_numbers(number):
	print(x)
