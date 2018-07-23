#!/user/bin/env python3
#coding:utf-8
import re

print('请输入一个字符串:')
test = input()

if re.match(r'正则字符串',test):
	print('OK')
else:
	print('Failed')