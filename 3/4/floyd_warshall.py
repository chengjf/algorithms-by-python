## -*- coding: utf-8 -*-
def floyd_warshall(W):
	n = len(W)
	D=[[[[] for i in range(n)]for j in range(n)]for k in range(n+1)]
#	for i in range(n+1):
#		for j in range(n):
#			for k in range(n):
#				D[i][j][k] = N
	D[0] = W
	for k in range(1,n+1):
		for i in range(0,n):
			for j in range(0,n):
				D[k][i][j] = min(D[k-1][i][j],D[k-1][i][k-1] + D[k-1][k-1][j])


	return D


def printf(D):
	for i in D:
		for j in i:
			print j
		print
if __name__ == "__main__":
	N = 10000
	W = [[0,3,8,N,-4],[N,0,N,1,7],[N,4,0,N,N],[2,N,-5,0,N],[N,N,N,6,0]]
	W=[[0,N,N,N,-1,N],
		[1,0,N,2,N,N],
		[N,2,0,N,N,-8],
		[-4,N,N,0,3,N],
		[N,7,N,N,0,N],
		[N,5,10,N,N,0]]
	W = [[0,-1,3,N,N],
		 [N,0,3,2,2],
		 [N,N,0,N,N],
		 [N,1,5,0,N],
		 [N,N,N,-3,0]
		]
	tmp = floyd_warshall(W)
	printf(tmp)