#!/user/bin/env python
#coding:utf-8
import time
localtime = time.localtime(time.time())
print time.strftime('%Y-%m-%d \n %H:%M:%S',localtime)
time.sleep(1)
print time.strftime('%Y-%m-%d \n %H:%M:%S',time.localtime(time.time()))

