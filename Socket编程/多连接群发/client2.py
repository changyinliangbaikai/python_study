#!/usr/bin/env python
# coding=utf-8
import socket
import time


def send3():
    secret_key = 'abcdefg'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 6666))
    sock.send('111')
    sock.getsockname()
    time.sleep(5)
    sock.close()


if __name__ == '__main__':
    send3()
