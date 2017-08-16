#!/usr/bin/env python
# coding=utf-8
import requests
import re
import re_util
from bs4 import BeautifulSoup,element
from spider_queue_dao import SpiderQueue
from spider_result_dao import SpiderResult
import task_mysql_dao as task_dao
import urlparse
from Download import request

class KeyWordSpider():
    config = {}
    rootLink = ""
    currentLint = ""
    spider_result = SpiderResult()
    def __init__(self,process_id):
        self.spider_queue = SpiderQueue(process_id)

    def param_config(self,param):
        self.param = param
        print u"解析配置"
        if self.param.has_key('_id') and self.param.has_key('depth') and self.param.has_key('keywords') and self.param.has_key('task_id'):
            self.task_id = self.param['task_id']
            print self.param
            return True
        return False
    def do_start(self,param):
        print u"程序开始运行"
        if self.param_config(param):
            print u"开始抓取"
            url = self.param['_id']
            depth = int(self.param['depth'])
            keywords = self.param['keywords']
            self.Spider(url,depth,keywords)

    def Spider(self,url,depth=1,keywords=""):
        print u"小虫虫就要出发咯"
        if keywords!="":
            r = urlparse.urlparse(url)
            self.rootLink = r.scheme+"://"+r.netloc
            self.currentLink = url[0:url.rfind("/")]
            self.LoadAllLink(url,depth,keywords)
            print u"小虫虫爬取完毕咯"
        else:
            return None

    def LoadHtml(self,url):
        resp = request.get(url)
        charset = requests.utils.get_encodings_from_content(resp.content)[0]
        resp.encoding = charset
        pageCode = resp.text
        print pageCode
        return pageCode

    def FindAllKeyword(self,url,keywords,pageCode):
        soup = BeautifulSoup(pageCode, 'lxml')
        for key in keywords:
            if isinstance(key, str):
                key = key.decode('utf-8')
            results = soup.find_all(text=re.compile(key))
            print results
            for r in results:
                if len(r.find_parents('a')) > 0:
                    task_dao.add_one_task_result(self.task_id,r.find_parents('a')[0].get('href'),re.sub(re_util.null_parrten,"",r))
                else:
                    task_dao.add_one_task_result(self.task_id, url, re.sub(re_util.null_parrten,"",r))


    def LoadAllLink(self,url,depth,keywords):
        resp = request.get(url,3)
        charset = requests.utils.get_encodings_from_content(resp.content)[0]
        resp.encoding = charset
        pageCode = resp.text
        pageCode = re.sub(re.compile('<script>.*?</script>', re.MULTILINE | re.S | re.I), "", pageCode)
        pageCode = re.sub(re.compile('<!--.*?-->',re.S),"",pageCode)
        soup = BeautifulSoup(pageCode,'lxml')
        depth -= 1
        if depth>0:
            for item_a in soup.body.find_all('a'):
                if item_a.get('href').startswith("/"):
                    subUrl = self.rootLink + item_a.get('href')
                    self.spider_queue.add_one(self.task_id, subUrl, depth, keywords)
        self.FindAllKeyword(url,keywords,pageCode)



