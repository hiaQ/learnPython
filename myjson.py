#!/user/bin/env python3
#coding:utf-8

import json

class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score =score

def student2dict(std):
	return {'name':std.name,'age':std.age,'score':std.score}

s = Student('Bob',20,88)
print(json.dumps(s, default = student2dict)) 
#给类序列化的另一种方法__dict__
print(json.dumps(s,default = lambda obj:obj.__dict__))