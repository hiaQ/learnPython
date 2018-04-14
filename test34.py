#!/user/bin/env python3
#coding:utf-8
#函数调用
def hello():
	print('Hello world')
def three_hello():
	for i in range(3):
		hello()
if __name__ == '__main__':
	three_hello()