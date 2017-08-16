#!/usr/bin/env python
# coding=utf-8
#主程序

import socket
from spider_controller import SpiderController
import multiprocessing
import time

def run_process():
    for i in range(8):
        spider = SpiderController(i)
        p = multiprocessing.Process(target=spider.GoSpider)
        p.start()

if __name__ == '__main__':

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 10075))
    sock.listen(5)
    while True:
        connection, address = sock.accept()
        try:
            connection.settimeout(5)
            buf = connection.recv(1024)
            if buf == '1':
                connection.send('welcome to server!')
            elif buf == 'add':
                connection.send('add success')
            else:
                connection.send('please go out!')
        except socket.timeout:
            print 'time out'
        connection.close()