#!/user/bin/env python3
#coding:utf-8

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr_(s):
	name,addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = input("From:")
password = input("Password:")
to_addr = input("To:")
server_smtp = input('SMTP Server:')

msg = MIMEText('<html><body><h1>Hello</h1>'+
	'<p>send  by<a href="http://www.python.org">Python</a>...</p>'+
	'</body></html>','html','utf-8')
msg['Subject'] = Header('来自SMTP的问候……','utf-8').encode()
msg['From'] = _format_addr_('Wendy<%s>' % from_addr)
msg['To'] = _format_addr_('管理员 <%s>' % to_addr)

server = smtplib.SMTP(server_smtp,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit() 