#!/usr/bin/env python
# coding: utf-8
"""
@version: 1.0
@author: jhx
@contact: jhx679@vip.qq.com
@software: PyCharm Community Edition
@file: CreateImage4Video.py
@time: 2016/11/24 14:04
"""
import os
import sys
reload(sys)
sys.setdefaultencoding("utf8")

basepath = u"F:\BaiduYunDownload\idm\三次元福利3"
for filename in os.listdir(basepath):
    #filename = filename.decode("gbk","ignore").encode("utf-8")
    if filename.find(".mp4")>0:
        imageName = filename.split(".mp4")[0] + ".png"
        imagePath = basepath + "\\" + imageName
        filepath = os.path.abspath(basepath+"\\"+filename)
        cmd = "ffmpeg -i "+filepath+" -y -f image2 -ss 5.010 -t 0.001 "+imagePath
        print cmd
        os.system(cmd.decode("utf-8","ignore").encode("gbk","ignore"))