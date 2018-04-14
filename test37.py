#!/user/bin/env python3
#coding:utf-8
#对10个数进行排序
l = []
N = 10
print('请输入10个数字：')
for i in range(N):
	l.append(int(input('请输入一个数字：\n')))

for p in range(N):
	print(l[p])

L = sorted(l)  #python中的排序函数
print('排序后',L)