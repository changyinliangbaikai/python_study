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
import datetime
from spider_result_dao import SpiderResult


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
    url = "http://www.runoob.com/python/file-methods.html"
    depth = 1
    keywords = [u'方法']
    task_id = 1
    spider_queue = SpiderQueue()
def test_time():
    start = datetime.datetime.now()
    time.sleep(2)
    end = datetime.datetime.now()
    print end -start

def test_spider_result():
    spider_result = SpiderResult()
    print spider_result.find_by_task_id(1)
    if spider_result.find_by_task_id(1):
        print True
    else:
        print False

def test_spider_regex():
    client = MongoClient()
    coll = client['spider']['spider_regex']
    record = coll.find_one({"_id":"common"})
    keyword_regex =  record["regex"]["keyword"]
    keyword = "岳海云测"
    print keyword_regex
    print type(keyword_regex)
    print str(keyword_regex)%keyword
    #print keyword_regex%keyword


test_spider_regex()



