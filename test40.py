#!/user/bin/env python3
#coding:utf-8
'''if __name__ == '__main__':
	a = [1,2,3,4,5,6]
	temp = []
	l = len(a)
	for i in range(l):
		temp.append(a[l-i-1])
	print(temp)'''

if __name__ == '__main__':
	temp = []
	print('请输入数组的大小：')
	lenght = int(input())
	for i in range(lenght):
		x = int(input())
		temp.append(x)
	print(temp)
	temp2 = []
	for j in range(lenght):
		temp2.append(temp[lenght - j- 1])
	print('逆序后输出：',temp2)

