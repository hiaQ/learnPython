#!/user/bin/env python
#coding:utf-8

import random
while 1:
	s = int(random.randint(1,3))
	if s == 1:
		s1 = '石头'
	elif s == 2:
		s1 = '剪刀'
	elif s == 3:
		s1 = '布'
	myinput = raw_input(unicode('请输入石头、剪刀或布：(输入end结束游戏)','utf-8').encode('gbk'))
	mora = ["石头","剪刀","布"]
	if (myinput not in mora) and (myinput != 'end'):
		print u"输入出错，请重新输入"
	elif (myinput not in mora) and (myinput == 'end'):
		print u"游戏正在退出...."
		break
	elif myinput == s1:
		print u"电脑出了"+s1+"，平局！"
	elif (myinput == '石头' and s1 == '剪刀') or (myinput == '剪刀' and s1 == '布') or (myinput == '布' and s1 == '石头'):
		print u"电脑出了"+s1+",你赢了!"
	elif (myinput == '剪刀' and s1 == '石头') or (myinput == '布' and s1 == '剪刀') or (myinput == '石头' and s1 == '布'):
		print u"电脑出了"+s1+",你输了!"