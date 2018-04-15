#!/user/bin/env python3
#coding:utf-8
#study from michaelliao
class Student(object):
	__slots__ = ('name','age')

class GraduateStudent(Student):
	pass

s = Student()
s.name = 'Wendy'
s.age = 23
#Error:AttributeError:'Student' object has no attribue 'score'
try:
	s.score = 95
except AttributeError as e:
	print('AttributeError:',e)

g = GraduateStudent()
g.score = 90
print('g.score=',g.score)