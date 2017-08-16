#!/usr/bin/env python
# coding=utf-8

import multiprocessing
import datetime,time
from models import *



def save_data():
    connect("test")
    p = TestProcess(content="test",add_time = datetime.datetime.now())
    r = p.save()
    print r.to_json()

if __name__ == '__main__':

    p_list = []
    for i in range(4):
        p = multiprocessing.Process(target=save_data)
        p_list.append(p)
        p.start()

    for p in p_list:
        p.join()
    print "end"
