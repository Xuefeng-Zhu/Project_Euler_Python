from operator import mul
n = 20
size = 4 
def process(x, y, grid):
	right, down, rightDown, leftDown = 4 * [0]
	if x <= n - size:
		right = reduce(mul, grid[y][x:x+size])
	if y <= n - size:
		 down = reduce(mul, [grid[i][x] for i in xrange(y,y+size)])
	if x <= n - size and y <= n - size:
		rightDown = reduce(mul, [grid[x+i][y+i] for i in xrange(size)])
		leftDown = reduce(mul, [grid[x+size-1-i][y+i] for i in xrange(size)])

	return max(right, down, rightDown, leftDown)

if __name__ == '__main__':
	file = open("11_grid.txt")
	grid = []
	for line in file:
		grid.append(map(int,line.split()))
	print max(process(i,j,grid)for i in xrange(n) for j in xrange(n))

			