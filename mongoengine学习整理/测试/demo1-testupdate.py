#!/usr/bin/env python
# coding=utf-8

from mongoengine import *
import time
import threading


class SpiderQueue(Document):
    task_id = IntField()
    status = IntField()


def add():
    SpiderQueue(task_id=1, status=1).save()


def start():
    SpiderQueue.objects(task_id=1).update(set__status=2)
    if SpiderQueue.objects(status=1):
        print 'update fail,start'
        return None
    return True


def pause():
    SpiderQueue.objects(task_id=1).update(set__status=1)
    if SpiderQueue.objects(status=2):
        print 'update fail,pause'
        return None
    return True


if __name__ == '__main__':
    connect('test_mongo',host='192.168.0.128')
    start_time = time.time()
    # for i in range(5000):
    #     #add()
    #     print 1
    for i in range(200):
        print u'第%s次测试...'%i
        if start():
            time.sleep(0.5)
            if pause():
                time.sleep(0.5)
            else:
                print i
                break
        else:
            print i
            break
    print 'time:', time.time() - start_time
