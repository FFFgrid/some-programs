from collections import deque
class HashTable():
	def __init__(self, size):
		self.HashSize = size #size是哈希表的大小（可以存放余数从0到size-1）
		self.Table = [None]*size
	def insert(self, data):
		i = data % self.HashSize #散列函数
		if self.Table[i] == None:
			self.Table[i] = deque([data]) #deque([iterable[, maxlen]]) 返回一个新的双向队列对象
		else:
			if data not in self.Table[i]:
				self.Table[i].append(data)
		return i		
	def search(self, data):
		i = data % self.HashSize
		if self.Table[i] != None and data in self.Table[i]:
			return i
		return -1

	def delete(self, data):
		i = data % self.HashSize
		if self.Table[i] != None and data in self.Table[i]:
			del self.Table[i][self.Table[i].index(data)]
			if len(self.Table[i]) == 0:
				self.Table[i] = None
			return i
		else:
			return -1	
