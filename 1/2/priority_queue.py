from random import randint
from heap_sort import max_heapify,build_max_heap,parent

class priority_queue:

	def __init__(self,a):
		build_max_heap(a)
		self.queue=a
	def heap_size(self):
		return len(self.queue)-1
	def insert(self,key):
		# self.heap_size += 1
		self.queue.append(-1)
		self.increase_key(self.heap_size(),key)
	def maximum(self):
		return self.queue[1] 

	def extract_max(self):
		if self.heap_size()<1:
			raise "heap underflow"
		maxnum=self.queue[1]
		self.queue[1]=self.queue[self.heap_size()]
		self.queue.pop()
		# self.heap_size -= 1
		heap_size=self.heap_size()
		max_heapify(self.queue,1,heap_size)
		return maxnum

	def increase_key(self,i,key):
		if key<self.queue[i]:
			raise "new key is samller than current key"
		self.queue[i]=key
		while i>1 and self.queue[parent(i)]<self.queue[i]:
			self.queue[i],self.queue[parent(i)]=self.queue[parent(i)],self.queue[i]
			i=parent(i)


if __name__ == "__main__":
	a=[0,10,50,30,40]
	print "Build priority_queue from\n",a

	queue=priority_queue(a)
	print "The priority-queue is:\n",queue.queue

	print "The maximum of this priority_queue is:\n",queue.maximum()

	print "Increase 30 to 90"
	queue.increase_key(3,90)
	print queue.queue

	print "Insert into 23"
	queue.insert(23)
	print queue.queue

	print "Insert into 100"
	queue.insert(100)
	print queue.queue

	for i in range(queue.heap_size()):
		print queue.extract_max()