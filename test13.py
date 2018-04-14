#!/user/bin/env python
#coding: utf-8

#水仙花数是三位数，且a*100+b*10+c = a^3+b^3+c^3
#水仙花数范围在100-999
print u"水仙花数为：\n"
for i in range(100,1000):
	c = i % 10    #个位数
	a = i / 100   #百位数
	b = (i / 10) % 10   #十位数
	if i == a**3+b**3+c**3:
		print i