#!/usr/bin/env python
# coding=utf-8

import request_util as request
from bs4 import BeautifulSoup
import codecs
import os
import tld
import urlparse

def open_tumblr(url):
    page_code = request.get_over_sock(url)
    if page_code:
        page_code = page_code.replace('&gt;', ">")
        page_code = page_code.replace('&lt;', "<")
        return page_code
    else:
        return None

def parse_tumblr(page_code):
    soup = BeautifulSoup(page_code, "lxml")
    videos = []
    photos = []
    for i in soup.find_all("video"):
        video_url = i.source.get('src')
        if video_url not in videos:
            videos.append(video_url)
    for i in soup.find_all("photo-url",attrs={'max-width':'1280'}):
        photo_url =  i.string
        photos.append(photo_url)
    return videos,photos

def save_file(name,content):
    result_file = "result/%s.txt"%name
    if not os.path.exists(result_file):
        f = codecs.open(result_file,'a')
        f.write(content)
        f.close()
    else:
        pass

def parse_tumblr_url(url):
    net_loc = urlparse.urlparse(url).netloc
    domain = tld.get_tld(url)
    if net_loc.find(domain):
        name = net_loc[:net_loc.find(domain) - 1]
        return name
    else:
        return None

def get_real_video_url(url):
    resp = request.get_resp_over_sock(url)
    if resp:
        return resp.headers['Location']
    else:
        return None

def start_task(url):
    name = parse_tumblr_url(url)
    if name:
        print name
        page_code = open_tumblr(url)
        if page_code:
            videos,photos = parse_tumblr(page_code)
            content = ""
            if videos:
                for v in videos:
                    real_url = get_real_video_url(v)
                    if real_url:
                        print real_url
                        content = content + real_url.replace("#_=_","") + "\n"
            if photos:
                for p in photos:
                    content = content + p + "\n"
            # print content
            save_file(name,content)
        else:
            pass

    else:
        pass
    return None

if __name__ == '__main__':
    input_url = "http://eaglelu.tumblr.com"
    net_loc = urlparse.urlparse(input_url).netloc
    url = "http://%s/api/read?type={photo|video}&start=0&num=200"%net_loc
    start_task(url)
