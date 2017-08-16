#!/usr/bin/env python
# coding=utf-8

import multiprocessing
import os
import time
import platform
import signal
import sys
import functools


def exit_handler(e, signum, frame):
    e.set()


def parent_process():
    print 'main process is running~'
    p = multiprocessing.Process(target=child_process)
    p.start()
    info = os.wait()
    print 'wait process stop :',info
    while True:
        time.sleep(5)
        pass


def child_process():
    print 'child process start,pid :%s' % os.getpid()
    e = multiprocessing.Event()
    p = multiprocessing.Process(target=sub_child_process,args=(e,))
    handler = functools.partial(exit_handler, e)
    signal.signal(signal.SIGTERM, handler)
    p.start()
    p.join()
    print 'child process stop,pid :%s' % os.getpid()
    pass


def sub_child_process(e):
    print 'sub child process start,pid :%s'%os.getpid()
    while not e.is_set():
        time.sleep(1)
    print 'sub child process stop,pid :%s' % os.getpid()
    pass


if __name__ == '__main__':
    if platform.system() == 'Windows':
        pass
    elif platform.system() == 'Linux':
        pid = os.fork()
        if pid == 0:
            parent_process()
        else:
            print "parent process %s" % os.getpid()
            print "parent process exit!"
            pass
    else:
        print 'system %s is not supported!' % platform.system()
    pass
