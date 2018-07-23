#!/user/bin/env python3
#coding:utf-8

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

import smtplib

def _format_addr(s):
	name,addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = input('From:')
password = input('password:')
to_addr = input('To:')
smtp_server = input('SMTP Server: ')

#邮件对象
msg = MIMEMultipart()
msg['From'] = _format_addr(from_addr)
msg['To'] = _format_addr(to_addr)
msg['Subject'] = Header('来自SMTP的问候……','utf-8').encode()

#邮件正文是MIMEText
msg.attach(MIMEText('<html><body><h1>Hello</h1>'+
	'<p><img src="cid:0"></p>'+
	'</body></html>','html','utf-8')) 

#添加附件就是加上一个MIMEBase，从本地读取一个图片
with open('E:/picture/2.jpg','rb') as f:
	#设置附件的MIME和文件名，这里是jpg格式
	mime = MIMEBase('image','jpg',filename='2.jpg')
	#加上必要的头信息
	mime.add_header('Content-Disposition','attachment',filename='2.jpg')
	mime.add_header('Content-ID','<0>')
	mime.add_header('X-Attachment-Id','0')
	#把附件的内容读进来
	mime.set_payload(f.read())
	#用base64编码
	encoders.encode_base64(mime)
	#添加到MIMEMultipart
	msg.attach(mime)

server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit() 

