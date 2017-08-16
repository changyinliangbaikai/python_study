#!/usr/bin/env python
# coding=utf-8

#本类旨在试验方法在自动销毁的时候会调用什么方法
import time
import os

class TestObj:
    def __init__(self):
        print 'init'
    def __del__(self):
        print 'destroied'

    def test(self,a):
        print a

if __name__ == '__main__':
    t = TestObj()
    t.test(1111)
    time.sleep(5)
    print 'main end'
