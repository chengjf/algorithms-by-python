from merge_sort import merge_sort
from binary_search import binary_search
from random import randint

def sum_exist(a,x):
	
	merge_sort(a,0,len(a)-1)
	##print a
	for i in range(len(a)):
		#binary_search(list,begin,end,key)
		if binary_search(a,i,len(a)-1,x-a[i]):
			return True
	return False

if __name__ == "__main__":
	a=[]
	for i in range(20):
		a.append(randint(0,100))
	print a
	x=input()
	print sum_exist(a,x)