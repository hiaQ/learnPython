#!/user/bin/env python
#coding:utf-8
import random 
answer = int(random.uniform(1,10))
#number = int(input('猜猜数字：'))
number = input(unicode('输入整数','utf-8').encode('gbk'))
if number == answer:
	print u'厉害，第一次就对啦'
while number != answer:
	if number > answer:
		print u'大了'
		number = input(unicode('再猜一次：','utf-8').encode('gbk'))
		#number = int(input('再猜一次：'))
	if number < answer:
		print u'小了'
		number = input(unicode('再猜一次：','utf-8').encode('gbk'))
		#number = int(input('再猜一次：'))
	if number == answer:
		print u'bingo!'
		break