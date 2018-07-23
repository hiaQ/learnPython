#!/user/bin/env python3
#coding:utf-8
#可以提取出带名字的Email地址
import re

def name_of_email(addr):
	if '<' in addr:
		return re.match(r'^(<\w+\s\w+>)(\w+)@(\w+.\w+)$',addr).group(1)
	else:
		return re.match(r'^(\w+)@(\w+.)(com)$',addr).group(1)

print(name_of_email('<Tom Paris>tom@voyager.org'))
print(name_of_email('tom@voyager.com'))