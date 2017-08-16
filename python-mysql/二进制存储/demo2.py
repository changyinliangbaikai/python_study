#!/usr/bin/env python
# coding=utf-8

import MySQLdb

def get_db():
    db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="123456", db="spider", charset="utf8")
    #db = MySQLdb.connect(host="192.168.0.128", user="root", passwd="123456", db="spider", charset="utf8")
    # db = MySQLdb.connect(host="123.57.26.246", user="root", passwd="g6s8m3t7s", db="spider", charset="utf8")
    cursor = db.cursor()
    return db, cursor

def insert_file():
    f = open("C:\\Users\\Administrator\\Desktop\\1.jar", "rb")
    b = f.read()
    print len(b), type(b)
    f.close()
    sql = 'INSERT INTO Dem_Picture (PicData) VALUES (%s)'
    db, cursor = get_db()
    try:
        cursor.execute(sql, (b,))

        db.commit()
    except Exception,e:
        print e
    cursor.close()
    db.close()

if __name__ == '__main__':
    insert_file()
