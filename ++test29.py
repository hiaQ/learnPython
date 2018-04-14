#!/user/bin/env python3
#coding:utf-8
i = int(input("请输入一个不多于5位数的正整数："))
a = i//10000
b = (i % 10000)//1000
c = (i % 1000)//100
d = (i % 100)//10
e = i % 10
if a!=0:
	print("5位数",e,d,c,b,a)
elif b!=0:
	print("4位数",e,d,c,b)
elif c!=0:
	print("3位数",e,d,c)
elif d!=0:
	print("2位数",e,d)
else:
	print("1位数",e)