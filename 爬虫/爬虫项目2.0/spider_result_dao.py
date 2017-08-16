#!/usr/bin/env python
# coding=utf-8
from mongodb_util import MongoUtil
from pymongo import errors
import datetime

class SpiderResult:
    dbName = 'spider'
    tableName = 'spider_result'
    mu = MongoUtil(dbName, tableName)

    def add_one_result(self,task_id,result_obj):
        obj = {
            'task_id':task_id,
            'result_obj':result_obj,
            'start_time':datetime.datetime.now()
        }
        return self.mu.insert_one(obj)

    def update_one_result(self,task_id,result_obj):
        pre_obj = {'task_id':task_id}
        after_obj = {'result_obj':result_obj,'end_time':datetime.datetime.now()}
        return self.mu.update_one(pre_obj,after_obj)

    def find_by_task_id(self,task_id):
        obj = {'task_id':task_id}
        return self.mu.get_table().find_one(obj)

    def find_result_by_task_id(self,task_id):
        obj = {'task_id':task_id}
        record = self.mu.get_table().find_one(obj)
        if record:
            return record['result_obj']
        else:
            return None
