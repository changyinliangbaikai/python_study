#!/usr/bin/env python
# coding=utf-8

import socket

import time
import json
import threading


def send():
    secret_key = 'abcdefg'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 8001))
    sock.settimeout(5)
    a = "a"
    for i in range(10000):
        a += 'a'
    while len(a) - 1024 > 0:
        sock.send('length(1024)')
        sock.send(a[:1024])
        a = a[1024:]
    sock.send('length(1024)')
    sock.send(a)
    sock.send('length(0)')
    print sock.recv(1024)
    sock.close()


def send2():
    secret_key = 'abcdefg'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 10001))
    sock.settimeout(5)
    a = "a"
    for i in range(10000):
        a += 'a'
    sock.send('length(%s)' % len(a))
    if sock.recv(1024)=='0':
        sock.sendall(a)
        print sock.recv(1024)
    else:
        print 'fail'
    sock.close()


def send3():
    secret_key = 'abcdefg'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('192.168.0.128', 10001))
    sock.settimeout(5)
    sock.send('1')
    print sock.recv(1024)
    sock.close()


def test_thread():
    start = time.time()
    t_list = []
    for i in range(20):
        t = threading.Thread(target=send)
        t.start()
        t_list.append(t)
    for t in t_list:
        t.join()
    end = time.time()
    print end - start


def test_normal():
    start = time.time()
    t_list = []
    for i in range(1):
        send2()
    end = time.time()
    print end - start


if __name__ == '__main__':
    test_normal()
