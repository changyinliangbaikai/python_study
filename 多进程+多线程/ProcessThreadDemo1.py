#!/usr/bin/env python
# coding=utf-8

import multiprocessing,threading,time,Queue


class myThread(threading.Thread):
    def __init__(self, threadID, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.q = q
    def getId(self):
        return self.threadID

    def run(self):
        #print "Starting " + str(self.threadID)
        process_data(self.threadID, self.q)
        #print "Exiting " + str(self.threadID)

def process_data(threadName, q):
    print "%s processing %s" % (threadName, q)
    time.sleep(2)


def Spider(name,max_threads = 5):
    taskQueue = Queue.Queue()
    for i in range(20):
        taskQueue.put(i)
    threadID = 1
    threads = []
    print "Spider %s start" %name
    a = True
    while threads or not taskQueue.empty():

        for thread in threads:
            # print "%s thread is %s alive"%(thread.getId(),thread.is_alive())
            if not thread.is_alive():  ##is_alive是判断是否为空,不是空则在队列中删掉
                threads.remove(thread)
        while len(threads) < max_threads and not taskQueue.empty():
            thread = myThread(threadID, taskQueue.get())  ##创建线程
            thread.setDaemon(True)  ##设置守护线程
            thread.start()  ##启动线程
            threads.append(thread)  ##添加进线程队列
            threadID += 1

        #print "threads length : %s ,taskQueue length : %s,threadID is %s" % (len(threads), taskQueue.qsize(), threadID)
        #print "sleep 1"
        if taskQueue.empty():
            break
    print "Spider End"





if __name__ == '__main__':
    print "main start --------------------->"
    pros = []
    for i in range(4):
        p = multiprocessing.Process(target=Spider,args=(i,))
        p.start()
        pros.append(p)
    for p in pros:
        p.join()
    #Spider(taskQueue)
    print "main end -----------------------<"