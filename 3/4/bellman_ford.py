def bellman_ford(G,start):

	d = []

	for i in G.keys():
		d.append(100000)
	d[start] = 0

	for i in range(len(G.keys())):# loop(V-1)
		for u in G.keys():
			for v in G[u]:
				relax(G,u,v,d)

	for u in G.keys():
		for v in G[u]:
			if d[v] > d[u] +getW(G,u,v):
				return False

	return d

def getV(G):
	sum = 0
	for i in G.keys():
		sum += len(G[i].values())
	return sum

def getW(G,u,v):
	temp = G[u]
	return temp[v]

def relax(G,u,v,d):
	if d[v] > d[u] + getW(G,u,v):
		d[v] = d[u] + getW(G,u,v)


if __name__ == "__main__":
	G = {
		0:{1:-1,2:3},
		1:{2:3,3:2,4:2},
		2:{},
		3:{1:1,2:5},
		4:{3:-3},
		}
	G = {
		0: {1: -1, 2: 3},
		1: {2: 3, 3: 2, 4: 2},
		2: {},
		3: {1: 1, 2: 5},
		4: {3: -3},
		5: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}}
	#print getV(G)
	#print getW(G,0,1)

	print bellman_ford(G,5)