#!/user/bin/env python
#coding:utf-8
a = 1.0
b = 2.0
x = 2.0
y = 3.0
s = 2/1.0 + 3/2.0
for i in range(3,21):
	c = a+b
	a = b
	b = c
	z = x+y
	x = y
	y = z
	s += z/c
print s 