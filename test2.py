#!/user/bin/env python
#coding:utf-8
num = input(unicode("输入整数：",'utf-8').encode('gbk'))
if num <= 10:
	sum = num*0.1
	print u'应发放的奖金总数：',sum
elif num > 10 and num < 20:
	sum = 10*0.1+(num-10)*0.075
	print u'应发放的奖金总数：',sum
elif num >= 20 and num < 40:
	sum = (num - 20)* 0.05
	print u'应发放的奖金总数：',sum
elif num  >= 40 and num < 60:
	sum = (num-40)* 0.03
	print u'应发放的奖金总数：',sum
elif num >= 60 and num < 100:
	sum = (num - 60)* 0.015
	print u'应发放的奖金总数：',sum
elif num >= 100:
	sum = (num - 100)*0.01
	print u'应发放的奖金总数：',sum