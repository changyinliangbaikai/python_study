#!/usr/bin/env python
# coding=utf-8
#主程序

import socket
import multiprocessing
import time
from process_controller import ProcessManage
from spider_controller import SpiderController




def run_process():
    process_manage = ProcessManage()
    process_manage.run_task_process(1)
    mp = multiprocessing.Process(target=process_manage.run_manage_process)
    mp.start()

if __name__ == '__main__':
    run_process()
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.bind(('127.0.0.1', 10075))
    # sock.listen(5)
    # while True:
    #     connection, address = sock.accept()
    #     try:
    #         connection.settimeout(5)
    #         buf = connection.recv(1024)
    #         if buf == '1':
    #             connection.send('welcome to server!')
    #         elif buf == 'add':
    #             connection.send('add success')
    #         else:
    #             connection.send('please go out!')
    #     except socket.timeout:
    #         print 'time out'
    #     connection.close()