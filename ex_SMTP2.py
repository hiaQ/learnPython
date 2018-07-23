#!user/bin/env python3
#coding:utf-8

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr)) #??

from_addr = input('From:')
password = input('Password:')
to_addr = input('To:')
smtp_server = input('SMTP server:')

msg = MIMEText('Hello, send by wendy...','plain','utf-8')
msg['From'] = _format_addr('WendyWang<%s>' % from_addr)
msg['To'] = _format_addr('收件人<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……','utf-8').encode() #转码

server = smtplib.SMTP(smtp_server,25) #不同的邮箱SMTP默认的端口号(25)不同
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit() 