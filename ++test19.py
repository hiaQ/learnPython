#!/user/bin/env python
#coding: utf-8
for j in range(2,1001):
	temp = []
	n = -1
	s = j
	for i in range(1,j):
		if j%i == 0:
			n+=1
			s-=i
			temp.append(i)
	if s == 0:
		print j
		print temp