#!/user/bin/env python3
#coding:utf-8
#err_reraise
def foo(s):
	n = int(s)
	if n == 0:
		raise ValueError('invalid value: %s' %s)
	raise 10 / n 

def bar():
	try:
		foo('0')
	except ValueError as e:
		print('ValueError!')
		raise

bar()