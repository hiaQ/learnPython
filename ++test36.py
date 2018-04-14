#!/user/bin/env python3
#coding:utf-8
#求100以内的素数
temp = []
flag = 0
for i in range(2,101):
	if i > 1:
		for j in range(2,i):
			if(i%j == 0):
				break
		else:
			temp.append(i)
print(temp)

