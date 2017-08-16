#!/usr/bin/env python
# coding=utf-8
import multiprocessing
import Queue,time
import SpiderService
import threading


class SpiderController():

    def __init__(self,max_procNum=8):
        self.procs = multiprocessing.Manager().list()
        self.taskQueue = multiprocessing.Queue()
        p = multiprocessing.Process(target=self.GoSpider, args=(self.taskQueue,self.procs,))
        p.start()




    def addTask(self,url):
        print "add a task, current process number is %s"%(len(self.procs))
        self.taskQueue.put(url)


    def GoSpider(self,taskQueue,procs):
        print "Spider is running !"
        while True:
            for p in procs:
                if not p.is_alive():
                    procs.remove(p)
            if not taskQueue.empty():
                ss = SpiderService.SpiderService()
                p = multiprocessing.Process(target=ss.out,args=(taskQueue.get(),))
                p.start()
                procs.append(p)


            time.sleep(1)









