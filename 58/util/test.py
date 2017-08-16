#!/usr/bin/env python
# coding=utf-8

from mongoengine import connect
import room_info_dao as RoomDao
import datetime
from models import *


def test_add():
    RoomDao.init_add("整租 | 奥体 银城西堤国际一区 三房精装修 看房方便", "http://jxjump.58.com/service?target=INKicKZPP1XJ2FI5AKZJ7lFm4eEH5-Its1GQsB5atrM_WDpQ0YHOYwuof1OgHjeWMScxCigD9oKTeiylz8mxl1d1R3BxuU5SHII2wFPCbh42Izz4Hh89BIjuQ2ZWxh8sumIJs-flxTMeyFVcrgA_hcknDDPdwbUQA1yRJZVyE20Je4wfMIlDHFMEma0sM7xAV8Dakkgn6l0&local=172&pubid=7183495&apptype=0&psid=100173363194660807346835337&entinfo=28731337413174_0&cookie=|||", "http://pic1.58cdn.com.cn/p1/small/n_v1bkuymc6vdv5vrjs3s4na.jpg?w=294&h=220&crop=1",
                     "银城西堤国际", "5500", "58")
    pass


def test_peek():
    room_info = RoomDao.peek()
    return room_info


def test_update():
    room_info = test_peek()
    if room_info is not None:
        RoomDao.completing(room_info.id, datetime.datetime.now(), [1, 2, 3], "1", "1", "1", "1")
        pass
    else:
        print room_info


if __name__ == '__main__':
    connect("find_room_test")
    #test_add()
    #test_update()
    room = RoomInfo.objects(title = None).first()
    print room
    pass
