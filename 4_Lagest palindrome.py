if __name__ == '__main__':
	nums = range(100,1000)
	temp = [i * j for j in nums for i in nums if j <= i and str(i*j) == str(i*j)[::-1]]
	print max(temp)
