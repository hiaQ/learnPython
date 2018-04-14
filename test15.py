#!/user/bin/env python
#coding:utf-8

score = int(raw_input(unicode("请输入考生的成绩:","utf-8").encode('gbk')))
if score >= 90:
	print "A"
elif score>=60 and score <=89:
	print "B"
elif score <60:
	print "C"
