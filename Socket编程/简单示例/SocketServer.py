#!/usr/bin/env python
# coding=utf-8

import socket
import json
import demjson
import threading
import re


def thread2(conn, num):
    length_pattern = re.compile('length\((\d+)\)')
    all_recv = ""
    while True:
        try:
            buf = conn.recv(4096)
            if re.match(length_pattern, buf):
                print True
                conn.send('0')
                buf_length = int(re.findall(length_pattern, buf)[0])
                print buf_length
                while buf_length > 0:
                    buf = conn.recv(4096)
                    all_recv += buf
                    buf_length = buf_length - len(buf)
                conn.send('1')
                print len(all_recv)
                break
            else:
                print False,len(buf)
                conn.send('2')
                break
        except Exception as e:
            print e.message,num
    conn.close()


def start_thread(conn):
    all_recv = ""
    while True:
        buf = conn.recv(1024)
        if buf == 'length(1024)':
            buf = conn.recv(1024)
            all_recv += buf
        elif buf == 'length(0)':
            break
        else:
            pass
    print len(all_recv)
    conn.send('success')
    conn.close()

def test3(conn):
    print 'join test3'
    buf = conn.recv(1024)
    print buf
    conn.send('success')
    conn.close()


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
            connection.settimeout(5)
            num += 1
            print u'有socket接入',num
            t = threading.Thread(target=thread2, args=(connection, num,))
            t.start()
            #thread2(connection,num)
            #test3(connection)




        except Exception as e:
            print 'time out', e.message, num


if __name__ == '__main__':
    run_server()
    pass
