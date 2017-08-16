#!/usr/bin/env python
# coding=utf-8
import socket
import struct
import os
import json

def send_msg():
    secret_key = 'abcdefg'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect(('127.0.0.1', 11097))
        sock.settimeout(60)
        filename = 'C:\\Users\\Administrator\\Desktop\\1.jar'
        sock.send('file(%s)' % filename)
        if sock.recv(1024) == '0':
            FILEINFO_SIZE = struct.calcsize('128sl')
            fhead = sock.recv(FILEINFO_SIZE)
            filename, filesize = struct.unpack('128sI', fhead)
            filename = filename.strip('\00')
            print filename,filesize
            fp = open('C:\\Users\\Administrator\\Desktop\\2.jar', 'wb')  # 新建文件，并且准备写入
            while filesize > 0:
                buf = sock.recv(4096)
                fp.write(buf)
                filesize -= len(buf)
            fp.close()
            sock.close()
            return True
        else:
            print 'fail'
            sock.close()
            return None
    except Exception as e:
        print "task_socket_dao Exception:",e

if __name__ == '__main__':
    send_msg()