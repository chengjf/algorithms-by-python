def parent(i):
	return i/2

def left(i):
	return 2*i

def right(i):
	return 2*i+1


def max_heapify(a,i,heap_size):
	#find the right place for a[i]
	#print heap_size
	l=left(i)
	r=right(i)
	if l<=heap_size and a[l]>a[i]:
		largest=l
	else:
		largest=i
	if r<=heap_size and a[r]>a[largest]:
		largest=r
	if largest!=i:
		a[i],a[largest]=a[largest],a[i]
		max_heapify(a,largest,heap_size)

def build_max_heap(a):
	#for all nonleaf do max_heapify
	#global heap_size
	heap_size=len(a)-1 #a[0] is Placeholder,so...
	for i in range((len(a)-1)/2,0,-1):#(len(a)-1) is the number that is not the leaf
		max_heapify(a,i,heap_size)

def heap_sort(a):
	build_max_heap(a)
	#global heap_size
	heap_size=len(a)-1
	for i in range(len(a)-1,1,-1):
		a[1],a[i]=a[i],a[1]
		heap_size -= 1
		max_heapify(a,1,heap_size)

if __name__ == "__main__":
	a=[-100,4,1,3,2,16,9,10,14,8,7]
	print a[1:]
	# a=[1,2,3]
	heap_sort(a)
	print a[1:]