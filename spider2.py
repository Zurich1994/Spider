# coding = utf-8
import os
import re
import urllib.error as error

import requests


def tieba_pic(url, name):
	payload = {'word': name, 'rn': 10}
	i = 0
	download_dir = 'f:/pic/'
	if os.path.isdir(download_dir):
		pass
	else:
		os.makedirs(download_dir)
	x = requests.get(url, params=payload, allow_redirects=False, timeout=200000)
	print("合成链接是：" + x.url)
	html = x.content.decode('GBK', 'ignore')
	pic_pattern = re.compile(r'http://[^\s]*.jpg')
	for image in pic_pattern.findall(html):
		download_name = str(i) + '.jpg'
		try:
			link_obj = requests.get(image)
			if (link_obj.status_code is not 200):
				continue
			image_data = link_obj.content
			with open(download_dir + download_name, 'wb') as f:
				print("正在下载第" + str(i) + "个图片" + image)
				i += 1
				f.write(image_data)
			f.close()
		except error.URLError:
			print('下载失败')
	print(i)


if __name__ == '__main__':
	search_name = input("请输入要搜索图片的关键词：")
	url0 = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8'
	tieba_pic(url0, search_name)
