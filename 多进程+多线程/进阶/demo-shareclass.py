#!/usr/bin/env python
# coding=utf-8

import multiprocessing
import mongoengine
import threading


class Person(mongoengine.Document):
    name = mongoengine.StringField()
    age = mongoengine.IntField()

class Count(mongoengine.Document):
    num = mongoengine.IntField()

def test_thread_safe():
    print 'start'
    thread_list = []
    for i in range(50):
        t = threading.Thread(target=add_num)
        t.start()
        thread_list.append(t)
    for i in range(50):
        t = threading.Thread(target=add_num)
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()
    print 'end'
    pass

def add_num():
    c = Count.objects.all().first()
    c.num += 1
    c.save()

def reduce_num():
    c = Count.objects.all().first()
    c.num -= 1
    c.save()

def add_person():
    # mongoengine.connect('advanced_tech')
    Person(name='jhx', age=25).save()
    print Person.objects.all().to_json()

if __name__ == '__main__':
    mongoengine.connect('advanced_tech')
    Count(num=0).save()
    test_thread_safe()
    print Count.objects.all().to_json()
