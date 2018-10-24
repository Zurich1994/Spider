# coding = utf-8
"""
-------------------------------------------------
   File Name：     v_s
   Description :   爬取VirusShare.com的种子文件
   Author :        Huanran Wang
   date：          2018/1/2/0002
-------------------------------------------------

"""
__author__ = 'SHERLOCK'
import os
import ssl
from bs4 import BeautifulSoup
from urllib import request
import time


def get_html():
    with open("web.html", "r") as f:
        html_str = f.read()
    return html_str


def download_torrent(download_url, file_name):
    local_Path = os.path.join('C:/Users/Sherlocked/Desktop/Virus_spider/Virus_set', file_name)
    with open(local_Path, "wb") as f:
        gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        req = request.Request(download_url, headers={'X-Mashape-Key': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'})
        f.write((request.urlopen(req, context=gcontext)).read())


def html_parse(html_str):
    count = 0
    soup = BeautifulSoup(html_str, "html.parser")  # 初始化
    table_tag_list = soup.findAll("table")
    del table_tag_list[0]
    for table_list in table_tag_list:
        for link in table_list.findAll("a"):
            count += 1
            url = link["href"]
            filename = (link.string + ".torrent").replace(".zip", "")
            print("正在爬取第%d个病毒种子..." % count)
            download_torrent(url, filename)


if __name__ == "__main__":
    time_start = time.time()
    html_parse(get_html())
    time_end = time.time()
    print("总耗时：%f ms." % (time_end - time_start))
