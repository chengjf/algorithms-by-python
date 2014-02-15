## -*- coding: utf-8 -*-
def greedy_knapsack(p,w,W,x,n):
	#x = []
	c = W
	for i in range(0,n,1):
		if w[i] <= c:
			x[i] = 1
			c = c - w[i]
		else:
			break
	if i < n:
		x[i] = c * 1.0 / w[i]
	return x

def sort_pw(p,w):
	temp = {}
	for i in range(len(p)):
		temp.update({i:p[i] * 1.0 / w[i]})

	result = sorted(temp.items(),key = lambda temp:temp[1])

	temp_p = [0] * len(p)
	temp_w = [0] * len(p)


	flag = len(p) - 1

	for i in result:
		index = i[0]
		temp_p[flag] = p[index]
		temp_w[flag] = w[index]
		flag -= 1


	#print temp_p,temp_w
	return temp_p,temp_w




	return (p,w)
if __name__ == "__main__":
	p = [20,30,65,40,60]
	w = [10,20,30,40,50]

	W = 100
	n = 5
	x =[0,0,0,0,0]
	p,w = sort_pw(p,w)
	print p
	print w
	print greedy_knapsack(p,w,W,x,n)