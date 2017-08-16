#!/usr/bin/env python
# coding=utf-8

import requests
import json


def test_ip_loc(ip=None):
    url = ""
    if ip is None:
        url = "http://api.map.baidu.com/location/ip?ak=ZOFZz2n8YNzajdEUlwarv1VONg4vnvxf&coor=bd09ll"
    else:
        url = "http://api.map.baidu.com/location/ip?ak=ZOFZz2n8YNzajdEUlwarv1VONg4vnvxf&coor=bd09ll&ip=%s"%ip

    resp = requests.get(url)
    resp.encoding = 'utf-8'
    print type(resp.content)
    print resp.content
    print type(eval(resp.text))
    # json_obj = eval(resp.text)['content']
    # for key in json_obj.keys():
    #     if isinstance(json_obj[key],dict):
    #         #print json_obj[key]
    #         pass
    #     elif isinstance(json_obj[key],str):
    #         print unicode(json_obj[key])
    print type(resp.text.decode('utf-8'))
    print json.dumps(resp.text,)
    json_obj =  json.loads(resp.text)
    print json_obj
    print json_obj['address']


test_ip_loc()
