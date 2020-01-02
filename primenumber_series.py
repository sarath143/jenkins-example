import sys
import math
import time
def generate_numbers(number):
	for num in range(1, number + 1):
   # all prime numbers are greater than 1
		if num > 1:
			for i in range(2, num):
				if (num % i) == 0:
					break
			else:
				print(num)
		time.sleep(3)

number = int(sys.argv[1])
generate_numbers(number)
