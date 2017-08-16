#!/usr/bin/env python
# coding=utf-8
from mongoengine import *

class Status:
    OUTSTANDING = 1  #初始状态
    PROCESSING = 2   #正在下载状态
    PAUSE = 3        #暂停
    COMPLETE = 4     #下载完成状态

class RoomInfo(Document):
    title = StringField()
    link = StringField()
    preview_link = StringField()
    address = StringField()
    area = StringField()
    room_type = StringField()
    price =StringField()
    send_time = DateTimeField()
    info_from = StringField()
    status = IntField(default=Status.OUTSTANDING)
    pic_list = ListField()
    height = StringField()
    decoration = StringField() #装修
    direction = StringField() #朝向
    desc = StringField() #概况（普通住宅）



class TestDate(Document):
    add_time = DateTimeField()