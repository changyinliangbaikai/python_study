#!/usr/bin/env python
# coding=utf-8
import socket
import time
import struct
import os

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
    f = open('socket_test.txt', 'wb')

    for i in range(1000000):
        f.write('for socket test, the line number is : ' + str(i) + '\n')

    f.close()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(50)
    e = 0
    try:
        sock.connect(('127.0.0.1', 8887))
        print 'connect...'
    except socket.timeout, e:
        print 'timeout', e
    except socket.error, e:
        print 'error', e
    except e:
        print 'any', e
    if not e:
        # while (1):
        # filename = raw_input('input your filename------->') # 输入文件名
        filename = 'socket_test.txt'
        FILEINFO_SIZE = struct.calcsize('128sI')  # 编码格式大小
        fhead = struct.pack('128sI', filename, os.stat(filename).st_size)  # 按照规则进行打包
        sock.send(fhead)  # 发送文件基本信息数据
        fp = open(filename, 'rb')
        fp2 = open('local_test.txt', 'wb')
        i = 0
        while 1:  # 发送文件
            filedata = fp.read(10240)
            if not filedata:
                break
            sock.sendall(filedata)
            fp2.write(filedata)
            print i
            i = i + 1
        print "sending over..."
        fp.close()
        fp2.close()
        sock.close()

if __name__ == '__main__':
    send2()