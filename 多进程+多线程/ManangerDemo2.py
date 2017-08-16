#!/usr/bin/env python
# coding=utf-8


import multiprocessing,time


class Mana():
    def __init__(self,list,queue):
        self.spiderList = list
        self.taskQueue = queue
        p = multiprocessing.Process(target=self.GoSpider,args=(self.taskQueue,self.spiderList))
        p.start()


    def addTask(self,url):
        self.taskQueue.put(url)

    def GoSpider(self,taskQueue,spiderList):
        print "Spider is running !"
        while True:
            if len(spiderList)>0:
                for spider in spiderList:
                    if not spider.is_alive():
                        spiderList.remove(spider)
            if not taskQueue.empty():
                p = multiprocessing.Process(target=out,args=(taskQueue.get(),))
                p.start()
                spiderList.append(p)


            time.sleep(1)

def out(url):
    print url

if __name__ == '__main__':
    taskQueue = multiprocessing.Queue()
    processList = multiprocessing.Manager().list()
    m = Mana(processList,taskQueue)
    #m.addTask('1111')