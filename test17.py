#!/user/bin/env python
#coding:utf-8

import string
str = raw_input(unicode("请输入一行字符（可以包含数字、英文字母、空格等","utf-8").encode('gbk'))
length = len(str)
a=b=c=d=0 #a是英文字母，b是空格，c是数字，d是其他字符
for i in range(0,length):
	x = str[i]
	if x.isalpha():
		a += 1
		i += 1
	elif x.isspace():
		b += 1
		i += 1
	elif x.isdigit():
		c += 1
		i += 1
	else:
		d += 1
		i += 1
print 'char = %d,space = %d,digit = %d, other = %d' % (a,b,c,d)
