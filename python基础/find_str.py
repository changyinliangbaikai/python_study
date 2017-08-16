#!/usr/bin/env python
# coding=utf-8
import re
en_str = "a.html"
html_pattern = re.compile('.*?\.html$')
print re.match(html_pattern,en_str)
if re.match(html_pattern,en_str):
    print True