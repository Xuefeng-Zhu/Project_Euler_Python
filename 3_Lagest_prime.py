# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


#reference http://www.daniweb.com/software-development/python/code/216558/prime-number-generator-python

if __name__ == '__main__':
	n = 600851475143
	low = 2
	while low < n:
		if n % low == 0:
			n /= low
		else:
			low += 1
	print n
	