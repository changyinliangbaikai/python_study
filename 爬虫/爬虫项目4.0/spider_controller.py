#!/usr/bin/env python
# coding=utf-8
import multiprocessing
import threading
import time

import spider_service
from spider_queue_dao import SpiderQueue
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class SpiderController():



    def __init__(self,process_id,max_thread_num=16):
        print 'spiderController has been created'
        self.process_id = process_id
        self.max_thread_num = max_thread_num


    def GoSpider(self):
        print "Spider %s is running !"%self.process_id
        spider_queue = SpiderQueue(self.process_id)
        threads = []
        while True:
            for t in threads:
                if not t.is_alive():threads.remove(t)
            while len(threads) < self.max_thread_num and spider_queue.is_empty():
                record = spider_queue.peek()
                if record:
                    SpiderQueue(self.process_id).spider_running(record['_id'])
                    ss = spider_service.SpiderService(record,self.process_id)
                    t = threading.Thread(target=ss.run_spider)
                    t.setDaemon(True)
                    t.start()
                    threads.append(t)
            time.sleep(0.1)








