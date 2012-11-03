## -*- coding: utf-8 -*-
def knapsack_dp(v,w,n,W):
	c = [[0 for i in range(W+1)] for j in range(n+1)]
	b = [[0 for i in range(W+1)] for j in range(n+1)]
	#for i in c:
	#	print i
	for i in range(1,n+1,1):
		#print i
		for j in range(1,W+1,1):
			#print i,j
			if w[i] <= j:
				if v[i] + c[i-1][j-w[i]] > c[i-1][j]:
					c[i][j] = v[i] + c[i-1][j-w[i]]
					b[i][j] = '$'
				else:
					c[i][j] = c[i-1][j]
					b[i][j] = '^'
			else:
				c[i][j] = c[i-1][j]
				b[i][j] = '^'

	return c,b

def print_path(b,w,n,W):
	if b[n][W] == "^":
		print_path(b,w,n-1,W)
	if b[n][W] == "$":

		print_path(b,w,n-1,W-w[n])
		print n










if __name__ == "__main__":
	n = 5
	w = ['a',1,2,5,6,7]
	v = ['a',1,6,18,22,28]
	W = 11

	n = 5
	W = 100
	w = ['a',10,20,30,40,50]
	v = ['a',20,30,65,40,60]
	c,b = knapsack_dp(v,w,n,W)
	print_path(b,w,n,W)