# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
#reference http://www.daniweb.com/software-development/python/code/216558/prime-number-generator-python

def getPML(n):
	candidates = range(3, n+1, 2)
	length = len(candidates)
	mroot = n ** 0.5
	i = 0
	m = 3
	while m <= mroot:
		if candidates[i]:
			temp = (m * m - 3) / 2
			while temp < length:
				candidates[temp] = 0
				temp += m
		i += 1
		m += 2 
	return [2]+[i for i in candidates if i]

if __name__ == '__main__':
	n = 2000000
	PMlist  = getPML(n)
	print sum(PMlist)


	