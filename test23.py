#!/user/bin/env python
#coding: utf-8
from sys import stdout
for i in range(1,5):
	for j in range(4-i):
		stdout.write(' ')
	for p in range(2*i-1):
		stdout.write('*')
	print
for k in range(3):
	for x in range(k+1):
		stdout.write(' ')
	for q in range(4-2*k+1):
		stdout.write('*')
	print