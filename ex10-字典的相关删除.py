#! /user/bin/env python
#coding: utf-8

dict = {'Name':'Jane','Sex':'female','Hobby':'dance','School':'CXY school'}
print "dict:",dict
del dict['Name']
print "dict:",dict;
print u"dict中所有键分别是：",dict.keys();
print u"dict中所有键的值分别是：",dict.values();
#dict.clear();
#print "dict:",dict;