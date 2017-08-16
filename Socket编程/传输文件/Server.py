#!/usr/bin/env python
# coding=utf-8
import socket
import struct
import threading


def run_server():
    print 'start server'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 10001))
    sock.listen(1024)
    print 'bind 127.0.0.1:10001,listen 1024'
    num = 0
    while True:
        print u'进入循环'
        connection, address = sock.accept()
        try:
            connection.settimeout(60)





        except Exception as e:
            print 'time out', e.message, num


def send_file():
    pass


def test():
    FILEINFO_SIZE = struct.calcsize('128sl')
    print FILEINFO_SIZE
    pass


def function(newsock, address):
    FILEINFO_SIZE = struct.calcsize('128sI')
    '''定义文件信息（包含文件名和文件大小）大小。128s代表128个char[]（文件名），I代表一个integer or long（文件大小）'''
    while 1:
        try:
            fhead = newsock.recv(FILEINFO_SIZE)
            print 'fhead:',fhead, type(fhead)
            filename, filesize = struct.unpack('128sI', fhead)
            '''把接收到的数据库进行解包，按照打包规则128sI'''
            print "address is: ", address
            print filename, len(filename), type(filename)
            print filesize
            # filename = 'new_'+filename.strip('\00') # 命名新文件new_传送的文件
            filename = filename.strip('\00')
            fp = open(filename, 'wb')  # 新建文件，并且准备写入
            restsize = filesize
            print "recving..."
            while 1:
                if restsize > 102400:  # 如果剩余数据包大于1024，就去1024的数据包
                    filedata = newsock.recv(10240)
                else:
                    filedata = newsock.recv(restsize)
                    fp.write(filedata)
                    # break
                if not filedata:
                    break
                fp.write(filedata)
                restsize = restsize - len(filedata)  # 计算剩余数据包大小
                if restsize <= 0:
                    break
            fp.close()
            print "recv succeeded !!File named:", filename
        except Exception, e:
            print unicode(e).encode('gbk')
            print "the socket partner maybe closed"
            newsock.close()
            break


def run_server2():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建tcp连接
    sock.bind(('127.0.0.1', 8887))  # 定于端口和ip
    sock.listen(5)  # 监听
    while True:
        newsock, address = sock.accept()
        print "accept another connection"
        tmpThread = threading.Thread(target=function, args=(newsock, address))  # 如果接收到文件，创建线程
        tmpThread.start()  # 执行线程
    print 'end'


if __name__ == '__main__':
    # run_server()
    # test()
    run_server2()
