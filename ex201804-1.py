#!/user/bin/env python
#coding:utf-8

class Student(object):
    def __init__(self):
        pass
def set_age(self,age):
    self.age = age
Student.set_age = set_age

s = Student()
from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age) 

#给一个实例绑定方法，对另一个实例是不起作用的
s2 = Student() 
s2.set_age(25)
print(s2.age)