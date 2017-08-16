#!/usr/bin/env python
# coding=utf-8

from mongoengine import *
from models import *



class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    age = IntField(unique=True)

def test_list():
    list_obj = [1,2,3,4]
    obj = TestList.objects.first()
    obj.list_item = [2,3,4,5,6]
    #TestList.objects(id=obj.id).update(set__list_item = [2,3,4,5,6])
    obj.update(list_item = [2,3,4,5,6])
    print TestList.objects.first().to_json()


if __name__ == '__main__':
    connect("test",host='192.168.0.128')
    u = User()
    u.email = 'aaa'
    u.first_name = 'test'
    u.save()




