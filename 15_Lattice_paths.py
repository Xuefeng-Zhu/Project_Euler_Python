# How many such routes are there through a 20×20 grid?

import scipy.misc as sc
if __name__ == '__main__':
	print sc.comb(40, 20, exact=True)