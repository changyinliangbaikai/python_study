#!/usr/bin/env python
# coding=utf-8

import socket
import SpiderController

if __name__ == '__main__':

    motherSpider = SpiderController.SpiderController()
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
                motherSpider.addTask("1111")
                connection.send('add success')
            else:
                connection.send('please go out!')
        except socket.timeout:
            print 'time out'
        connection.close()
