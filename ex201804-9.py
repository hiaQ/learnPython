#!/user/bin/env python3
#coding:utf-8
'''import subprocess

print('$ nslookup www.baidu.com')
r = subprocess.call(['nslookup','www.baidu.com'])
print('Exit code:',r)  '''

import subprocess
print('$nslookup')
p = subprocess.Popen(['nslookup'],stdin = subprocess.PIPE,
	stdout = subprocess.PIPE,stderr = subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('GBK'))
print('Exit code:',p.returncode) 
