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

    python sqlmap.py -h 或者python sqlmap.py --help

指定收集的图片存取路径和其他帮助信息可以参加题目描述和具体使用-h有提示，比如指定线程数量为40个:

    python sqlmap.py -n 40

Links
----

* Scrapy: [http://scrapy.org/](http://scrapy.org/)

* Python:[https://www.python.org/](https://www.python.org/)

