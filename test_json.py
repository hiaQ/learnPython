#!user/bin/env python3
#coding:utf-8
#对中文进行JSON序列化时，json.dumps()提供了一个
#ensure_ascii参数，观察该参数对结果的影响
import json

obj = dict(name = '小明', age = 20)
s = json.dumps(obj, ensure_ascii = False)
print(s)