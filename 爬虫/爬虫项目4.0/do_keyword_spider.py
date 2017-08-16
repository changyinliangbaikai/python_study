#!/usr/bin/env python
# coding=utf-8
import re
import re_util
from bs4 import BeautifulSoup,element
from spider_queue_dao import SpiderQueue
from spider_result_dao import SpiderResult
import task_mysql_dao as task_dao
import urlparse
import request_util as request
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


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
            url = self.param['url']
            depth = int(self.param['depth'])
            keywords = self.param['keywords']
            num_retried = self.param['num_retried']
            self.Spider(url,num_retried,depth,keywords)

    def Spider(self,url,num_retried,depth=1,keywords=""):
        print u"小虫虫就要出发咯"
        if keywords!="":
            # try:
            r = urlparse.urlparse(url)
            self.domain = re_util.get_domain_name(url)
            if self.domain == None:
                self.domain = "#"
            self.rootLink = r.scheme+"://"+r.netloc
            self.currentLink = url[0:url.rfind("/")]
            self.LoadAllLink(url,num_retried,depth,keywords)
            # except Exception as e:
            #     print e
            #     pass
            print u"小虫虫爬取完毕咯"
        else:
            return None


    def FindAllKeyword(self,url,keywords,pageCode):
        soup = BeautifulSoup(pageCode, 'lxml')
        if isinstance(keywords, str):
            key = keywords.decode('utf-8')
        results = soup.find_all(text=re.compile(keywords))
        print results
        for r in results:
            if len(r.find_parents('a')) > 0:
                if r.find_parents('a')[0].get('href') is not None:
                    if r.find_parents('a')[0].get('href').startswith("/"):
                        task_dao.add_one_task_result(self.task_id, self.rootLink + r.find_parents('a')[0].get('href'),
                                                     re.sub(re_util.null_parrten, "", r.strip()))
                    else:
                        task_dao.add_one_task_result(self.task_id,r.find_parents('a')[0].get('href'),re.sub(re_util.null_parrten,"",r.strip()))
            else:
                task_dao.add_one_task_result(self.task_id, url, re.sub(re_util.null_parrten,"",r.strip()))


    def LoadAllLink(self,url,num_retried,depth,keywords):
        pageCode = request.get_html(url)
        if pageCode is not None:
            soup = BeautifulSoup(pageCode,'lxml')
            depth -= 1
            if depth>0:
                for item_a in soup.body.find_all('a'):
                    if item_a.get('href') != None :
                        if item_a.get('href').startswith("/"):
                            subUrl = self.rootLink + item_a.get('href')
                            if not re_util.file_suffix_pattern.search(urlparse.urlparse(subUrl).path):
                                self.spider_queue.add_one(self.task_id, subUrl, depth, keywords)
                        elif re_util.get_domain_name(item_a.get('href')) == self.domain:
                            subUrl = item_a.get('href')
                            if not re_util.file_suffix_pattern.search(urlparse.urlparse(subUrl).path):
                                self.spider_queue.add_one(self.task_id, subUrl, depth, keywords)
                        else:
                            pass
            self.FindAllKeyword(url,keywords,pageCode)
        else:
            if num_retried > 1:
                num_retried -= 1
                self.spider_queue.add_one(self.task_id,url,depth,keywords,num_retried=num_retried)



