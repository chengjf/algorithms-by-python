
def fun(a,b,k):
	##a and b is sorted list,find Kth smaller
	##print a,b,k
	if a==[]:
		##print "Answer: ",b[k-1]
		return b[k-1]
	if b==[]:
		##print "Answer: ",a[k-1]
		return a[k-1]

	if k==1:
		##print "Answer: ",min(a[0],b[0])
		return min(a[0],b[0])
	if k==len(a)+len(b):
		##print "Answer: ",max(a[-1],b[-1])
		return max(a[-1],b[-1])

	m=len(a)
	n=len(b)
	x=a[m/2]
	y=b[n/2]
	#a[0,m/2] is m/2+1
	#b[0,n/2] is n/2+1
	#a and b divide two part:m/2+1 and m/2-1
	if k>=(m/2+1+n/2+1):
		if x<y:
			#a[m/2+1:end],b
			return fun(a[m/2+1:],b,k-m/2-1)
		else:
			#a,b[n/2+1:end]
			return fun(a,b[n/2+1:],k-n/2-1)
	else:
		if x<y:
			#a,b[begin,n/2-1]
			return fun(a,b[:n/2],k)
		else:
			#a[begin,m/2-1],b
			return fun(a[:m/2],b,k)

def show(a,b):
	print "a:",a,"b:",b
	for i in range(1,len(a)+len(b)+1):
		print "The",i," is :",fun(a,b,len(a)+len(b)-i+1)
class Test:
	def test1(self):
		##a is [] or b is []
		a=[]
		b=[1,2,3]
		show(a,b)
	def test2(self):
		##a is equal to b
		a=[1,2,3]
		b=a
		show(a,b)
	def test3(self):
		##a is all lower to b
		a=[1,2,3]
		b=[4,5,6,7]
		show(a,b)
	def test4(self):
		##a and b lower and higher by turn
		a=[1,3,5]
		b=[2,4,6]
		show(a,b)
	def go(self):
		self.test1()
		self.test2()
		self.test3()
		self.test4()

if __name__=="__main__":
	test=Test()
	test.go()
