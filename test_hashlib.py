#!/user/bin/env python3
#coding:utf-8
#根据用户输入的口令，计算出存储在数据库中的MD5口令
#并设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回
#True或False

import hashlib
def calc_md5(password):
	md5 = hashlib.md5()
	md5.update(password.encode('utf-8'))
	md5_p = md5.hexdigest()
	return md5_p

db = {'michael':'e10adc3949ba59abbe56e057f20f883e',
	'bob':'878ef96e86145580c38c87f0410ad153',
	'alice':'99b1c2188db85afee403b1536010c2c9'}

def login(user,password):
	if user in db:
		if db[user] == calc_md5(password):
			return True
		else:
			return False
	else:
		return False


assert login('michael','123456')
assert login('bob','abc999')
assert login('alice','alice2008')
assert not login('michael','1234567')
assert not login('bob','123456')
print('OK')
  