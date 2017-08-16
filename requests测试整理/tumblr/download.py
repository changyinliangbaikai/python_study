#!/usr/bin/env python
# coding=utf-8
import requests


def test_download(url='https://vtt.tumblr.com/tumblr_nqelktSgK11svdbo2.mp4#_=_'):
    proxies = {
        'http': 'socks5://127.0.0.1:1080',
        'https': 'socks5://127.0.0.1:1080'
    }
    r = requests.get(url, stream=True, proxies=proxies, allow_redirects=False, )
    f = open("1.mp4", "wb")
    for chunk in r.iter_content(chunk_size=512):
        if chunk:
            f.write(chunk)
    pass


def test_download2(url='https://vtt.tumblr.com/tumblr_nqelktSgK11svdbo2.mp4#_=_'):
    proxies = {
        'http': 'socks5://127.0.0.1:1080',
        'https': 'socks5://127.0.0.1:1080'
    }
    UA = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    headers = {'User-Agent': UA}
    r = requests.get(url, stream=True, headers=headers, allow_redirects=False, timeout=5,verify=False,)
    f = open("1.mp4", "wb")
    for chunk in r.iter_content(chunk_size=512):
        if chunk:
            f.write(chunk)
    pass


url = 'javascript:void(0)'

if __name__ == '__main__':
    test_download2()
