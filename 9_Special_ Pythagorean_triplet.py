# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

if __name__ == '__main__':
	n = 1000000
	for a in xrange(1, n/3):
		for b in xrange(a+1, (n-a)/2):
			c = n - a - b
			if (a**2 + b**2 == c**2):
				print a * b * c
				exit()
