import re
import urllib.request

# ------ 获取网页源代码的方法 ---
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

# ------ getHtml()内输入任意帖子的URL ------
html = getHtml("http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8")
# ------ 修改html对象内的字符编码为UTF-8 ------
html = html.decode('UTF-8')

# ------ 获取帖子内所有图片地址的方法 ------
def getImg(html):
    # ------ 利用正则表达式匹配网页内容找到图片地址 ------
    reg = r'src="([.*\S]*\.jpg)" pic_ext="jpeg"'
    imgre = re.compile(reg);
    imglist = re.findall(imgre, html)
    return imglist

imgList = getImg(html)
imgName = 0
for imgPath in imgList:
    # ------ 这里最好使用异常处理及多线程编程方式 ------
    f = open("f:/pic/"+str(imgName)+".jpg", 'wb')
    f.write((urllib.request.urlopen(imgPath)).read())
    f.close()
    imgName += 1

print("All Done!")