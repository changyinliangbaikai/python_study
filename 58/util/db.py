#!/usr/bin/env python
# coding=utf-8
import pymongo

def get_db(db_name):
    client = pymongo.MongoClient(connect=False)
    db = client[db_name]
    return db

def insert(db_name,coll_name,obj):
    db = get_db(db_name)
    coll = db[coll_name]
    try:
        coll.insert(obj)
    except:
        return None