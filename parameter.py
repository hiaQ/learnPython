#!/user/bin/env python
#coding: utf-8

def printinfo(arg1, *vartuple):
	u"打印任何传入的参数"
	print u"输出："
	print arg1
	for var in vartuple:
		print var
	return;
printinfo(10);
printinfo(70,60,50);
 