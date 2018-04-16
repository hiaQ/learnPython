#!/user/bin/env python3
#coding:utf-8
#@property only read
class Student(object):
	@property
	def birth(self):
		return self._birth
	@birth.setter
	def birth(self,value):
		self._birth = value
	@property
	def age(self):
		return 2018-self._birth

s = Student()
s.birth = 1995
print(s.birth)
print(s.age)