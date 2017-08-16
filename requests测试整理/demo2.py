#!/usr/bin/env python
# coding=utf-8

import requests
from Download import request
from bs4 import BeautifulSoup
import re
import re_util

def test_sina():
    url = 'http://www.sina.com.cn/'
    resp = requests.get(url)
    print resp.status_code
    print resp.text

def test_down():
    url = 'http://weibo.com/?category=0'
    resp = request.get(url,1)
    print resp.status_code
    print type(resp.content),type(resp.text)
    print resp.encoding.lower()
    #print resp.apparent_encoding
    charset =  requests.utils.get_encodings_from_content(resp.content)[0]
    resp.encoding = charset

    #resp.encoding = 'utf-8'
    pageCode =  resp.text
    print pageCode
    pageCode = re.sub(re.compile('<script>.*?</script>',re.MULTILINE|re.S|re.I),"",pageCode)
    pageCode = re.sub(re.compile('<!--.*?-->', re.S), "", pageCode)
    keywords = [u'\u624b\u673a']
    FindAllKeyword(url,keywords,pageCode)

def FindAllKeyword(url,keywords,pageCode):
    soup = BeautifulSoup(pageCode, 'lxml')
    #print soup.prettify()
    for key in keywords:
        if isinstance(key,str):
            key = key.decode('utf-8')
        results = soup.find_all(text=re.compile(key))
        print results
        for r in results:
            if len(r.find_parents('a')) > 0:
                print r.find_parents('a')[0].get('href'),re.sub(re_util.null_parrten,"",r)
                #task_dao.add_one_task_result(self.task_id,r.find_parents('a')[0].get('href'),re.sub(re_util.null_parrten,"",r))
            else:
                print url, re.sub(re_util.null_parrten,"",r)
                #task_dao.add_one_task_result(self.task_id, url, re.sub(re_util.null_parrten,"",r))
def test_find_all_a():
    url = "http://news.sina.com.cn"
    resp = request.get(url, 3)
    charset = requests.utils.get_encodings_from_content(resp.content)[0]
    resp.encoding = charset
    pageCode = resp.text
    pageCode = re.sub(re.compile('<script>.*?</script>', re.MULTILINE | re.S | re.I), "", pageCode)
    pageCode = re.sub(re.compile('<!--.*?-->', re.S), "", pageCode)
    soup = BeautifulSoup(pageCode, 'lxml')
    for item_a in soup.body.find_all('a'):
        if item_a.get('href') != None:
            print type(item_a.get('href')),item_a.get('href'),item_a



test_find_all_a()