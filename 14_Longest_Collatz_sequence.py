# The following iterative sequence is defined for the set of positive integers:

# Using the rule above and starting with 13, we generate the following sequence:

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

# Initially, I try to solve it recursively starting from 1, but it causes stack overflow. Use brute force int the end

from collections import deque
maxLen,maxNum,cache = 0,0,{1:1}
def cacheChain(chain, rest):
	global maxLen,maxNum,cache
	if len(chain)+rest > maxLen:
		maxLen,maxNum = len(chain)+rest,chain[0]
	while len(chain):
		cache[chain[0]] = len(chain)+rest
		chain.popleft()
	
if __name__ == '__main__':
	for n in xrange(2,10**6):
		chain = deque()
		while n!=1:
			chain.append(n)
			n = (n/2) if n%2==0 else 3*n+1
			if n in cache:
				cacheChain(chain, cache[n])
				break
	print maxNum
