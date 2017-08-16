#!/usr/bin/env python
# coding=utf-8

from models import RoomInfo, Status


def init_add(title, link, preview_link, address, price, info_from):
    room = RoomInfo.objects(title=title.encode('utf8','ignore'),
                            link=link.encode('utf8','ignore'),
                            preview_link=preview_link.encode('utf8','ignore'),
                            address=address.encode('utf8','ignore'),
                            price=price.encode('utf8','ignore'),
                            info_from=info_from.encode('utf8','ignore')).first()
    if room:
        if room.send_time is not None:
            room.update(set__status=Status.OUTSTANDING)
            pass
        pass
    else:
        RoomInfo(title=title, link=link, preview_link=preview_link, address=address,
                 price=price, info_from=info_from).save()
    pass


def completing(id, send_time, pic_list, height, decoration, direction, desc):
    RoomInfo.objects(id = id).update(send_time=send_time, pic_list=pic_list, height=height,
                                     decoration=decoration, direction=direction, desc=desc,
                                     status=Status.COMPLETE)
    pass


def peek():
    return RoomInfo.objects(status=Status.OUTSTANDING).first()
    pass
