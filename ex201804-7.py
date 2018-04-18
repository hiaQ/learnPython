#!/user/bin/env python3
#coding:utf-8
#err_raise
class FooError(ValueError):
	pass

def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('Invalid value: %s' % s)
	return 10/n

print(foo('0'))