#!/user/bin/env python
#coding:utf-8
num = int(input('请输入一个5位数：'))
if num // 10000 == 0:
	print('输入内容不符合要求')
else:
	a = num // 10000
	b = (num // 1000)%10
	c = (num // 100)%10
	d = (num // 10)%10
	e = num % 10
	if a == e and b == d:
		print('%d是回文数'%num)
	else:
		print('%d不是回文数'%num)