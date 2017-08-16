#!/usr/bin/env python
# coding=utf-8

from mongoengine import *

class Test(Document):
    test_column = StringField()
    status = IntField()


if __name__ == '__main__':

    connect("test")
    for t in ["2"]:
        Test.objects(test_column = t).update(set__status=2)
