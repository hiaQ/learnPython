#!/user/bin/env python3
#coding:utf-8
from xml.parsers.expat import ParserCreate
from urllib import request

def parseXml(xml_str):
	print(xml_str)
	return {
		'city':'?',
		'forecast':[
		{
			'date':'09 May 2018',
			'high':82,
			'low':53
		},
		{
			'date':'10 May 2018',
			'high':80,
			'low':59
		}
		]
	}

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL) as f:
	data = f.read()
result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'