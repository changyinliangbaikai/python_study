#!/usr/bin/env python
# coding=utf-8
import multiprocessing
import multiprocessing
import threading
import time
from bson.objectid import ObjectId
from pymongo import MongoClient
from spider_queue_dao import SpiderQueue
from task_list_dao import TaskList


def test_dao():
    spider_queue = SpiderQueue()
    obj_id = spider_queue.add_one(1, "5555555555", [1, 2, 3])
    print obj_id
    print spider_queue.mu.get_table().find_one({'_id': obj_id})
    spider_queue.spider_running(obj_id)
    print spider_queue.find_by_id(obj_id)
    print spider_queue.mu.get_table().find_one({'_id': ObjectId(obj_id)})
    # print spider_queue.mu.get_table().find({"_id":ObjectId(obj_id)})
    # client = MongoClient()
    # coll = client['spider']['spider_queue']
    # #print coll.find_one({"status":1})
    # for recoed in coll.find({'status':1}):
    #     print recoed
    # obj = {
    #     'status':1,
    #     'url':'5555'
    # }
    # obj_id = coll.insert(obj)
    # print obj_id


def add_task():
    spider_queue = SpiderQueue()
    for i in range(1):
        obj_id = spider_queue.add_one(i, "this is %s" % i, [i, i + 1, i + 2])
        print obj_id


client = MongoClient()
coll = client['spider']['spider_queue']
record = coll.find_one()
print record,type(record)
