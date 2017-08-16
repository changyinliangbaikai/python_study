#!/usr/bin/env python
# coding=utf-8

from mongoengine import *

class TestProcess(Document):
    content = StringField()
    add_time = DateTimeField()