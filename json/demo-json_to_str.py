#!/usr/bin/env python
# coding=utf-8
import json

def to_json(json_str):
    obj = json.loads(json_str)
    print type(obj)
    print obj

def to_str(json_obj):
    obj = json.dumps(json_obj)
    print type(obj)
    print obj
    return obj



if __name__ == '__main__':
    json_obj = {'status':1,'result':'ok'}
    json_str = '{"status":1,"result":"ok"}'
    #json_str = to_str(json_obj)
    to_json(json_str)