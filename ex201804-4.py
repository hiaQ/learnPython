#!/user/bin/env python3
#coding:utf-8
#以菲波拉契数为例，写一个Fib类，可以用于for循环
class Fib(object):
	def __init__(self):
		self.a, self.b = 0,1 #初始化
	def __iter__(self):
		#实例本身就是迭代对象，故返回自己
		return self 
	def __next__(self):
		#计算下一个值
		self.a, self.b = self.b, self.a+self.b
		if self.a > 100:  #退出循环的条件
			raise StopIteration()
		return self.a

for n in Fib():
	print(n) 