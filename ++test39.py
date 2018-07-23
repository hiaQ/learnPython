#!/user/bin/env python3
#coding:utf-8
#有一个已经排好序的数组，现输入一个数，要求按原来的规律
#将它插入其中
a = [1,3,4,6,7,8,9,13,25,68]
print('原始列表：')
for b in a:
	print(b)
print('请输入一个数（整数）:')
ip = int(input())
end = a[-1]
if ip >= end:
	a.append(ip)
	print('插入'+str(ip)+'之后的数组变为：',a)
else:
	for i in range(len(a)-1):
		if a[i] <= ip < a[i+1]:
			a.insert(i+1,ip)
			break
	print('排序后的数组是：')
	print(a)
 #注意Python内置函数的使用