
#!/user/bin/env python
#coding:utf-8

def sum(month):
		if (month ==1 or month ==2):
			return 1
		else:
			return sum(month-1) + sum(month-2)

print sum(2)
print sum(36)
