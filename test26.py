#!/user/bin/env python
#coding:utf-8
def fun(i):
	sum = 0
	if i == 0:
		sum = 1
	else:
		sum = i*fun(i-1)
	return sum
print fun(5)
