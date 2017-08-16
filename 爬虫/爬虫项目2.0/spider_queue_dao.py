#!/usr/bin/env python
# coding=utf-8

#爬虫队列表操作类
from mongodb_util import MongoUtil
from pymongo import errors

class SpiderQueue:
    dbName = 'spider'
    tableName = 'spider_queue'
    OUTSTANDING = 1  ##初始状态
    PROCESSING = 2  ##正在下载状态
    PAUSE = 3  ##暂停
    COMPLETE = 4  ##下载完成状态
    mu = MongoUtil(dbName, tableName)

    def is_empty(self):
        """
        这个函数，我的理解是如果下面的表达为真，则整个类为真
        至于有什么用，后面我会注明的（如果我的理解有误，请指点出来谢谢，我也是Python新手）
        $ne的意思是不匹配
        """
        record = self.mu.get_table().find_one(
            {'status': self.OUTSTANDING}
        )
        return True if record else False

    def add_one(self,task_id,url,depth,param):
        spider_obj = {
            'task_id':task_id,
            '_id':url,
            'keywords':param,
            'depth':depth,
            'status':self.OUTSTANDING
        }

        try:
            obj_id = self.mu.insert_one(spider_obj)
            return obj_id
        except errors.DuplicateKeyError as e:
            print u'地址已经存在了'
            pass


    def peek(self):
        record = self.mu.get_table().find_one({
            'status':self.OUTSTANDING
        })
        if record:
            return record['_id']

    def spider_running(self,_id):
        pre_obj = {'_id':_id}
        after_obj = {'status':self.PROCESSING}
        self.mu.update_one(pre_obj,after_obj)

    def spider_complete(self,_id):
        pre_obj = {'_id':_id}
        after_obj = {'status':self.COMPLETE}
        self.mu.update_one(pre_obj,after_obj)

    def add_many(self,objs):
        self.mu.get_table().insert(objs)

    def find_by_id(self,_id):
        return self.mu.find_by_id(_id)