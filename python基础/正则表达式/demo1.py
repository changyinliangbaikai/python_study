#!/usr/bin/env python
# coding=utf-8

import re


def test1():
    key_pattern = re.compile('(.*?)\|(.*?)\&(.*?)-(.*)')
    keyword = 'A,B|D,H&C,E-F,G'
    keyword2 = 'A,B|D,H&C,E-'
    keyword3 = 'A,B|D,H&-F,G,p'
    keyword4 = 'A,B|&C,E-F,G,p'
    zh_str1 = u"ABCDEFG"
    zh_str2 = u"ABCDEFG"
    zh_str3 = u"ABCDEFG"
    zh_str4 = u"ABCDEFG"
    zh_str5 = u"ABCDEFG"
    and_pattern = re.compile('(AB)|(G)')
    print re.findall(and_pattern, zh_str1)
    print re.findall(key_pattern,keyword4)
    print re.findall(re.compile('-(.*)'),keyword)
    pass


if __name__ == '__main__':
    test1()
