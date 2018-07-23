#!/user/bin/env python3
#coding:utf-8
'''from contextlib import contextmanager

class Query(object):
	def __init__(self,name):
		self.name = name

	def query(self):
		print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
	print('Begin')
	q = Query(name)
	yield q
	print('End')

with create_query('Bob') as q:
	print(q.query()) '''

from contextlib import contextmanager
@contextmanager
def tag(name):
	print("<%s>" % name)
	yield
	print("</%s>" % name)

with tag("h1"):
	print('hello') 
	print('world')