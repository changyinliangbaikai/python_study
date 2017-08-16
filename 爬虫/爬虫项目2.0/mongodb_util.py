#!/usr/bin/env python
# coding=utf-8
# MongoDB 通用方法类1.0
from pymongo import MongoClient


class MongoUtil:
    def __init__(self, dbName, tableName):
        self.client = MongoClient()
        self.db = self.client[dbName]
        self.table = self.db[tableName]

    def insert_one(self, obj):
        obj_id = self.table.insert(obj)
        return obj_id

    def update_one(self, preObj, afterObj):
        return self.table.update_one(preObj, {'$set':afterObj})

    def find_by_id(self,_id):
        return self.table.find_one({'_id':_id})

    def get_table(self):
        return self.table
