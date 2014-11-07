# encoding=utf8
# author:shellvon

import time

import opt_config
import spider
import urlfetch


def main():
    start = time.time()
    args = opt_config.get_opt()
    thread_pool = spider.ThreadingPool(args.thread_num, args.timeout)
    thread_pool.add_job(urlfetch.scan_url, urlfetch.START_URL, args)
    thread_pool.start_job()
    thread_pool.wait()
    progressinfo = thread_pool.get_progressinfo()
    print '{0}\nFinished in {1:.2f} seconds'.format(progressinfo, time.time()-start)

if __name__ == '__main__':
    main()
