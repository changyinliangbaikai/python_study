#!/usr/bin/env python
# coding=utf-8

import MySQLdb
from spider_result_dao import SpiderResult
import Log4p as log
import datetime

def get_db():
    db = MySQLdb.connect(host="123.57.26.246", user="root", passwd="g6s8m3t7s", db="spider", charset="utf8")
    cursor = db.cursor()
    return db,cursor

def copy_result_to_mysql(task_id):
    sql = """insert into task_result (taskId,url,content) values (%s,%s,%s)"""
    db,cursor = get_db()
    spider_result = SpiderResult()
    results = spider_result.find_by_task_id(task_id)
    l = []
    for r in results:
        l.append((1,r['url'],r['content']))
    try:
        cursor.executemany(sql,l)
        db.commit()
    except:
        print "exception "
        db.rollback()
    db.close()

def task_peek():
    db,cursor = get_db()
    sql = "select id,url,type,depth,keyword from task_list where status = 1 limit 1"
    result = ""
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
    except Exception as e :
        print e
        result = None
    db.close()
    return result

def add_one_task_result(task_id,url,content):
    sql = "insert into task_result (taskId,url,content) values (%s,%s,%s)"
    db, cursor = get_db()
    try:
        cursor.execute(sql,(task_id,url,content))
        db.commit()
    except:
        print "exception "
        db.rollback()
    db.close()

def updata_completion(task_id,c):
    sql = "update task_list set completion = %s where id = %s"
    db, cursor = get_db()
    try:
        cursor.execute(sql, (c,task_id))
        db.commit()
    except:
        print "exception "
        db.rollback()
    db.close()

def update_status_and_endtime(task_id,status,endtime=None):
    sql = "update task_list set status = %s,endTime = %s where id = %s"
    db, cursor = get_db()
    try:
        cursor.execute(sql, (status,endtime,task_id))
        db.commit()
    except Exception as e:
        print e
        db.rollback()
    db.close()

