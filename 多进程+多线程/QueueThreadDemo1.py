#!/usr/bin/env python
# coding=utf-8

# 测试线程池与队列
import threading
import Queue
import time


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
    #time.sleep(2)

queueLock = threading.Lock()
theadQueue = Queue.Queue(4)
taskQueue = Queue.Queue()
threads = []
threadList = ["Thread-1", "Thread-2", "Thread-3"]
threadID = 1

for i in range(10):
    taskQueue.put(i)

# 创建新线程
print taskQueue.qsize()
max_threads = 5
a = True
while threads or not taskQueue.empty():

    for thread in threads:
        #print "%s thread is %s alive"%(thread.getId(),thread.is_alive())
        if not thread.is_alive():  ##is_alive是判断是否为空,不是空则在队列中删掉
            threads.remove(thread)
    while len(threads) < max_threads and not taskQueue.empty():

        thread = myThread(threadID, taskQueue.get())  ##创建线程
        thread.setDaemon(True)  ##设置守护线程
        thread.start()  ##启动线程
        threads.append(thread)  ##添加进线程队列
        threadID += 1
    if a:
        #queueLock.acquire()
        for i in range(10):
            taskQueue.put(i)
        #queueLock.release()
    a = False
    print "threads length : %s ,taskQueue length : %s,threadID is %s" % (len(threads),taskQueue.qsize(),threadID)
    print "sleep 1"
    if taskQueue.empty():
        break

print "main exit"