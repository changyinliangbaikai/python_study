#!/usr/bin/env python
# coding=utf-8

import multiprocessing
import threading
import time
from bson.objectid import ObjectId
from bson.codec_options import CodecOptions
from pymongo import MongoClient
from spider_queue_dao import SpiderQueue
from task_list_dao import TaskList
import datetime
from result_dao_bak import SpiderResult
from process_manage_dao import ProcessList
import requests
from bs4 import BeautifulSoup
import re
import re_util
import urllib
import urlparse

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


def test_capped_collection():
    client = MongoClient()
    db = client['spider']
    db.get_collection('test_capped').drop()
    coll = db.create_collection('test_capped',capped=True,size=10000,max=10000)
    obj = coll.insert({"a":1111})
    print obj
    coll2 = db['test_capped2']
    o2 = coll2.insert({'a':111})#只有insert才会返回id
    print o2




def test_db():
    client = MongoClient()
    db = client['spider']
    colls = db.collection_names()
    coll = 'spider_queue'
    if coll in colls:
        print True
    else:
        print False

class test_init:
    def __init__(self):
        spider_queue = SpiderQueue(1)

    def test_go(self):
        for i in range(5):
            print i
            time.sleep(1)
def test_process_dao():
    pl = ProcessList()
    obj = pl.find_process_id_by_least_task_number()
    print obj
    # client = MongoClient()
    # db = client['spider']
    # coll = db['process_list']
    # print coll.find().sort()

def test_task_list_dao():
    task_list = TaskList()
    url = "http://cuiqingcai.com/977.html"
    keyword = [u'正则表达式']
    obj = task_list.add_one('b',url,keyword,1)
    print obj

def test_spider_queue_dao():
    spider_queue = SpiderQueue(0)
    task_id = '5860c4d9540b62299474909c'
    print task_id
    all_spider_task = spider_queue.count_all_by_task_id(ObjectId(task_id))
    completed = spider_queue.count_complete_by_task_id(ObjectId(task_id))
    completion = float(completed / all_spider_task)
    print all_spider_task,completed
    print completion
    print float('%.2f'%completion)
    # client = MongoClient()
    # db = client['spider']
    # coll = db['spider_queue_0']
    # records = coll.find({'task_id':ObjectId(task_id)})
    #
    # for record in records:
    #     print record

    return


def test_int_and_float():
    a = float(5)
    b = float(6)
    print type(a),type(b)
    print a/b
    return

def test_process_and_dict():
    client = MongoClient()
    db = client['spider']
    coll = db['test']
    coll.insert_one({'a':11111111})
    client.close()
    time.sleep(20)

def test_request_bs4():
    url = "http://www.runoob.com/python/file-methods.html"
    page_code = requests.get(url).text
    soup = BeautifulSoup(page_code,'lxml')
    keywords = [u"语句"]
    for key in keywords:
        results = soup.find_all(text=re.compile(key))
        print len(results)
        for r in results:
            if len(r.find_parents('a')) > 0:
                print re.sub(re_util.null_parrten,"",r),r.find_parents('a')[0].get('href')
            else:
                print r

def test_urllib():
    url = 'https://souhu.com/sssss'
    proto, rest = urllib.splittype(url)
    res, rest = urllib.splithost(rest)
    print proto
    print "unkonw" if not res else res
    print rest


def test_urlparse():
    url = 'https://www.souhu.com/sssss'
    r = urlparse.urlparse(url)
    print r.scheme,r.netloc,r.path,r.fragment
    print r.scheme+"://"+r.netloc


print u'\u6b63\u5728\u66f4\u6362\u4ee3\u7406\uff0c10S\u540e\u5c06\u91cd\u65b0\u83b7\u53d6\u5012\u6570\u7b2c'



