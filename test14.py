#!/user/bin/env python
#coding: utf-8
n = int(raw_input(unicode("请输入一个正整数：",'utf-8').encode('gbk')))
if n <= 0 :
	print u"请输入一个正确的数字！"
temp = []
while n != 1:
	for i in range(2,n+1):
		if n%i == 0:
			temp.append(i)
			n = n/i
			break
print temp