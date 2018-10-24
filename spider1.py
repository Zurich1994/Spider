# coding = utf-8
'''
用来爬具有分页的网址
网址为春节吧某一个话题的分页
http://tieba.baidu.com/p/4957196734?pn=
'''
import requests
import os.path


def tieba(url, head_page, tail_page):
	for i in range(head_page, tail_page + 1):
		file_dir = 'f:/spider/'
		file_name='第' + str(i).zfill(5) + '页.html'
		print("正在下载第" + str(i) + "页...")
		html = requests.get(url + str(i)).content
		if os.path.isdir(file_dir):
			pass
		else:
			os.mkdir(file_dir)
		with open(file_dir+file_name, "wb") as f:
			f.write(html)
		f.close()


if __name__ == "__main__":
	url = "http://tieba.baidu.com/p/4957196734?pn="
	headpage = 1
	tailpage = 10
	tieba(url, headpage, tailpage)

