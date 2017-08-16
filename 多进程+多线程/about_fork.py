#!/usr/bin/env python
# coding=utf-8

import os
import time


if __name__ == '__main__':

    print 'main process %s'%os.getpid()
    pid = os.fork()
    if pid == 0:

        print "child process %s"%os.getpid()
        for i in range(10):
            print i
            time.sleep(1)
        print "child process exit!"
        pass
    else:
        print "parent process %s"%os.getpid()
        print "parent process exit!"