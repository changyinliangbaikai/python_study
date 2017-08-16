#!/usr/bin/env python
# coding=utf-8

import signal
import time
import os
import Log4p as log

# Define signal handler function
def myHandler(signum, frame):
    print 'I received: ', signum
    log.logINFO('sig_num is %s'%signum)
    os._exit(1)


if __name__ == '__main__':
    print 'main process start :',os.getpid()
    # register signal.SIGTSTP's handler
    signal.signal(signal.SIGINT, myHandler)
    signal.signal(signal.SIGTERM, myHandler)
    while True:
        time.sleep(1)
        # print('End of Signal Demo')
