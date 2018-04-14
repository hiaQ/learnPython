#!/user/bin/env python
#coding:utf-8
str = input('please input:')
if str == '':
	print('Please input!')
elif str == 'M':
	print('It is Monday')
elif str == 'W':
	print('It is Wednesday')
elif str == 'F':
	print('It is Friday')
elif str == 'T':
	print('Please input the second letter:')
	letter = input('Please input:')
	if letter == 'u':
		print('It is Tuesday')
	elif letter == 'h':
		print('It is Thursday')
elif str == 'S':
	print('Please input the second letter:')
	letter = input('Please input:')
	if letter == 'u':
		print('It is Sunday')
	elif letter == 'a':
		print('It is Satday')
else:
	print('data Error')