#!/user/bin/env python3
#coding:utf-8
try:
    print('try...')
    r = 10/0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END') 

print('====================')
try:
    print('try...')
    r = 10/2
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END') 