#!/user/bin/env python3
#coding:utf-8
try:
    print('try...')
    r = 10 / int('a')
    print('result:',r)
except ValueError as e:
	print('ValueError:',e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:',e)
finally:
	print('finally...')
print('END')