#!/user/bin/env python3
#coding:utf-8
def foo(s):
	return 10/int(s)

def bar(s):
	return foo(s)*2

def main():
	try:
		bar(0)
	except Exception as e:
		print('Error')
	finally:
		print('finally...')

main()