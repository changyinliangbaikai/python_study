#!/usr/bin/env python
# coding=utf-8

import threading
import time
import multiprocessing

class A(threading.Thread):

    def __init__(self,value):
        threading.Thread.__init__(self)
        self.value = value

    def run(self):
        p = multiprocessing.Process(target=out,args=(self.value,))
        p.start()
def out(value):
    time.sleep(5)
    print value
if __name__ == '__main__':
    print "main start"

    a = A("111")
    a.start()

    print "main end"