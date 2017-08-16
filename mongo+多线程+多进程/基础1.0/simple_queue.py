#!/usr/bin/env python
# coding=utf-8

from pymongo import MongoClient,errors


class SimpleQueue():
    OUTSTANDING = 1  ##初始状态
    PROCESSING = 2  ##正在下载状态
    COMPLETE = 3  ##下载完成状态

    def __init__(self,dbName,tableName):
        self.client = MongoClient()
        self.db = self.client[dbName]
        self.table = self.db[tableName]

    def insert(self,url):
        self.table.insert({
            '_id':url,
            'status':self.OUTSTANDING
        })
    def peek(self):
        record = self.table.find_one({'status':self.OUTSTANDING})
        print record
        if record:
            return record['_id']

    def updateStatus(self,url,status):
        self.table.update({'_id':url},{'$set':{
            'status': status
        }})
    def countIsRunning(self):
        return self.table.find({'status':self.PROCESSING}).count()

    def countNotStarting(self):
        return self.table.find({'status':self.OUTSTANDING}).count()

    def taskIsDoing(self,url):
        self.updateStatus(url,self.PROCESSING)

    def taskComplete(self,url):
        self.updateStatus(url,self.COMPLETE)


    def clear(self):
        """这个函数只有第一次才调用、后续不要调用、因为这是删库啊！"""
        self.db.drop()


# sq = SimpleQueue('spider', 'demo1')
# task_id = sq.peek()
# print task_id