#!/user/bin/env python3
#coding:utf-8
#请把下面的Student对象的gender字段对外隐藏起来，然
#后用get_gender()和set_gender()代替，并检查参数的有效性

class Student(object):
	def __init__(self,name,gender):
		self.name = name
		self.__gender = gender

	def get_gender(self):
		return self.__gender

	def set_gender(self,gender):
		if gender in ('male','female'):
			self.__gender = gender
		else:
			return ValueError('Wrong gender')

	def print_student(self):
		print("%s:%s" % (self.name,self.__gender))

bart = Student('Bart','male')
print('bart.get_gender():',bart.get_gender())
print('==============')
bart.set_gender('female')
bart.print_student()