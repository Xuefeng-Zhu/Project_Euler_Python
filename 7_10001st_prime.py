# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?
def is_Prime(n):
	for i in xrange(3, int(n ** 0.5)+1, 2):
		if n % i == 0:
			return False
	return True

if __name__ == '__main__':
	n = 10001
	count = 1
	i = 1
	while count < n:
		i += 2
		if is_Prime(i):
			count += 1
	print i