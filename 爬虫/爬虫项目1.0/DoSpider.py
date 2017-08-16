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
import ReUtil
class Spider():
    config = {}
    rootLink = ""
    currentLint = ""
    result = []
    depth = 1
    def ParamConfig(self):
        print u"解析配置"
        if len(sys.argv)>1:
            self.config = eval(sys.argv[1])
            if self.config.has_key('url') and self.config.has_key('depth') and self.config.has_key('keywords'):
                print self.config
                return True
        return False
    def DoStart(self):
        print u"程序开始运行"
        if self.ParamConfig():
            print u"开始抓取"
            url = self.config['url']
            self.depth = int(self.config['depth'])
            keywords = self.config['keywords']
            len(keywords)
            for i in range(len(keywords)):
                #初始化结果参数和关键词编码
                self.result.append(0)
                keywords[i] = keywords[i].decode('gbk','ignore')
            print url,self.depth,keywords
            print len(self.result)
            self.Spider(url,self.depth,keywords)

    def Spider(self,url,depth=1,keywords=""):
        print u"小虫虫就要出发咯"
        if keywords!="":
            items = re.findall(ReUtil.rootLinkParrten,url)
            self.rootLink = items[0][0:len(items[0])-1]
            self.currentLink = url[0:url.rfind("/")]
            self.LoadAllLink(url,keywords)
            print self.result
            print u"小虫虫爬取完毕咯"
        else:
            return None

    def LoadHtml(self,url):
        pageCode = requests.get(url).text
        return pageCode

    def FindAllKeyword(self,keywords,pageCode):
        index = 0
        for keyword in keywords:
            keyParrten = re.compile(keyword)
            items = re.findall(keyParrten,pageCode)
            self.result[index] = self.result[index] + len(items)
            index += 1

    def LoadAllLink(self,url,keywords):
        pageCode = requests.get(url).text
        self.FindAllKeyword(keywords,pageCode)
        self.depth -= 1
        if self.depth>0:
            items = re.findall(ReUtil.linkParrten,pageCode)
            for item in items:
                if item.startswith("/"):
                    subUrl = self.rootLink+item
                    self.LoadAllLink(subUrl,keywords)




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








if __name__ == '__main__':
    sp = Spider()
    t_start = time.time()
    sp.DoStart()
    t_end = time.time()
    print t_end-t_start






