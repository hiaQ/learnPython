#!/user/bin/env python
#coding:utf-8
num = []
for i in range(3):
	x = raw_input(unicode('请输入三个数字：\n','utf-8').encode('gbk'))
	num.append(x)
num.sort()
print num
 

