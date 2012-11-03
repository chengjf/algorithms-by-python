## -*- coding: utf-8 -*-
import sys
def lcs_length(x,y):
	m = len(x)
	n = len(y)
	c = [[0 for i in range(n)]for j in range(m)]
	b = [[0 for i in range(n)]for j in range(m)]

	for i in range(1,m,1):
		for j in range(1,n,1):
			if x[i] == y[j]:
				c[i][j] = c[i-1][j-1] + 1
				b[i][j] = 0
			elif c[i-1][j] >= c[i][j-1]:
				c[i][j] = c[i-1][j]
				b[i][j] = 1
			else:
				c[i][j] = c[i][j-1]
				b[i][j] = 2
	print
	return (c,b)

def print_lcs(b,x,i,j):
	if i == 0 or j == 0:
		return
	if b[i][j] == 0:
		print_lcs(b,x,i-1,j-1)
		sys.stdout.write(x[i])
	elif b[i][j] == 1:
		print_lcs(b,x,i-1,j)
	else:
		print_lcs(b,x,i,j-1)

if __name__ == "__main__":
	x='0xzyzzyx'
	y='0zxyyzxz'
	(c,b) = lcs_length(x,y)
	print_lcs(b,x,len(x)-1,len(y)-1)
	x='0MAEEEVAKLEKHLMLLRQEYVKLQKKLAETEKRCALLAAQANKESSSESFISRLLAIVAD'
	y='0MAEEEVAKLEKHLMLLRQEYVKLQKKLAETEKRCTLLAAQANKENSNESFISRLLAIVAG'
	(c,b) = lcs_length(x,y)
	print_lcs(b,x,len(x)-1,len(y)-1)
	x='010010101'
	y='0010110110'
	(c,b) = lcs_length(x,y)
	print_lcs(b,x,len(x)-1,len(y)-1)