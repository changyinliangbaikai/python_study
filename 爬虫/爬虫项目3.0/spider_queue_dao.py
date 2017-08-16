#!/usr/bin/env python
# coding=utf-8

#爬虫队列表操作类
from pymongo import errors,MongoClient
from process_manage_dao import ProcessList

class SpiderQueue:
    __dbName = 'spider'
    __collName = 'spider_queue_%s'
    __OUTSTANDING = 1  ##初始状态
    __PROCESSING = 2  ##正在下载状态
    __PAUSE = 3  ##暂停
    __COMPLETE = 4  ##下载完成状态
    __process_list = ProcessList()
    def __init__(self,process_id):
        self.__process_id = process_id
        self.__collName = self.__collName%process_id
        self.__client = MongoClient()
        self.__db = self.__client['spider']
        if not self.__collName in self.__db.collection_names():
            self.__db.create_collection(self.__collName,capped=True,size=20000,max=20000)
        self.coll = self.__db[self.__collName]

    def __del__(self):
        self.__client.close()

    def clear(self):
        self.coll.drop()

    def is_empty(self):
        """
        这个函数，我的理解是如果下面的表达为真，则整个类为真
        至于有什么用，后面我会注明的（如果我的理解有误，请指点出来谢谢，我也是Python新手）
        $ne的意思是不匹配
        """
        record = self.coll.find_one(
            {'status': self.__OUTSTANDING}
        )
        return True if record else False

    def add_one(self,task_id,url,depth,param,type=1):
        spider_obj = {
            'task_id':task_id,
            '_id':url,
            'type':type,
            'keywords':param,
            'depth':depth,
            'status':self.__OUTSTANDING
        }

        try:
            obj_id = self.coll.insert(spider_obj)
            self.__process_list.process_task_add(self.__process_id)
            return obj_id
        except errors.DuplicateKeyError as e:
            print u'地址已经存在了'
            pass


    def peek(self):
        record = self.coll.find_one({
            'status':self.__OUTSTANDING
        })
        if record:
            return record

    def spider_running(self,_id):
        pre_obj = {'_id':_id}
        after_obj = {'status':self.__PROCESSING}
        return self.coll.update_one(pre_obj, {'$set':after_obj})

    def spider_complete(self,_id):
        pre_obj = {'_id':_id}
        after_obj = {'status':self.__COMPLETE}
        self.__process_list.process_task_reduce(self.__process_id)
        return self.coll.update_one(pre_obj, {'$set':after_obj})

    def add_many(self,objs):
        return self.coll.insert(objs)

    def find_by_id(self,_id):
        return self.coll.find_one({'_id':_id})

    def count_all_by_task_id(self,task_id):
        return self.coll.find({'task_id':task_id}).count()

    def count_complete_by_task_id(self,task_id):
        return self.coll.find({'task_id':task_id,'status':self.__COMPLETE}).count()