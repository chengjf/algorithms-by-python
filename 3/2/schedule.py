## -*- coding: utf-8 -*-
def schedule(W):
	print W

	n = len(W)
	s = [0]*n
	#print s
#	for i in range(n):
#		s[i] = min(W)
#		#print min(W)
#		W.remove(s[i])
	s = W
	s.sort()
	print s


if __name__ == "__main__":
	W = [15,8,3,10]
	schedule(W)