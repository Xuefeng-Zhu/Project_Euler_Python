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
	