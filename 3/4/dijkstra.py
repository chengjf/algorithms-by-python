## -*- coding: utf-8 -*-
import copy
def dijkstra(G,s):
	d = []

	for i in G.keys():
		d.append(1000)
	d[s] = 0
	S = []
	Q = copy.copy(d)

	while len(S) != len(G):

		Q = copy.copy(d)
		for i in S:
			Q[i] = 10000
		value = min(Q)
		u = Q.index(value)
		S.append(u)

		for v in G[u]:
			relax(G,u,v,d)


	return d

def getV(G):
	sum = 0
	for i in G.keys():
		sum += len(G[i].values())
	return sum

def getW(G,u,v):
	temp = G[u]
	return temp[v]

def extract_min(Q):
	tmp = Q[0]
	Q.remove(tmp)
	return tmp

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
	#G={0: {1: 1, 2: 3}, 1: {2: 1, 3: 3, 4: 0}, 2: {}, 3: {1: 0, 2: 2}, 4: {3: 0}, 5: {0: 0, 1: 2, 2: 0, 3: 3, 4: 0}}
	print dijkstra(G,0)