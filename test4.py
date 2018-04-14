#!/user/bin/env python
#coding:utf-8
year = input(unicode('输入年：',"utf-8").encode("gbk"))
month = input(unicode('输入月：','utf-8').encode('gbk'))
day = input(unicode('输入日：','utf-8').encode('gbk'))

leap = [31,60,91,121,152,182,213,244,274,305,335,366]
notleap = [31,59,90,120,151,181,212,243,273,304,334,365]

if(month <= 2):
	ymd = (month - 1) * 31 + day
elif (month > 2):
	if((year / 400 == 0) or ((year / 4 == 0) and (year / 100 != 0))):
		a = leap
	else:
		a = notleap
	ymd = a[month-2] + day

print u"这一天是这一年中的第%s天" % ymd

	




