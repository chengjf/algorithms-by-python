from random import randint

def partition(A,p,r):
	#A[p,r]
	x=A[r]
	i=p-1
	# print p,r
	for j in range(p,r):
		global count
		count += 1
		if A[j]<=x:
			i+=1
			A[i],A[j]=A[j],A[i]
	A[i+1],A[r]=A[r],A[i+1]
	# print count
	# print i+1
	return i+1

def quicksort(A,p,r):
	if p<r:
		q=partition(A,p,r)
		quicksort(A,p,q-1)  #not include q
		quicksort(A,q+1,r)  #not include q
def test():
	a=[]
	for i in range(10):
		a.append(randint(0,100))
	print a
	quicksort(a,0,len(a)-1)
	print a
def maximum_test():
	global count
	count=0
	a=[]
	for i in range(11):
		a.append(1)
	print a
	quicksort(a,0,len(a)-1)
	print a
	print count
def minimum_test():
	global count
	count=0
	# b=[0,1,3,4,2,8,6,7,9,10,5]
	# b=[12,13,17,19,15,23,21,22,24,25,20]
	b=[0,1,3,4,2,8,6,7,9,10,5,20,12,13,17,19,15,23,21,22,24,25,11]
	print b
	quicksort(b,0,len(b)-1)
	print b
	print count

if __name__=="__main__":
	# maximum_test()
	minimum_test()