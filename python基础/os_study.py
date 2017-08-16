#!/usr/bin/env python
# coding=utf-8
# 自带系统os模块
import os
# print os.path.exists("./find_str.py")
# print os.path.exists("./test_path/1.txt")
# print os.path.exists("./test_path/2.txt")
# 自带系统平台模块可以获取平台信息 如 系统版本 类型 32/64位
import platform


def get_platform_info():
    print platform.platform()
    print platform.system()
    print platform.architecture()


# cpu_count 获取cpu核心数量
import multiprocessing


def get_cpu_count():
    # 获取cpu核心数量
    print multiprocessing.cpu_count()
    pass


# 获取cpu、内存使用率
import psutil

# 获取cpu使用率
def get_cpu_state():
    print psutil.cpu_percent(1)


# 获取内存使用率
def get_memmory_state():
    phymem = psutil.virtual_memory()
    line = "Memory: %5s%% %6s/%s" % (
        phymem.percent,
        str(int(phymem.used / 1024 / 1024)) + "M",
        str(int(phymem.total / 1024 / 1024)) + "M"
    )
    print line


if __name__ == '__main__':
    get_platform_info()
