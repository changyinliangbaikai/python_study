#!/usr/bin/env python
# coding=utf-8

'''
#使用from引用jhxtest模块中的所有函数
from jhxtest import *

if __name__ == '__main__':
    aa = A()
    print_info(111)
'''

#使用import引用
import jhxtest

if __name__ == '__main__':
    a = jhxtest.A()
    jhxtest.print_info(111)