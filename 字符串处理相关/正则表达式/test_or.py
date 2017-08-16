#!/usr/bin/env python
# coding=utf-8
import re

def test_or():
    zh_str = u'一二三四五六七八'
    zh_re = u'一二|五八'
    print re.findall(re.compile(zh_re),zh_str)  #[u'\u4e00\u4e8c']
    pass



if __name__ == '__main__':
    test_or()