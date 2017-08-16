#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: jhx
@contact: jhx679@vip.qq.com
@software: PyCharm Community Edition
"""
import re
import tld
linkParrten = re.compile('<a.*?href="(.*?html)".*?>')
rootLinkParrten = re.compile('(http://(.*?))|(https://(.*?)/?)')
null_parrten = re.compile('\n',re.M)
script_parrten = re.compile('<script>.*</script>',re.MULTILINE)
file_suffix_pattern = re.compile('(\.apk|\.ipa|\.jpg|\.png|\.mp4|\.mp3|\.flv)$')

def get_domain_name(url):
    try:
        return tld.get_tld(url)
    except:
        return None
