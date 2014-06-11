# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


if __name__ == '__main__':
	nums = range(100,1000)
	temp = [i * j for j in nums for i in nums if j <= i and str(i*j) == str(i*j)[::-1]]
	print max(temp)
