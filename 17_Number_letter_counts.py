if __name__ == '__main__':
	numDict = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3,
	11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6, 
	30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6}
	result = 0
	for num in xrange(1,1000):
		hundred = num / 100
		rest = num % 100
		if hundred:
			result += numDict[hundred] + (10 if rest else 7)
		if rest:
			if numDict.get(rest):
				result += numDict[rest]
			else:
				digit = rest % 10
				ten = rest - digit
				result += numDict[digit] + numDict[ten]
	print result + 11



