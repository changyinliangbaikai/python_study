#!/usr/bin/env python
# coding=utf-8

import Queue
import multiprocessing

import time


def sayHi(name,delay):
    print 'Hi my name is %s' % name
    time.sleep(delay)
    print 'process %s exit'%name


if __name__=='__main__':
    lock = multiprocessing.Lock()
    print multiprocessing.cpu_count()
    for i in range(4):
        p = multiprocessing.Process(target=sayHi,args=(i,5))
        p.start()

    print "main exit"