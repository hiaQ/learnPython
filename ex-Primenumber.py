#!/user/bin/env python
#coding:utf-8

i = 2
while (i < 100):
	j = 2
	while(j <= (i/j)):
		if not(i % j):
			break
		j = j+1
	if(j > i/j):
		print i,u" 是素数"
	i = i+1

print "Good bye"