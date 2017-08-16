#!/usr/bin/env python
# coding=utf-8
# 爬虫任务列表操作类
from mongodb_util import MongoUtil
import datetime


class TaskList:
    dbName = 'spider'
    tableName = 'task_list'
    OUTSTANDING = 1  ##初始状态
    PROCESSING = 2  ##正在下载状态
    PAUSE = 3  ##暂停
    COMPLETE = 4  ##下载完成状态
    mu = MongoUtil(dbName, tableName)

    def add_one(self, name, root_url, param, depth,type=1):
        obj = {'name': name,
               'root_url': root_url,
               'param': param,
               'depth':depth,
               'status': self.OUTSTANDING,
               'type': type,
               'completion': 0.0,
               'start_time': datetime.datetime.now()}
        task_id = self.mu.insert_one(obj)
        return task_id

    def peek(self):
        return self.mu.get_table().find_one({'status':self.OUTSTANDING})


    def count_running_tasks(self):
        return self.mu.get_table().find({'status': self.PROCESSING}).count()

    def find_all_task(self):
        return self.mu.get_table().find()

    def task_running(self,_id):
        pre_obj = {'_id':_id}
        after_obj = {'status':self.PROCESSING}
        self.mu.update_one(pre_obj,after_obj)

    def task_complete(self,_id):
        pre_obj = {'_id': _id}
        after_obj = {'status': self.COMPLETE}
        self.mu.update_one(pre_obj, after_obj)

    def change_completion_by_id(self,_id,completion):
        pre_obj = {'_id': _id}
        after_obj = {'completion':completion}
        self.mu.update_one(pre_obj,after_obj)

    def find_by_task_id(self,_id):
        return self.mu.find_by_id(_id)