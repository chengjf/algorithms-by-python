## -*- coding: utf-8 -*-
def dpmaxsum(a,n):
	sum = 0
	b = 0
	for i in range(0,n,1):
		if b > 0:
			b += a[i]
		else:
			b = a[i]
		if b > sum:
			sum = b
	return sum

def dpmaxsum1(a,n):
	sum = a[0]
	b=[0 for i in range(len(a))]
	b[0] =a[0]
	for i in range(1,n,1):
		if b[i-1] > 0:
			b[i] = b[i-1] + a[i]
		else:
			b[i] = a[i]
		if b[i] > sum:
			sum = b[i]
	return sum

if __name__ == "__main__":
	a=[-2,11,-4,13,-5,-2]
	print dpmaxsum(a,len(a))
