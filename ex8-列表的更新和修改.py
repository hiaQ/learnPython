#!/user/bin/env python
#coding:utf-8
list = ['apple','iphone',2016,2017]
print u"初始列表：",list
list[2] = 2015;
print u"一次更新：",list
list.append(2018);
print u"二次更新：",list
del list[2]
print u"删除之后：",list
len1 = len(list)
print u"列表长度为：",len1