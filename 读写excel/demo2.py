#!/usr/bin/env python
# coding=utf-8
import os
import subprocess
import re


def test_aapt(apk_path):
    out = os.popen("aapt dump badging %s"%apk_path)
    #print out.readlines()
    #p = subprocess.call(aapt+" dump badging %s"%apk_path2, shell=True)  # 使用这个可以行
    return out.readlines()

    pass

def get_index_and_package_name():
    dir_path = u'D:\\app\\11'
    files = os.listdir(dir_path)
    for f in files:
            # if f.find('_') > -1:
            #     print f[:f.find('_')], f[f.find('_') + 1:f.rfind('.')]
            get_app_name2(f,os.path.join(dir_path,f))


def get_app_name2(file_name,apk_path):
    lines = test_aapt(apk_path)
    app_name = ""
    package_name = ""
    for line in lines:
        if line.find('application-label:')>-1:
            app_name = line[line.find('\'')+1:len(line)-2]
        if line.find('package: name')>-1:
            package_name = line[line.find('=')+2:line.find('\'',line.find('=')+2)]
    print file_name,',',package_name,',',app_name

def get_app_name(index,file_name,apk_path):
    lines = test_aapt(apk_path)
    app_name = ""
    package_name = ""
    for line in lines:
        if line.find('application-label:')>-1:
            app_name = line[line.find('\'')+1:len(line)-2]
        if line.find('package: name')>-1:
            package_name = line[line.find('=')+2:line.find('\'',line.find('=')+2)]
    if file_name == package_name:
        print index, app_name, package_name
    else:
        print index, app_name, package_name,11111111111
    #os.system("adb uninstall %s"%package_name)
if __name__ == '__main__':
    get_index_and_package_name()