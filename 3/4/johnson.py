## -*- coding: utf-8 -*-
import copy
from bellman_ford import bellman_ford
from dijkstra import dijkstra
def johnson(G):
	duv = [[0 for i in range(len(G))]for j in range(len(G))]

	_G = copy.copy(G)
	x = len(G)
	tmp = {}
	for i in G.keys():
		tmp.update({i:0})
	_G.update({x:tmp})

	d = bellman_ford(_G,x)

	if d == False:
		print "the input graph contains a negative-weight cycle"
		return
	else:
		h = {}
		for i in _G.keys():
			h.update({i:d[i]})
		#print 'h:',h

		for u in _G.keys():
			for v in _G[u]:
				_G[u][v] = _G[u][v] + h[u] - h[v]
		#print _G

		for u in G.keys():
			d = dijkstra(_G,u)
			#print u,d
			for v in G.keys():

				duv[u][v] = d[v] + h[v] - h[u]

	return duv








def getV(G):
	V = []
	for i in G.keys():
		v.append(i)
	return V

def getW(G,u,v):
	temp = G[u]
	return temp[v]


if __name__ == "__main__":
	G = {
		0:{1:-1,2:3},
		1:{2:3,3:2,4:2},
		2:{},
		3:{1:1,2:5},
		4:{3:-3},
		}
	for i in johnson(G):
		print i