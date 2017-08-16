#!/usr/bin/env python
# coding=utf-8
from multiprocessing import Process, Manager
def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    for i in range(10):
        l.append(i)
    for i in l:
        print i

if __name__ == '__main__':
    manager = Manager()
    d = manager.dict()
    l = manager.list()
    p = Process(target=f, args=(d, l))
    p.start()
    p.join()
    print(d)
    print(l)
