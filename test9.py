#!/user/bin/env python
#coding:utf -8
#暂停一秒输出（使用time模块的sleep()函数）
import time
myID = {1:'a',2:'b'}
for key,value in dict.items(myID):
	print key, value 
	time.sleep(1)