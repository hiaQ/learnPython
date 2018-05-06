#!/user/bin/env python3
#coding:utf-8
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

	def __init__(self,capacity):
		#super调用父类的一个方法
		super(LastUpdatedOrderedDict,self).__init__()
		self._capacity = capacity

	def __setitem__(self,key,value):
		#如果key存在，那么dict的containsKey设为1，否则为0
		containsKey = 1 if key in self else 0
		'''
		如果当前元素不在dict中，此时dict的长度已经大于自身
		容量，则需要将第一个元素删除
		如果当前元素存在于dict中，此时dict的长度已经大于等
		于自身容量，但减去1就不满足该条件了
		所以这种情况下会将原来存在的元素给覆盖掉而不是去删
		除第一个元素
		'''
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last = False)
			print('remove:',last)
		if containsKey:
			del self[key]
			print('set:',(key,value))
		else:
			print('add:',(key,value))
		OrderedDict.__setitem__(self,key,value)

if __name__ == '__main__':
	fifo = LastUpdatedOrderedDict(3)
	fifo['x'] = 1
	fifo['y'] = 2
	fifo['z'] = 3
	fifo['a'] = 4
	print('fifo = ',fifo)