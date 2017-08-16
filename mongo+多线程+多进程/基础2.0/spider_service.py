#!/usr/bin/env python
# coding=utf-8
import time
from spider_queue_dao import SpiderQueue
from task_list_dao import TaskList
class SpiderService():
    def __init__(self):
        self.spider_queue = SpiderQueue()
        self.task_list = TaskList()
    def out(self,_id):
        self.spider_queue.spider_running(_id)
        print 'task start'
        time.sleep(5)
        print "spider id is %s:"%(_id)
        print self.spider_queue.find_by_id(_id)
        time.sleep(5)
        print 'task complete change task status'
        self.spider_queue.spider_complete(_id)
