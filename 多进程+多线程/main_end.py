#!/usr/bin/env python
# coding=utf-8
import time
import multiprocessing
import os
#测试主进程结束的时候 子进程会不会结束

def run_while(name):
    for i in range(4):
        print name
        time.sleep(1)


if __name__ == '__main__':
    p_list = []
    pid = os.fork()
    print pid
    p_a = multiprocessing.Process(target=run_while,args=("a",))
    p_b = multiprocessing.Process(target=run_while,args=("b",))
    p_list.append(p_a)
    p_list.append(p_b)
    p_a.daemon = True
    p_b.daemon = True
    p_a.start()
    p_b.start()
    print p_a.is_alive()
    for i in range(2):
        time.sleep(1)
    p_a.terminate()
    time.sleep(3)

    print p_a.is_alive()
    pass
