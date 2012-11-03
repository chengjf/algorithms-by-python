## -*- coding: utf-8 -*-
def nqueens(n):
	k = 1
	X=[0 for i in range(n+1)]
	X[1] = 0

	num = 0
	while k > 0:
		X[k] += 1
		while X[k] <= n and not place(X,k):
			X[k] += 1
		if X[k] <= n:
			if k == n:
				print X
				num += 1
			else:
				k = k+1
				X[k] = 0
		else:
			k -=1
	print num

def place(X,k):
	i = 1
	while i < k:
		if X[i] == X[k] or abs(X[i] - X[k]) == abs(i - k):
			return False
		i += 1
	return True


if __name__ == "__main__":
	nqueens(100)