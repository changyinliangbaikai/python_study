#!/usr/bin/env python
# coding=utf-8
import time
from simple_queue import SimpleQueue

class SpiderService():
    def __init__(self):
        self.taskQueue = SimpleQueue('spider', 'demo1')
    def out(self,task):
        self.taskQueue.taskIsDoing(task)
        print 'task start'
        time.sleep(5)
        print "task url is %s:"%(task)
        time.sleep(5)
        print 'task complete change task status'
        self.taskQueue.taskComplete(task)
