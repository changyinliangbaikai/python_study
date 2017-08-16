#!/usr/bin/env python
# coding=utf-8
import time
from spider_queue_dao import SpiderQueue
from task_list_dao import TaskList
from do_spider import Spider

class SpiderService():
    def __init__(self,url):
        self.spider_queue = SpiderQueue()
        self.task_list = TaskList()
        self.spider_url = url
        print self.spider_url
    def out(self,_id):
        self.spider_queue.spider_running(_id)
        print 'task start'
        time.sleep(5)
        print "spider id is %s:"%(_id)
        print self.spider_queue.find_by_id(_id)
        time.sleep(5)
        print 'task complete change task status'
        self.spider_queue.spider_complete(_id)

    def run_spider(self):
        self.spider_queue.spider_running(self.spider_url)
        param = self.spider_queue.find_by_id(self.spider_url)
        s = Spider()
        s.do_start(param)
        self.spider_queue.spider_complete(self.spider_url)
