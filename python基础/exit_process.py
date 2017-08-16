#!/usr/bin/env python
# coding=utf-8
#   UTF-8 without BOM
#
# refer:
#   http://stackoverflow.com/questions/26414704/how-does-a-python-process-exit-gracefully-after-receiving-sigterm-while-waiting?rq=1
#   http://www.cnblogs.com/kaituorensheng/p/4445418.html
# init created: 2016-07-13
# last updated: 2016-07-14
#
#######################################################################
import os
import signal
import multiprocessing
import time
import functools


def test_event():
    e = multiprocessing.Event()
    e.set()
    print e.is_set()


def func_worker(e):
    print 'process %s is started' % os.getpid(),
    while not e.is_set():
        print '. ',
        time.sleep(1)
    print
    print 'process %s is end' % os.getpid()


def test_process_with_event():
    e = multiprocessing.Event()
    p = multiprocessing.Process(target=func_worker, args=(e,))
    p.start()
    p2 = multiprocessing.Process(target=func_worker, args=(e,))
    p2.start()
    a = 0
    while 1:
        if a == 5:
            e.set()
            break
        a += 1
        time.sleep(1)
    time.sleep(1)


def test_signal_handler(e,signum, frame):
    print os.getpid(),signum,
    e.set()
    os._exit(1)


def test_signal(e):
    handler = functools.partial(test_signal_handler,e)
    signal.signal(signal.SIGTERM, handler)

def func_no_e(e):
    print 'process %s is started' % os.getpid(),
    while 1:
        print '. ',
        time.sleep(1)
    # print
    # print 'process %s is end' % os.getpid()
if __name__ == '__main__':
    print 'main pid:',os.getpid()
    e = multiprocessing.Event()
    test_signal(e)
    a = 0

    p = multiprocessing.Process(target=func_worker,args=(e,))
    p.daemon = True
    p.start()
    while True:
        a += 1
        time.sleep(1)
