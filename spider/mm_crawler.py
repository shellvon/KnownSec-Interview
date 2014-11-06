# encoding=utf8
# author:shellvon

import time
import argparse

import opt_config
import spider
import urlfetch


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
    thread_pool.add_job(urlfetch.scan_url, urlfetch.START_URL, args)
    thread_pool.start_job()
    thread_pool.wait()
    progressinfo = thread_pool.get_progressinfo()
    print 'thread_pool info:{0}\nfinished in {1}s'.format(progressinfo, time.time()-start)

if __name__ == '__main__':
    main()
