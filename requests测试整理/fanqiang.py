#!/usr/bin/env python
# coding=utf-8

import requests
from bs4 import BeautifulSoup
import re


def get_google():
    # socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
    # socket.socket = socks.socksocket
    proxies = {
        'http': 'socks5://127.0.0.1:1080',
        'https': 'socks5://127.0.0.1:1080'
    }
    url = "http://eaglelu.tumblr.com/api/read?type={photo|video}&start=0&num=200"
    resp = requests.get(url, timeout=5, proxies=proxies, )
    print resp.status_code
    # print re.findall(re.compile('&lt;'),resp.text)
    # print re.findall(re.compile('&gt;'), resp.text)
    resp.encoding = "utf-8"
    page_code = resp.text
    page_code = page_code.replace('&gt;',">")
    page_code = page_code.replace('&lt;',"<")
    return page_code


def parse_tumblr(page_code):
    soup = BeautifulSoup(page_code,"lxml")
    videos = []
    for i in soup.find_all("video"):
        print type(i.source.get('src'))
        videos.append(i.source.get('src'))
    print videos
    # for i in soup.find_all("photo-url",attrs={'max-width':'1280'}):
    #     print i

    # print len(soup.find_all("video")),len(soup.find_all("photo-url"))


def test():
    page_code = open("test2.txt").read()
    print type(page_code)
    page_code = re.sub(re.compile('&lt;'), "<", page_code)
    page_code = re.sub(re.compile('&gt;'), ">", page_code)
    print page_code

def test_real_video_url():
    proxies = {
        'http': 'socks5://127.0.0.1:1080',
        'https': 'socks5://127.0.0.1:1080'
    }
    url = "http://eaglelu.tumblr.com/video_file/t:0ZoAscT-jMzDiFo1pvlGUg/155627529762/tumblr_o4ch4tmwu21uxoh6y"
    resp = requests.get(url,proxies= proxies,allow_redirects = False,)
    print resp.headers['Location']


if __name__ == '__main__':
    page_code = get_google()
    parse_tumblr(page_code)
    # #test()
    #test_real_video_url()
