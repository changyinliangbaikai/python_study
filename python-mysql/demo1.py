#!/usr/bin/env python
# coding=utf-8

import MySQLdb

def test_connect():
    db = MySQLdb.connect("127.0.0.1", "root", "g6s8m3t7s", "spider")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取一条数据库。
    data = cursor.fetchone()
    print "Database version : %s " % data
    # 关闭数据库连接
    db.close()
    return

def test_insert():
    db = MySQLdb.connect("192.168.0.128", "root", "123456", "spider",charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    cursor.execute
    zh_str = str("地址")
    zh_str2 = u"地址"
    zh_str3 = "地址".decode('utf-8')
    print zh_str,zh_str2,zh_str3
    sql = """insert into task_result (task_id,url,content) values (1,%s,'test-content') """
    try:
        cursor.execute(sql,zh_str2)
        db.commit()
    except Exception as e:
        print e
        db.rollback()
    db.close()

def get_db():
    db = MySQLdb.connect(host="192.168.0.128", user="root", passwd="123456", db="spider", charset="utf8")
    #db = MySQLdb.connect(host="123.57.26.246", user="root", passwd="g6s8m3t7s", db="spider", charset="utf8")
    cursor = db.cursor()
    return db,cursor
def find_result():
    db,cursor = get_db()
    sql = "select id from task_result where url = %s and content = %s"
    url = "http://news.sohu.com/20170103/n477632051.shtml"
    content = u"习近平亲力亲为打造全球伙伴关系网1111"
    #print sql%url
    try:
        cursor.execute(sql,(url,content,))
        print cursor.rowcount
        results = cursor.fetchall()
        print results
    except Exception as e :
        print e
        result = None
    db.close()

def find_all():
    db, cusor = get_db()
    try:
        sql = "select * from task_list where userid = 1 limit 1"
        cusor.execute(sql)
        results = cusor.fetchall()
        if results:
            print True
        else:
            print False
        print type(results),len(results)
        for r in results:
            print r
    except:
        print "Exception"
    db.close()

if __name__ == '__main__':
    test_connect()