#!/user/bin/env python3
#coding:utf-8
try:
    print('try...')
    r = 10 / 2
    print('result:',r)
except ValueError as e:
	print('ValueError:',e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:',e)
else:
	print('No ERROR!')
finally:
	print('finally...')
print('END') 