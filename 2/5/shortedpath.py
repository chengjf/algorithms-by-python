def bellman_ford(G,start,end):

	d = []

	b = [0 for i in range(end - start + 1)]
	#print b
	for i in G.keys():
		d.append(100000)
	d[start] = 0

	for i in range(len(G.keys())):# loop(V-1)
		#print i
		for u in G.keys():
			#print u
			for v in G[u]:
				if d[v] > d[u] + getW(G,u,v):
					d[v] = d[u] + getW(G,u,v)
					b[v] = u
	for u in G.keys():
		for v in G[u]:
			if d[v] > d[u] +getW(G,u,v):
				return False

	#print b
	return d,b

def getV(G):
	sum = 0
	for i in G.keys():
		sum += len(G[i].values())
	return sum

def getW(G,u,v):
	temp = G[u]
	return temp[v]

def print_path(b,start,end):
	if end != 0:
		print_path(b,start,b[end])
		print end


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

	#print getV(G)
	#print getW(G,0,1)

	d,b = bellman_ford(G,0,15)
	print d
	print b
	print_path(b,0,15)