#!/user/bin/env python3
#coding:utf-8
import base64,struct

def bmp_info(data):
	m = struct.unpack('<ccIIIIIIHH',data[:30])
	print(m)
	return {
		'width':m[6],
		'height':m[7],
		'color':m[9]
	}

with open(r'C:\Users\wq\Desktop\1.bmp','rb') as f:
	bmp_data = f.read(30)

bi = bmp_info(bmp_data)
assert bi['width'] == 1152
assert bi['height'] == 648
assert bi['color'] == 8 
print('OK')