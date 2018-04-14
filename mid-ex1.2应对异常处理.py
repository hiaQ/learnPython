#!/user/bin/env python
#coding:utf-8

while 1:
	try:
		num1 = raw_input(unicode('输入被除数：','utf-8').encode('gbk'))
		num2 = raw_input(unicode('输入除数：','utf-8').encode('gbk'))
		result = int(num1) / int(num2)
	except ZeroDivisionError:
		print u'0不能作为除数'+'\n'
	except ValueError:
		print u'请勿输入空值或字母'+'\n'
	else:
		print u'运算结果为%d' % result+'\n'