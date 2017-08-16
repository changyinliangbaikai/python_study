#!/usr/bin/env python
# coding=utf-8

from pymongo import MongoClient

class SpiderResult:
    __client = MongoClient()
    __db = __client['spider']
    __coll = __db['task_result']

    def __del__(self):
        self.__client.close()

    def add_one(self,task_id,url,content):
        obj = {
            'task_id':task_id,
            'url':url,
            'content':content

        }
        if not self.__coll.find_one(obj):
            return self.__coll.insert(obj)
        return

    def find_by_task_id(self,task_id):
        obj = {'task_id':task_id}
        return self.__coll.find(obj)
