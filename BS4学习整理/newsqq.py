#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup
import requests
import re
zhPattern = re.compile(u'[\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u6211\u4f60\u5927\u5c0f]+')
def get_html(url):
    resp = requests.get(url, timeout=1)
    if len(requests.utils.get_encodings_from_content(resp.content)) > 0:
        charset = requests.utils.get_encodings_from_content(resp.content)[0].lower()
        resp.encoding = charset

    pageCode = resp.text
    match = zhPattern.search(pageCode)
    if match:
        print True
        print re.findall(zhPattern,pageCode)
    else:
        resp.encoding = 'gbk'
        pageCode = resp.text
        for i in re.findall(zhPattern, pageCode):
            print i


    pageCode = re.sub(re.compile('<script.*?</script>', re.MULTILINE | re.S | re.I), "", pageCode)
    pageCode = re.sub(re.compile('<!--.*?-->', re.S), "", pageCode)
    return pageCode

def parse_html(url):
    pagecode = get_html(url)
    soup = BeautifulSoup(pagecode,'lxml')
    #print soup.prettify()




if __name__ == '__main__':
    url = "http://news.qq.com"
    parse_html(url)
    print u'\u6211'



