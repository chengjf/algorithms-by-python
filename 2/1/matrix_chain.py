import sys

##
##
def matrix_chain_order (p):
	n=len(p)-1
	m=[[0 for col in range(n+1)] for row in range(n+1)]
	s=[[0 for col in range(n+1)] for row in range(n+1)]

	for l in range(2,n+1):
		for i in range(1,n-l+1+1):
			j=i+l-1
			m[i][j]=100000
			for k in range(i,j):
				q=m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
				if q<m[i][j]:
					m[i][j]=q
					s[i][j]=k
			#show(m)
			#show(s)
	return (m,s)

##
##'
def print_optimal_parens(s,i,j):
	if i == j:
		s='A%d'%i
		sys.stdout.write(s)
	else:
		sys.stdout.write("(")
		print_optimal_parens(s,i,s[i][j])
		print_optimal_parens(s,s[i][j]+1,j)
		sys.stdout.write(")")






def show(m):
	for i in m:
		print i


if __name__=="__main__":
	#p=[30,35,15,5,10,20,25]
	p=[5,10,3,12,5,50,6]
	show(matrix_chain_order(p)[0])
	show(matrix_chain_order(p)[1])
	print_optimal_parens(matrix_chain_order(p)[1],1,6)


