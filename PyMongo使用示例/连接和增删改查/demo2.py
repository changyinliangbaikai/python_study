#!/usr/bin/env python
# coding=utf-8

#获取具体某个字段的值
from pymongo import MongoClient

client = MongoClient()
db = client['spider']
table = db['demo1']

record = table.find_one({'status':2})
print record
print record['status']
print record['_id']