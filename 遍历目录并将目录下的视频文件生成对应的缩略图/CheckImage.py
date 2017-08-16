#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: jhx
@contact: jhx679@vip.qq.com
@software: PyCharm Community Edition
@file: CheckImage.py
@time: 2016/11/25 11:10
"""
import os
import sys
import re
reload(sys)
sys.setdefaultencoding("utf8")

def ListFile(path):
    basepath = os.path.abspath(path)
    for filename in os.listdir(basepath):
        filepath = basepath+"/"+filename
        if os.path.isdir(filepath):
            ListFile(filepath)
        else:
            if filename.find(".mp4")>0:
                imageName = filename.split(".mp4")[0] + ".png"
                imagePath = basepath + "/" + imageName
                if os.path.exists(imagePath)==False:
                    print filepath


dirPath = "."
ListFile(dirPath)