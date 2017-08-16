#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: jhx
@contact: jhx679@vip.qq.com
@software: PyCharm Community Edition
"""
import re
linkParrten = re.compile('<a.*?href="(.*?html)".*?>')
rootLinkParrten = re.compile('http://.*?/|https://.*?/')
