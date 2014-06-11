# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from operator import mul
if __name__ == '__main__':
	facList = []
	for i in xrange(2,21):
		for num in facList:
			if i % num == 0:
				i /= num 
		else:
			if i > 1:
				facList.append(i)
	print reduce(mul, facList)