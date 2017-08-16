#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: jhx
@contact: jhx679@vip.qq.com
@software: PyCharm Community Edition
@file: TestRe.py
@time: 2016/11/25 10:34
"""
import re
path = "/home/testee/jhx/tomcat8/webapps/vp/video/剑皇沙龙/大二骚屄露脸口吃  黑撕来袭 》请备足手纸 少撸两次.mp4"
removeSpace = re.compile('\s+')
result =  re.sub(removeSpace,"",path)
if re.match(removeSpace,path):
    print True
else:
    print False

if re.search(removeSpace,path):
    print True
else:
    print False