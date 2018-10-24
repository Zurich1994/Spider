参数说明：
基本参数：
-h 查看帮助
-u 要爬取的url
-n 最大线程数，默认为10
-o 图片存放路径，默认放在当前路径的pic目录下
-l 爬取的最大图片数限制，默认无限制
-c 网页的编码方式，默认utf-8
-e 是否爬取外链，默认不爬取

高级参数：
-r 加速倍数，默认不加速
-t 线程启动间隔时间，默认0.001s
-ae 用于添加图片类型，默认支持的图片类型为['jpg','png','gif']
-ad 用于添加要爬取的域名

例子1：
python spider.py -u "http://www.22mm.cc/" -ad "meimei22.com"

例子2：
python spider.py -u "http://girl-atlas.com/" -n 20 -o "g:\images" -c "utf-8" -r 2 -t 0.001 -ae "jpg!mid" -ae "jpg!pre" -ae "jpg!prev" -ad "upaiyun.com"

有问题可发邮件到:
479209228@qq.com

