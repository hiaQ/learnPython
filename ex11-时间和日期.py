#! /user/bin/env python
#coding: utf-8

import time;
print time.time(); 
#上面的时间是距离1970年1月1日的秒数
print time.localtime(time.time());
#上面的代码是输出年月日时分秒信息
print time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime());
print time.strftime('%y-%m-%d',time.localtime());
print time.strftime('%I:%M:%S  %A %b %c', time.localtime());

import calendar;
print calendar.month(2017,11);