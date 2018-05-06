#!/user/bin/env python3
#coding:utf-8
import base64

def safe_base64_decode(s):
	while (len(s)%4 != 0):
		s = s + b"="
	return base64.b64decode(s)

if __name__ == '__main__':
	print(safe_base64_decode(b'YWJjZA=='))
	print(safe_base64_decode(b'YWJjZA'))