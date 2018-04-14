#!/user/bin/env python
#coding:utf-8
#为了统计学生人数，可以给Student类增加一个类属性，每创
#建一个实例，该属性自动增加

class Student(object):
    count = 0

    def __init__(self,name):
        self.name = name
        Student.count = Student.count + 1

if Student.count != 0:
    print('测试失败')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败')
    else:
        lisa = Student('Lisa')
        if Student.count != 2:
            print('测试失败')
        else:
            print('Students:',Student.count)
            print('测试通过')