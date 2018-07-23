#!/user/bin/env python3
#coding:utf-8
#metaclass是类的模板，所以必须从type类型派生
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

#有ListMetaclass之后，在定义类时还要指示使用ListMetaclass来定制类，
#传入关键字参数metaclass
class MyList(list,metaclass = ListMetaclass):
    pass
        
