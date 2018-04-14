#!/user/bin/env python
#coding:utf-8
a = 10
h = 100.0
height = h*(0.5**a)
print u"第10次反弹有%d米高" % height
for i in range(1,10):
	h += 100.0*(0.5**i)*2
print u"在第10次落地时，共经过%d米" % h