#!/user/bin/env python3
#coding:utf-8

from enum import Enum,unique

#@unique装饰器可以帮我检查保证没有重复值
@unique
class Weekday(Enum):
	#把Sun的value值改为0
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6 

#访问枚举类型
day1 = Weekday.Mon
print('Weekday.Mon = ',day1)
print('Weekday.Tue = ',Weekday.Tue)
print('Weekday.Tue.value = ', Weekday.Tue.value)
print(Weekday['Tue'])
for name,member in Weekday.__members__.items():
	print(name,'=>',member) 
