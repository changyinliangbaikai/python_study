#!/usr/bin/env python
# coding=utf-8

import util.request_sises as request
import util.room_info_dao as RoomDao
from util.models import *
from mongoengine import *
from bs4 import BeautifulSoup
import time,datetime


def get_title_link(soup):
    title_items = []
    link_items = []
    for i in soup.find_all("div",class_="des"):
        resp = request.get_real_url(i.a.get('href'))
        if resp is not None:
            item_url = resp.url
            item_desc = i.a.string.strip()
            title_items.append(item_desc)
            link_items.append(link_items)
    return title_items,link_items

def get_items(page_code):
    items = []
    soup = BeautifulSoup(page_code, 'lxml')
    item_list = soup.find("ul",class_="listUl").find_all("li")
    for li in item_list:
        tile_and_link = li.find("div",class_="des")
        preview = li.find("div",class_="img_list")
        money = li.find("div",class_="money")
        send_time = li.find("div",class_="sendTime")
        if tile_and_link and preview and money and send_time:
            item_title = tile_and_link.a.string.strip()
            item_url = tile_and_link.a.get('href')
            item_money = money.b.string
            item_type = tile_and_link.find("p",class_="room").string.strip()
            item_addr = tile_and_link.find("p", class_="add").find_all("a")[1].string
            item_time = send_time.string.strip()
            item_preview_link = preview.find("img").get("lazy_src")
            if item_time == u'今天':
                # print type(item_title),type(item_url),type(item_preview_link),type(item_addr),type(item_money)
                RoomDao.init_add(item_title, item_url,
                                 item_preview_link, item_addr, item_money, "58")
                pass


def get_send_time(url):
    try:
        page_code = request.get_html(url)
    except:
        return None
    soup = BeautifulSoup(page_code,'lxml')
    house_title = soup.find("div",class_="house-title")
    #print house_title
    send_time = house_title.p.em.previous_sibling.strip()
    send_time = send_time.replace(u'更新',"")
    print send_time,type(send_time)
    test_date = TestDate()
    test_date.add_time = send_time
    test_date.save()
    t = time.strptime(send_time,'%Y-%m-%d %H:%M:%S')
    print t
    y,m,d,h,M,s = t[0:6]
    send_time = datetime.datetime(y,m,d,h,M,s)
    print datetime.datetime(y,m,d,h,M,s),type(send_time)
    test_date2 = TestDate()
    test_date2.add_time = send_time
    test_date2.save()


def test_get_sent_time():
    url ="http://nj.58.com/zufang/28741150753743x.shtml?entinfo=28741150753743_0&psid=137551520194582451730831830&cookie=|||e6b7424b-fc7e-4703-9cea-cc8714d6290c&local=172&apptype=0&pubid=7103319&trackkey=28741150753743_09d9ac32-bcd1-482b-865a-22e8a08e8aec_20170116135818_1484546298638&fcinfotype=gz"
    #get_send_time(url)
    objs = TestDate.objects(add_time__gt ='2017-01-16 12:17:00')
    for obj in objs:
        print obj.add_time

if __name__ == '__main__':
    connect("find_room")
    for i in range(1):
        url = "http://nj.58.com/chuzu/pn%s/"%(i+1)
        #page_code = open("1.html").read()
        page_code = request.get_html(url)
        get_items(page_code)
        # print type(item_title), type(item_url), type(item_preview_link), type(item_addr), type(item_money)
        # RoomDao.init_add(item_title, item_url,
        #                  item_preview_link, item_addr, item_money, "58")
        # print item_title.encode('utf8','ignore')
        # print str(item_url)
        # print str(item_preview_link)
        # print item_addr.encode('utf8','ignore')
        # print type(item_money.encode('utf8','ignore'))
        # room = RoomInfo.objects(title=item_title,
        #                         link=item_url.encode('utf8','ignore'),
        #                         preview_link=item_preview_link.encode('utf8','ignore'),
        #                         #address=item_addr,
        #                          #price=item_money.encode('utf8','ignore'),
        #                         info_from="58").first()
        # print room.to_json()


    pass
    #test_get_sent_time()
