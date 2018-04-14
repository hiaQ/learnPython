#!/user/bin/env python
#coding: utf-8

fo = open("foo.txt","r+")
str = fo.read(12)
print u"读取的字符串是：",str

#查找当前位置
position = fo.tell()
print u"当前文件位置：",position

#把指针再次重新定位到文件开头
position = fo.seek(3,0)
str = fo.read(10)
print u"重新读取字符串：",str

#关闭文件
fo.close()