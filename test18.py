#!/user/bin/env python
#coding: utf-8

n = int(raw_input(unicode("请输入一个底数：","utf-8").encode('gbk')))
x = int(raw_input(unicode("请输入共有多少个数相加：","utf-8").encode('gbk')))

sum = 0
temp = []
result = 0
for i in range(0,x):
	sum = sum * 10 +n
	temp.append(sum)
	result = result+temp[i]
print "temp = ",temp
print "result = ",result