#!/user/bin/env python3
#coding:utf-8
import os

#查看当前目录的绝对路径
print('当前目录的绝对路径：',os.path.abspath('.'))

#在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
os.path.join('C:/Users/wq/Desktop','testdir')
#然后创建一个目录
os.mkdir('C:/Users/wq/Desktop/testdir') 

print(os.path.split('C:/Users/wq/Desktop/11.txt'))

print(os.path.splitext('/path/to/11.txt'))  