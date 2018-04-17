#!/user/bin/env python3
#coding:utf-8
#实现一个定制类，便于链式调用
class chain(object):
	"""docstring for chain"""
	def __init__(self, path = ''):
		self.path = path
	#调用print()打印path
	def __str__(self):
		return self.path
	#当对实例进行调用a('xxx')时将path连接并返回一个新的实例
	def __call__(self,path):
		return chain('%s/%s' % (self.path,path))
	def __getattr__(self,item):
		return chain('%s/%s' % (self.path,item))
	__repr__ = __str__

c = chain() 
print(c.users('wendy').repos('xxx')) 
print(c.status.user.timeline.list)