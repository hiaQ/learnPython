#!/user/bin/env python3
#coding:utf-8
import itertools
def pi(N):
	#Step1:创建一个奇数序列：1,3,5,7,9... 
	i = itertools.count(1,2) 
	#Step2:去该序列的前N项
	n = itertools.takewhile(lambda x: x <= 2*N, i)
	#Step3:添加正负号并用4除
	sum = 0
	t = 4
	for i in n:
		sum += t/i 
		t = -t
	return sum

print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok') 