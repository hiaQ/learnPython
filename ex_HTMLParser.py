#!/user/bin/env python3
#coding:utf-8
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
	def handler_starttag(self,tag,attrs):
		print('<%s>' % tag)

	def handler_endtag(self,tag):
		print('<%s>' % tag)

	def handler_startendtag(self,tag,attrs):
		print('<%s/>' % tag)

	def handler_data(self,data):
		print(data)

	def handler_comment(self,data): 
		print('<!——',data,'——>')

	def handler_entityref(self,name):
		print('&%s:' % name)

	def handler_charref(self,name):
		print('&#%s:' % name)

parser = MyHTMLParser()
parser.feed('''<html><head></head><body><!——test html parser ——>
	<p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')
