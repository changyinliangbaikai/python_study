#!/usr/bin/env python
# coding=utf-8

import requests
import json


def test_poi():
    ak = "ZOFZz2n8YNzajdEUlwarv1VONg4vnvxf"
    baidu_place_url = "http://api.map.baidu.com/place/v2/search?q=%s&region=%s&output=json&ak=%s"
    target_place = u'中泰国际公寓'
    city = u'南京'
    resp = requests.get(baidu_place_url%(target_place,city,ak))
    print resp.text
    loc_obj = json.loads(resp.text)
    print type(loc_obj)
    print type(loc_obj['results'][0])
    print loc_obj['results'][0]["location"] #百度坐标经纬度


def test_route():
    ak = "ZOFZz2n8YNzajdEUlwarv1VONg4vnvxf"
    url = "http://api.map.baidu.com/routematrix/v2/driving?output=json&tactics=11&origins=31.971885,118.721934&destinations=32.00644,118.73344&ak=ZOFZz2n8YNzajdEUlwarv1VONg4vnvxf"
    resp = requests.get(url%ak)
    print resp.text

def test_direction():
    ak = "ZOFZz2n8YNzajdEUlwarv1VONg4vnvxf"
    url = "http://api.map.baidu.com/direction/v2/transit?origin=31.971885,118.721934&destination=32.00644,118.73344&ak=%s"
    resp = requests.get(url % ak)
    print resp.text
    loc_obj = json.loads(resp.text)
    print loc_obj['result']['routes']

if __name__ == '__main__':
    test_direction()