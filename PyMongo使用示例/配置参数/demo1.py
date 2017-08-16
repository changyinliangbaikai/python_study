#!/usr/bin/env python
# coding=utf-8

#测试MongoClient中的几个参数

from pymongo import MongoClient

def test_param():
    client = MongoClient(host="127.0.0.1",connect=False,maxPoolSize=200)
    db = client.get_database("test")
    coll = db.get_collection("test_param")
    coll.insert({"a":11111111})
    for doc in coll.find():
        print doc

def get_connection_to_mongodb(db_name,coll_name):
    client = MongoClient(host="127.0.0.1",connect=False,maxPoolSize=200)
    db = client.get_database(db_name)
    coll = db.get_collection(coll_name)
    return client,db,coll



if __name__ == '__main__':
    test_param()