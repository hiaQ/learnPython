#!/user/bin/env python3
#coding:utf-8
import re

def is_valid_email(addr):
	re_email = re.compile(r'^\w+.+\w+@\w+.com$')
	if re_email.match(addr):
		return re_email.match(addr).group()
	else:
		return 'Error!'

print(is_valid_email('someone@gmail.com'))
print(is_valid_email('bill.gates@microsoft.com'))
print(is_valid_email('bob#example@.com'))
print('OK')