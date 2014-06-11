if __name__ == '__main__':
	fbList = [1, 2]
	while fbList[-1] < 4000000:
		fbList.append(fbList[-1] + fbList[-2]);
	print sum([i for i in fbList if i % 2 == 0])