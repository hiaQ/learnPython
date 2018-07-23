#!/user/bin/env python3
#coding:utf-8
import re
from datetime import datetime,timedelta,timezone

print('请正确输入日期和时间：')
dt = input()
print('请输入正确的时区信息：')
tz = input()

def to_timestamp(dt_str,tz_str):
	dt_str = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
	hour = re.match(r'UTC([+-]{1}\d{1,2}):(\d{2})',tz_str).group(1)
	tz = dt_str.replace(tzinfo = timezone(timedelta(hours = int(hour))))
	return tz.timestamp()

if dt == '' or tz == '':
	print('输入日期时间有误或输入时区信息有误')
else:
	print(to_timestamp(dt,tz)) 

