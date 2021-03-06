#!/usr/bin/env python
# coding=utf-8
import multiprocessing
import threading
import time

import spider_service
from spider_queue_dao import SpiderQueue
from task_list_dao import TaskList

class SpiderController():

    task_list = TaskList()
    spider_queue = SpiderQueue()

    def __init__(self,name,max_thread_num=8):
        print 'spiderController has been created'
        self.name = name
        self.max_thread_num = max_thread_num

    def GoSpider(self):
        print "Spider %s is running !"%self.name
        threads = []
        while True:
            for t in threads:
                if not t.is_alive():threads.remove(t)
            while len(threads) < self.max_thread_num and self.spider_queue.is_empty():
                if self.spider_queue.peek():
                    ss = spider_service.SpiderService()
                    t = threading.Thread(target=ss.out,args=(self.spider_queue.peek(),))
                    t.setDaemon(True)
                    t.start()
                    threads.append(t)
            time.sleep(1)
            print 'process %s is running'%self.name


if __name__ == '__main__':
    for i in range(4):
        spider = SpiderController(i)
        p = multiprocessing.Process(target=spider.GoSpider)
        p.start()
    time.sleep(2)





