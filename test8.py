#!/user/bin/env python
#coding:utf-8

i = 1
while(i <= 9):
	for j in range(1,i+1):
		print "%d x %d=%d" % (i,j,i*j),
	print
	i+=1 
