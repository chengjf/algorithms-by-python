from random import randint
def binary_search(s,begin,end,key):
	#s[begin,end] search key
	if begin<=end:
		mid=(begin+end)/2
		if s[mid]==key:
			return True
		elif s[mid]>key:
			return binary_search(s,begin,mid-1,key) #not include mid
		else:
			return binary_search(s,mid+1,end,key) #not include mid
	else:
		return False


if __name__=="__main__":
	a=[]
	for i in range(20):
		a.append(randint(0,100))
	a.sort()
	print a
	key=input()
	print(binary_search(a,0,len(a)-1,key))