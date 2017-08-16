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
import re
reload(sys)
sys.setdefaultencoding("utf8")

removeSpace = re.compile('\s+')
def ListFile(path):
    basepath = os.path.abspath(path)
    print basepath
    for filename in os.listdir(basepath):
        filepath = basepath+"\\"+filename
        haveSpace = re.search(removeSpace,filepath)
        if haveSpace:
            os.rename(filepath,re.sub(removeSpace,"",filepath))
            filepath = re.sub(removeSpace,"",filepath)
            filename = re.sub(removeSpace,"",filename)
        print filepath
        if os.path.isdir(filepath):
            ListFile(filepath)
        else:
            if filename.find(".mp4")>0:
                imageName = filename.split(".mp4")[0] + ".png"
                print "imageName: ",imageName
                imagePath = basepath + "\\" + imageName
                if os.path.exists(imagePath)==False:
                    cmd = "ffmpeg -i "+filepath+" -y -f image2 -ss 5.010 -t 0.001 "+imagePath
                    print cmd
                    os.system(cmd)

print sys.argv[1]
dirPath = sys.argv[1]
ListFile(dirPath)
