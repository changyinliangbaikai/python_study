#!/usr/bin/env python
# coding=utf-8
from mongoengine import *

class ProcessItem(Document):
    task_num = IntField()
    status = IntField()  #进程启停标志
    max_thread_num = IntField()
    platform_type = IntField()
    real_status = IntField() # 进程真实状态
    pass

def add():
    ProcessItem(task_num=0).save()

def reset():
    ProcessItem.objects(task_num__gt=3).update(set__task_num=1)


if __name__ == '__main__':
    connect('test_mongo')
    reset()
    print ProcessItem.objects.all().to_json()