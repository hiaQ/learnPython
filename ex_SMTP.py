#!user/bin/env python3
#coding:utf-8
from email.mime.text import MIMEText
from email.header import Header
msg = MIMEText('Hello, send by wendy...','plain','utf-8')
#输入Email地址和口令
from_addr = input('From: ')
password = input('Password: ')    #密码是授权密码而非邮箱密码 
#输入收件人地址
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

import smtplib
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)

#=====不标注下面这一段的话网易会把邮件视为垃圾邮件或错误邮件
#而发布出去============================
subject = 'Hello' 
msg['Subject'] = Header(subject,'utf-8')
msg['From'] = '<wangqi950701@163.com>'
msg['To'] = '1120352508@qq.com'
#===========================================

server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()