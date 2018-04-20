#!/user/bin/env python3
#coding:utf-8
#对Student类编写单元测试，结果发现测试不通过，请修改Student
#让测试通过
import unittest
class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score
	def get_grade(self):
			if 0 <= self.score and self.score < 60 :
				return 'C'
			elif 60 <= self.score and self.score < 80:
				return 'B'
			elif 80 <= self.score and self.score <= 100:
				return 'A'
			else:
				raise ValueError('score is not between 0 and 100')

