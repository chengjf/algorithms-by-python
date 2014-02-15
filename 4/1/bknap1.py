## -*- coding: utf-8 -*-
import copy
def bknap1(M,n,W,P,fw,fp,X):
	cw,cp = 0,0
	k = 1
	fp = -1
	Y = [0 for i in range(n+1)]
	#print Y
	while 1:
		#print k
		while k <= n and cw + W[k] <= M:
			cw = cw + W[k]
			cp = cp + P[k]
			Y[k] = 1
			k += 1
			print cw,cp,k
			#print Y

		if k > n:
			fp = cp
			fw = cw
			k = n
			#fuck this,must use copy.copy!!!
			X = copy.copy(Y)

			#print X
		else:
			Y[k] = 0

		#print X
		while bound(cp,cw,k,M) <= fp:

			while k != 0 and Y[k] != 1:
				k -= 1

			if k == 0:

				print fw,fp

				return X
			Y[k] = 0
			cw = cw - W[k]
			cp = cp - P[k]
		k += 1


def bound(p,w,k,M):
	print k
	b = p
	c = w
	for i in range(k+1,n+1,1):
		c = c + W[i]
		if c < M:
			b = b + P[i]
		else:
			print (b*1.0+1.0*(1-1.0*(c-M)/W[i])*P[i])
			return (b*1.0+1.0*(1-1.0*(c-M)/W[i])*P[i])
	print b
	return b






if __name__ == "__main__":
	P = [0,11,21,31,33,43,53,55,65]
	W = [0,1,11,21,23,33,43,45,55]
	P = [0,65,20,30,60,40]
	W = [0,30,10,20,50,40]
	M = 100
	n = len(P)-1
	fw = 0
	fp = 0
	X = [0 for i in range(len(P))]
	print bknap1(M,n,W,P,fw,fp,X)
