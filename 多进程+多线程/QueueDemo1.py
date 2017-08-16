#!/usr/bin/env python
# coding=utf-8

import multiprocessing


def writer_proc(q):
    try:
        q.put(1, block=False)
    except:
        pass


def reader_proc(q):
    try:
        print q.get(block=False)
    except:
        pass


if __name__ == "__main__":
    q = multiprocessing.Queue()
    for i in range(10):
        q.put(i)
    readers = []
    pool = multiprocessing.Pool(processes=2)
    for i in range(10):
        # reader = multiprocessing.Process(target=reader_proc, args=(q,))
        # readers.append(reader)
        # reader.start()
        pool.apply(func=reader_proc,args=(q,))

    pool.close()
    pool.join()
    print q.empty()

