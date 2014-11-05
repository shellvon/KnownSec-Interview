# encoding=utf8
# author:shellvon

import argparse
import opt_config
import spider
import requests
import os
import chardet
import time


def func(url, args):
    # for test
    for i in get_img_url_list(None):
        filename = i.split('/')[-1]
        path = args.output
        data = requests.get(i).content
        charset = chardet.detect(data)['encoding']
        save(filename, data, path)


def get_img_url_list(url):
    """
    parser the html get get all the illegal picture's url
    """
    return ['http://qlimg1.meimei22.com/pic/qingliang/2014-8-7/1/17375792120140629135409094_640.jpg']


def save(filename, data, path):
    fullname = os.path.join(path, filename)
    try:
        if not os.path.exists(path):
            os.mkdir(path)
    except IOError, e:
        print e
        return False
    with open(fullname, 'wb') as f:
        f.write(data)
    return True


def main():
    start = time.time()
    parser = argparse.ArgumentParser(
        description='The %(prog)s by shellvon',
        epilog="""
                爬虫->22mm.cc上->美女图片
            """
    )
    arguments = opt_config.optional_arguments
    map(lambda x: parser.add_argument(x, **arguments[x]), arguments)
    args = parser.parse_args()
    thread_pool = spider.ThreadingPool(args.thread_num)
    start_url = 'www.baidu.com'
    thread_pool.add_job(func, start_url, args=args)
    thread_pool.start_job()
    thread_pool.wait()
    progressinfo = thread_pool.get_progressinfo()
    print 'thread_pool info:{0}\nfinished in {1}s'.format(progressinfo, time.time()-start)

if __name__ == '__main__':
    main()
