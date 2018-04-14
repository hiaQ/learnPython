#!/user/bin/env python
#coding: utf-8

tup1 = (1,2,3);
tup2 = ('apple','orange');

#元组中的元素是不可以被修改的
#下面这样写程序会出错
#tup1[0]=100
#正确的写法如下：

tup3 = tup1 + tup2;
print tup3;