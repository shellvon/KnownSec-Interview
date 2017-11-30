# coding=utf8
# author:shellvon

import re
import requests
import os
import urlparse

START_URL = "http://www.22mm.cc/"
URL_TO_SCAN_PATTERN = "/mm/[^\"']+"
BIG_IMG_URL_PATTERN = "http://\w+\.meimei22.com/\w+/\w+/\d{4}-\d{1,2}-\d{1,2}/\d/\d+_640.jpg"


def scan_url(url, deep=None, **args):
    """
    需要爬取的网页，爬取深度，其他附属参数，比如:超时，请求头，代理等，参数参见requests文档
    """
    web_url_lst_to_scan = []
    img_url_lst_to_down = []
    try:
        req = requests.get(url, **args)
        if req.status_code == 200:
            web_url_lst_to_scan = re.findall(URL_TO_SCAN_PATTERN, req.content, re.I)
            img_url_lst_to_down = re.findall(BIG_IMG_URL_PATTERN, req.content, re.I)
            web_url_lst_to_scan = (urlparse.urljoin(url, i) for i in web_url_lst_to_scan)
            img_url_lst_to_down = (i.replace('/big/', '/pic/') for i in img_url_lst_to_down)
    except Exception, e:
        pass
    return (list(set(web_url_lst_to_scan)), list(set(img_url_lst_to_down)))

if __name__ == '__main__':
    pass
