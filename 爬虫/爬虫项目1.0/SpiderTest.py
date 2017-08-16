#!/usr/bin/env python
#coding=utf-8

import re
import ReUtil

url = "http://www.baidu.com/1111/222"
items = re.findall(ReUtil.rootLinkParrten,url)
print items[0][0:len(items[0])-1]
currentUrl = url[0:url.rfind("/")]
print currentUrl