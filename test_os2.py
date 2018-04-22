#!/user/bin/env python3
#coding:utf-8
#编写一个程序，能在当前目录以及当前目录的所有子目录下
#查找文件名包含指定字符串的文件，并打印出相对路径
import os

def find(name,path = '.'):
	for x in os.listdir(path):
		x = os.path.join(path,x)
		if os.path.isfile(x) and (name in x):
			print(os.path.join(path,x))
		if os.path.isdir(x):
			find(name,os.path.join(path,x))

path = os.getcwd()
find('ex1',path)


