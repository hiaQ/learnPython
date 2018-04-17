#!/user/bin/env python3
#coding:utf-8
class Student(object):
	def __init__(self):
		self.name = 'Wendy'
	'''def __getattr__(self,attr):
		if attr == 'score':
			return 99'''
	def __getattr__(self,attr):
		if attr == 'age':
			return lambda:25

s = Student()
print(s.name) 
#注意函数的调用方式
print(s.age()) 