#!/user/bin/env python
#coding:utf-8

num1 = raw_input(unicode('输入被除数：','utf-8').encode('gbk'))
num2 = raw_input(unicode('输入除数：','utf-8').encode('gbk'))

result = int(num1) / int(num2)

print u'运算结果为:%d' % result