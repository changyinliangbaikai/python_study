#!/usr/bin/env python
# coding=utf-8

import threading,multiprocessing
import datetime,time
from models import *

def start_thread():
    connect("test")
    t_list = []
    for i in range(4):
        t = threading.Thread(target=save_data)
        t_list.append(t)
        t.start()

    for p in t_list:
        p.join()
    print "end"

def save_data():

    p = TestThread(content="test",add_time = datetime.datetime.now())
    r = p.save()
    print r.to_json()

if __name__ == '__main__':
    for i in range(4):
        p = multiprocessing.Process(target=start_thread)
        p.start()

