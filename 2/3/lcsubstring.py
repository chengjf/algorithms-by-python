def lcsubstring(x,y):
	l = [[0 for i in range(len(x))]for i in range(len(y))]

	z=0
	ret=[]

	for i in range(0,len(x),1):
		for j in range(0,len(y),1):
			if x[i] == y[j]:
				if i == 0 or j == 0:
					l[i][j] = 1
				else:
					l[i][j] = l[i-1][j-1] + 1
				if l[i][j] > z:
					z = l[i][j]
					ret = []
				if l[i][j] == z:
					ret.extend(x[i-z+1:i+1])
			else:
				l[i][j] = 0;
	print z
	return ret

if __name__ == "__main__":
	x='xzyzzyx'
	y='zxyyzxz'
	print lcsubstring(x,y)
	x='MAEEEVAKLEKHLMLLRQEYVKLQKKLAETEKRCALLAAQANKESSSESFISRLLAIVAD'
	y='MAEEEVAKLEKHLMLLRQEYVKLQKKLAETEKRCTLLAAQANKENSNESFISRLLAIVAG'
	print lcsubstring(x,y)
