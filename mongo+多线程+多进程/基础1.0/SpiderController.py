#!/usr/bin/env python
# coding=utf-8
import multiprocessing
import threading
import time

import SpiderService
from simple_queue import SimpleQueue


class SpiderController():
    taskQueue = SimpleQueue('spider', 'demo1')
    def __init__(self,max_procNum=8):
        print 'spiderController has been created'




    def addTask(self,url):
        print "add a task, current process number is %s"%(self.taskQueue.countIsRunning())
        self.taskQueue.insert(url)


    def GoSpider(self):
        print "Spider is running !"
        while True:
            if self.taskQueue.peek():
                ss = SpiderService.SpiderService()
                t = threading.Thread(target=ss.out,args=(self.taskQueue.peek(),))
                t.setDaemon(True)
                t.start()
            time.sleep(1)


if __name__ == '__main__':
    spider = SpiderController()
    p = multiprocessing.Process(target=spider.GoSpider)
    p.start()
    time.sleep(2)
    spider.addTask("1111")
    p.join()





