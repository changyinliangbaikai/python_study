#!/usr/bin/env python
# coding=utf-8

from multiprocessing import Process, Value, Array,Lock
def f(n, a,l):
    n.value = 3.1415927
    for i in range(len(a)):
        l.acquire()
        a.append(i)
        l.release()
if __name__ == '__main__':
    lock = Lock()
    num = Value('d', 0.0)
    arr = Array('i', range(10))
    p = Process(target=f, args=(num, arr,lock))
    p.start()
    p.join()
    print(num.value)
    print(arr[:])