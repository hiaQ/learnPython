#!/user/bin/env python
#coding:utf-8

#判断素数的方法：用一个数分别去除2到sqrt(该数)，如果能被整除则表明次数不是素数
from math import sqrt
leap = 1
a = 0  #mark the number of the 
for i in range(101,201):
	s = int(sqrt(i+1))
	for j in range(2,s+1):
		if i % j == 0:
			leap = 0
			break
	if leap == 1:
		a+=1
		print i
	leap = 1   #这句是重点
print u'101-200之间的素数总共有%d个' % a