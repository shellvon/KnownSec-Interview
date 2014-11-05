mm_crawler
==
Description:
----
mm_crawler 是用来爬去22mm.cc里面的图片爬虫，使用Python Scrapy,此代码来自于本次之知道创宇的校招题目，题目描述如下：

需满足：

1. 需要排除非相关的图片；

2. 考虑多线程或者协程；

3. 命令行-h可以查看程序运行帮助，-n可以指定并发线程数（默认10个），-o可以指定图片存储在哪个目录（默认当前运行目录的pics目录下），-l可以限制爬多少图片就结束（默认不限制）；

4. 思考个问题，如果下次要爬其他的美女网站，这个程序如何尽可能利于复用；

5. 把你的实现思路清晰记录在该爬虫项目的目录下：readme.txt；

6. 你可以用Python内置模块与第三方模块来加速你这个任务；

7. 先搞定功能，再进行优化，一周的时间，合理安排 , 代码可放github上

8. 如果有时间，可考虑实现一个web app，用上python的framework

Usage:
----
`python mm_crawler.py  [-h] [-l L] [-o O] [-n N] [-v]`

如果想要或许详细的帮助信息，可以:

    python mm_crawler.py -h 或者python sqlmap.py --help

指定收集的图片存取路径和其他帮助信息可以参加题目描述和具体使用-h有提示，比如指定线程数量为40个:

    python mm_crawler.py -n 40

----------

Requirements
----

代码由Ubuntu Python 2.7及其第三方包Requests完成。

Why I Not Choose Scrapy
----

本来打算借此机会使用Scrapy完成该任务。有2个原因放弃了选择

+ 公司无法看到Scrapy文档，所以选择了较为熟悉的Requests自己写。
+ Requests公司电脑上天然拥有。

思路参考之前写的豆瓣音乐爬虫，因为之前代码的失败【比如部分歌曲下载失败】的经验，所以此时一开始设计就打算多加入
诸如精细度的日志/进度信息等。因为网页和图片较多，所以多线程这里自然想到要线程池。对于需求提到的指定下载图片个数之后必须能结束下载，所以我加入了统计失败/成功的计数器。

另外需求提到复用性，比如可能会下载其他地方的，把下载处理图片的函数单独提取出来。这样下次需要改变website的时候尽可能最少改动代码。

Improved
----

我其实还是想学习Scrapy.

Links
----

* Scrapy: [http://scrapy.org/](http://scrapy.org/)

* Python:[https://www.python.org/](https://www.python.org/)

* Requests:[http://docs.python-requests.org/](http://docs.python-requests.org/)
