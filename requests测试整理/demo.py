#!/usr/bin/env python
# coding=utf-8

#测试requests在断网、地址错误的情况下的返回结果
import requests
from Download import request
from bs4 import BeautifulSoup
import re


def test_no_internet():
    url = 'https://www.baidu.com'
    try:
        resp = requests.get(url)
        print "status_code:",resp.status_code
        print resp.encoding,resp.cookies,resp.links,resp.url

    except Exception as e:
        print e

def test_requests_url():
    url = "https://www.baidu.com/link?url=3RigZ02zCfobuLC7d58ITYb8rCAFpi_cF-vUBBlPWAVvilo2x9R4TaupWgWIOwh7t3fxXkcaoGFS-yJf4SndXK&wd=&eqid=f19d385000011809000000055864b4c7"
    try:
        resp = request.get(url,1)
        print "status_code:",resp.status_code
        print resp.encoding,resp.cookies,resp.links,resp.url
        print resp.links,resp.headers
        print resp.is_redirect,resp.is_permanent_redirect,resp.raise_for_status()
        print resp.text
    except Exception as e:
        print e

def test_baidu_real_url(url):
    try:
        resp = request.get(url, 1)
        print resp.status_code,resp.url
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text,'lxml')
            #print soup.prettify()
            for e in soup.find_all('meta',content=re.compile('.*?(url|URL)=.*?')):
                print re.findall(r'(url|URL)=\'(.*?)\'',e.get('content'))[0][1]
                return re.findall(r'(url|URL)=\'(.*?)\'',e.get('content'))[0][1] # 该规则可以获取到真实地址

        else:
            print resp.status_code
    except Exception as e:
        print e

def test_baidu_search_result():
    url = "https://www.baidu.com/s?wd=%E5%8D%97%E4%BA%AC%E7%A7%AF%E5%88%86%E8%90%BD%E6%88%B7%E6%94%BF%E7%AD%96"
    try:
        resp = request.get(url, 1)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text,'lxml')
            results = soup.find_all(class_has_str)

            for r in results:
                url = r.h3.a.get('href')
                content = ""
                for i in r.find('div',class_='c-abstract').children:
                    content = content + i.string
                print content
                #real_url = test_baidu_real_url(url)
                print url

        else:
            print resp.status_code
    except Exception as e:
        print e

def class_has_str(tag):
    if tag.get('class') and  'result' in tag.get('class') and 'c-container' in tag.get('class'):
        return True
    return False

def test_re():
    t_str = '<div class = "result c-container ">1111</div><div class = "c-container ">1111</div>'
    soup = BeautifulSoup(t_str,'lxml')
    print soup.find_all(class_has_str)
    #print soup.div.get('class')
    # if re.findall(re.compile('aaaa'),t_str):
    #     print True
    # else:
    #     print False

if __name__ == '__main__':
    #test_re()
    #test_baidu_search_result()
    #url = "http://www.baidu.com/link?url=f0BGFiMsXtGnKbBgAuFYOTPAeIpjKwAZVv5tN4EdSwlgxzcpZNy8yRXjlHViWs7zBsfpimsp6Ro7kqynlOewdsYFWYdU2fITItNgpbNjcnX6Dwj7WlPMmnCNfaF6kysG"
    #test_baidu_real_url(url)
    resp = requests.get("http://news.southcn.com/community/content/2016-12/28/content_162574303.htm")
    print resp.text