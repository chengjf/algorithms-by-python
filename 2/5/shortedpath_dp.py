## -*- coding: utf-8 -*-
import sys
def shortedpath_dp(G,start,end):
	b = [10000 for i in range(end - start + 1)]
	d = [0 for i in range(end - start + 1)]

	b[start] = 0
	count = 0
	for i in range(start + 1,end + 1,1):
		for j in getPre(G,i):
			count += 1
			if b[j] + getW(G,j,i) <= b[i]:
				b[i] = b[j] + getW(G,j,i)
				d[i] = j
	print d
	print count
	return d







def getPre(G,v):
	pre = []
	for i in G:
		#print G[i]
		temp = G[i]
		for j in temp.keys():
			if j == v:
				pre.append(i)
	return pre


def getW(G,u,v):
	temp = G[u]
	return temp[v]

def print_path(b,start,end):
	if end != 0:
		print_path(b,start,b[end])
		temp = str(end)+'->'
		sys.stdout.write(temp)



if __name__ == "__main__":
	G = {
		0:{1:5,2:3},
		1:{3:1,4:3,5:6},
		2:{4:6,5:7,6:6},
		3:{7:6,8:8},
		4:{7:3,8:5},
		5:{8:3,9:3},
		6:{8:8,9:4},
		7:{10:2,11:2},
		8:{11:1,12:2},
		9:{11:3,12:3},
		10:{13:3,14:5},
		11:{13:5,14:2},
		12:{13:6,14:6},
		13:{15:4},
		14:{15:3},
		15:{}
	}

	path = shortedpath_dp(G,0,15)

	print_path(path,0,15)