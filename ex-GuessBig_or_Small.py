#!/user/bin/env python
#coding:utf-8

import random
s = random.randint(1,100)
num = int(raw_input(unicode('请输入整数：','utf-8').encode('gbk')))
while num != s:
	if (num > s):
		print u"大了"
		num = int(raw_input(unicode('请输入整数1：','utf-8').encode('gbk')))
	if (num < s):
		print u"小了"
		num = int(raw_input(unicode('请输入整数2：','utf-8').encode('gbk')))
	if (num == s):
		print u"猜对啦！正确值为：",num
		break

