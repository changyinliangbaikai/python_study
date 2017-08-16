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
        self.__client = MongoClient(connect=False)
        self.__db = self.__client[self.__dbName]
        self.coll = self.__db[self.__collName]


    def __del__(self):
        self.__client.close()

    def clear(self):
        self.coll.drop()

    def is_empty(self):
        """
        $ne的意思是不匹配
        """
        record = self.coll.find_one(
            {'status': self.__OUTSTANDING}
        )
        return True if record else False

    def add_one(self,task_id,url,depth,param,type=1,num_retried=3):
        spider_obj = {
            'task_id':task_id,
            'url':url,
            'type':type,
            'keywords':param,
            'depth':depth,
            'status':self.__OUTSTANDING,
            'num_retried':num_retried
        }

        try:
            pre_obj = self.find_by_id(url)
            if pre_obj:
                if pre_obj['keywords'] == param:
                    #pass
                    self.coll.update_one({'_id': url}, {'$set':spider_obj})
                else:
                    self.coll.update_one({'_id':url},{'$set':spider_obj})
            else:
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