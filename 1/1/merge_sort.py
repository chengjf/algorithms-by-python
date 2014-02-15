def test(a,b):
	if b.__eq__(a.sort()):
		print "right"
	else:
		print "wrong"

def merge(A,p,q,r):
	#A[p,q],A[q+1,r]
	n1=q-p+1
	n2=r-q
	##print n1,n2
	L=[]
	R=[]
	for i in range(0,n1):
		L.append(A[p+i])
		##print L[i]
	for j in range(0,n2):
		R.append(A[q+j+1])
		##print R[j]
	i=0
	j=0
	L.append(100000)
	R.append(100000)
	for k in range(p,r+1):
		if L[i]<=R[j]:
			A[k]=L[i]
			i=i+1
		else:
			A[k]=R[j]
			j=j+1

def merge_sort(A,p,r):
	#two arguments,p is the begin,r is the end,all include
	#if p=r,don't neet to merge.it's it
	if p<r:
		q=(p+r)/2
		#divide to tow part,A[p,q] and A[q+1,r]
		merge_sort(A,p,q)
		merge_sort(A,q+1,r)
		merge(A,p,q,r)

if __name__=="__main__":
	a=[2,1,6,9,4,7]
	b=a
	print a
	merge_sort(a,0,len(a)-1)
	#test(b,a)
	print a
