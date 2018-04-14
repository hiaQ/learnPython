#!/user/pin/bin/env python
#coding:utf-8

#window系统的写法，需要进行转码
str = raw_input(unicode('raw_input请输入：','utf-8').encode('gbk'));
print u'raw_input的内容是：',str

#其他系统
str = raw_input("raw_input请输入：");
print u"raw_input的内容是：",str 