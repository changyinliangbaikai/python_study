#!/usr/bin/env python
# coding=utf-8

from mongodb_util import MongoUtil
from pymongo import MongoClient

class ProcessList:
    __dbName = "spider"
    __tableName = "process_list"
    __RUNNING = 1
    __STOP = 2

    def __init__(self):
        self.__client = MongoClient(connect=False)
        db = self.__client[self.__dbName]
        if not self.__tableName in db.collection_names():
            db.get_collection(self.__tableName).drop()
            db.create_collection(self.__tableName, capped=True, size=20, max=20)
        self.coll = db[self.__tableName]

    def __del__(self):
        self.__client.close()

    def clear(self):
        return self.coll.drop()

    def process_regist(self,process_id):
        obj = {
            '_id':process_id,
            'task_number':0,
            'status':self.__RUNNING,
            'max_thread_size':1
        }
        if not self.coll.find_one({'_id':process_id}):
            obj_id = self.coll.insert(obj)
            return obj_id


    def find_process_id_by_least_task_number(self):
        if self.coll.find().count()>0:
            records = self.coll.find().sort('task_number',1).limit(-1)
            for record in records:
                return record['_id']
        return None

    def process_task_add(self,_id):
        obj = {'_id':_id}
        record = self.coll.find_one(obj)
        if record:
            task_number = record['task_number']
            return self.coll.update_one(obj,{'$set':{'task_number':task_number+1}})

    def process_task_reduce(self,_id):
        obj = {'_id': _id}
        task_number = self.coll.find_one(obj)['task_number']
        if task_number - 1 < 0:
            task_number = 0
        else:
            task_number -= 1
        return self.coll.update_one(obj, {'$set': {'task_number': task_number}})

    def add_max_thread_size(self,_id,max_thread_size):
        return self.coll.update_one({'_id':_id},{'$set':{'max_thread_size':max_thread_size}})

    def start_process(self,_id):
        return self.coll.update_one({'_id': _id}, {'$set': {'status': self.__RUNNING}})

    def stop_process(self,_id):
        return self.coll.update_one({'_id': _id}, {'$set': {'status': self.__STOP}})