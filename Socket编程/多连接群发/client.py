#!/usr/bin/env python
# coding=utf-8
import socket


def send3():
    secret_key = 'abcdefg'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 6666))
    while True:
        try:
            buf = sock.recv(4096)
            print buf
        except Exception as e:
            print e
            sock.close()
            break


if __name__ == '__main__':
    send3()
