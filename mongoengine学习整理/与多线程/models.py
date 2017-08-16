#!/usr/bin/env python
# coding=utf-8

from mongoengine import *

class TestThread(Document):
    content = StringField()
    add_time = DateTimeField()