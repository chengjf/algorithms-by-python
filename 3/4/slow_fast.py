## -*- coding: utf-8 -*-
def extend_shortest_paths(L,W):

	n = len(L)
	tmp = [[NaN for j in range(n)]for i in range(n)]
	#print l

	for i in range(n):
		for j in range(n):
			if i == j:
				tmp[i][j] = 0
			for k in range(n):

				tmp[i][j] = min(tmp[i][j],L[i][k]+W[k][j])
	return tmp

def slow_all_pairs_shortest_paths(W):
	n = len(W)
	l = [[]for i in range(n)]
	l[0] = W
	for i in range(1,n-1):
		l[i] = extend_shortest_paths(l[i-1],W)
		#print l[i]

	return l
def faster_all_pairs_shortest_paths(W):
	n = len(W)
	l = [[]for i in range(n+1)]
	l[1] = W
	m = 1
	while m < n-2:
		l[2*m] = extend_shortest_paths(l[m],l[m])
		m = m * 2
	print m
	return l[m]


if __name__ == "__main__":

	NaN = 100000

	W=[[0,3,8,NaN,-4],[NaN,0,NaN,1,7],[NaN,4,0,NaN,NaN],[2,NaN,-5,0,NaN],[NaN,NaN,NaN,6,0]]
	W=[[0,NaN,NaN,NaN,-1,NaN],[1,0,NaN,2,NaN,NaN],[NaN,2,0,NaN,NaN,-8],[-4,NaN,NaN,0,3,NaN],[NaN,7,NaN,NaN,0,NaN],[NaN,5,10,NaN,NaN,0]]
	#n = len(W)
	#L = [[NaN for j in range(n)]for i in range(n)]

	#print extend_shortest_paths(W,W)
	tmp = slow_all_pairs_shortest_paths(W)
	tmp = faster_all_pairs_shortest_paths(W)
	for i in tmp:
		print i
	for i in tmp:
		print '----------'
		for j in i:
			print j
