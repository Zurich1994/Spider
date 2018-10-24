# coding = utf-8
# coding:utf-8
# chardet 需要下载安装
# 爬虫中文编码的处理

import chardet
from requests import get

line = "http://www.baidu.com"
html_1 = get(line).content
encoding_dict = chardet.detect(html_1)
web_encoding = encoding_dict['encoding']
if web_encoding == 'utf-8' or web_encoding == 'UTF-8':
	html = html_1
else:
	html = html_1.decode('gbk', 'ignore').encode('utf-8')
