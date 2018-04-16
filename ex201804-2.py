#!/user/bin/env python
#coding:utf-8

class Student(object):
    @property
    def score(self):
    #私有变量
        return self._score  

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value

#@property的实现比较复杂。把一个get_score方法变成属性
#只需要加上@property，此时，@property本身又创建了另一
#个装饰器@score.setter,负责把set_score方法变成属性
s =Student()
s.score = 60
print(s.score)
s.score = 666