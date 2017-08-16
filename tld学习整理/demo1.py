#!/usr/bin/env python
# coding=utf-8

import tld
import urlparse

def test_parse_url(url):
    print tld.get_tld(url)#域名
    u = urlparse.urlparse(url)
    print u.query #参数
    print u.geturl()#地址本身
    print u.fragment #空 碎裂部分？ 不太理解
    print u.hostname #主机地址
    print u.netloc #也是主机地址
    print u.params #空 参数？ 什么参数？
    print u.password #None
    print u.username #None
    print u.path #主机地址后面的地址
    print u.port #None
    print u.scheme #http  通信协议

    net_loc = u.netloc
    domain = tld.get_tld(url)
    if net_loc.find(domain):
        print net_loc[:net_loc.find(domain)-1]
    else:
        print "No"






if __name__ == '__main__':
    url = "http://souhu.com/1111?aa=22&bb=33"
    test_parse_url(url)