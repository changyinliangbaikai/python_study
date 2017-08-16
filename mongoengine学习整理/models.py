#!/usr/bin/env python
# coding=utf-8
from mongoengine import *

class TestList(Document):
    list_item = ListField()