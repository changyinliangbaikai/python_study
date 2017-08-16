#!/usr/bin/env python
# coding=utf-8
"""
@version: 1.0
@author: jhx
@contact: jhx679@vip.qq.com
@software: PyCharm Community Edition
@file: do_spider.py
"""
import sys
import requests
import urllib2
import re
import time
import re_util
from spider_queue_dao import SpiderQueue
from spider_result_dao import SpiderResult
class Spider():
    config = {}
    rootLink = ""
    currentLint = ""
    spider_queue = SpiderQueue()
    spider_result = SpiderResult()

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
            items = re.findall(re_util.rootLinkParrten, url)
            self.rootLink = items[0][0:len(items[0])-1]
            self.currentLink = url[0:url.rfind("/")]
            self.LoadAllLink(url,depth,keywords)
            print u"小虫虫爬取完毕咯"
        else:
            return None

    def LoadHtml(self,url):
        pageCode = requests.get(url).text
        return pageCode

    def FindAllKeyword(self,keywords,pageCode):
        result = self.spider_result.find_result_by_task_id(self.task_id)
        if result == None:
            result = {}
        for keyword in keywords:
            keyParrten = re.compile(keyword)
            items = re.findall(keyParrten,pageCode)
            if not result.has_key(keyword):
                result[keyword] = 0
            result[keyword] = result[keyword] + len(items)
        if self.spider_result.find_by_task_id(self.task_id):
            self.spider_result.update_one_result(self.task_id,result)
        else:
            self.spider_result.add_one_result(self.task_id,result)

    def LoadAllLink(self,url,depth,keywords):
        pageCode = requests.get(url).text
        self.FindAllKeyword(keywords,pageCode)
        depth -= 1
        if depth>0:
            items = re.findall(re_util.linkParrten, pageCode)
            for item in items:
                if item.startswith("/"):
                    subUrl = self.rootLink+item
                    self.spider_queue.add_one(self.task_id,subUrl,depth,keywords)




    def Test(self):
        print u"小虫虫就要出发咯"
        url = "http://www.runoob.com/python/file-methods.html"
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20100101 Chrome/17.0.963.56'
        headers = { 'User-Agent' : user_agent }
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        #pageCode = response.read().decode('utf-8','ignore')
        pageCode = requests.get(url).text
        charset = re.compile(u'方法')
        items = re.findall(charset,pageCode)
        print len(items)
        #linkItems = re.findall(ReUtil.linkParrten,pageCode)
        #print len(linkItems)
        #print linkItems
        print u"小虫虫爬取完毕咯"















