#!/usr/bin/env python
# coding=utf-8

import jieba

def start(zh_str):
    results = jieba.cut(zh_str)
    for r in results:
        print r

if __name__ == '__main__':
    zh_str = u'南京积分落户政策'
    start(zh_str)
