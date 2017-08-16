#!/usr/bin/env python
# coding=utf-8
import socket
import json
import threading
import re
import struct
import os
# 提供外部接口，使得外部可以调用来上传爬取结果
def run_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 11097))
    sock.listen(0)
    while True:
        conn, address = sock.accept()
        try:
            conn.settimeout(60)
            t = threading.Thread(target=recv_large_str, args=(conn,))
            t.start()
        except Exception as e:
            print 'time out', e.message


def recv_large_str(conn):
    secret_key = "abcdefg"
    length_pattern = re.compile('length\((\d+)\)')
    file_pattern = re.compile('file\((.*?)\)')
    all_recv = ""
    try:
        buf = conn.recv(4096)
        if re.match(length_pattern, buf):
            print 'send result'
            conn.send('0')
            buf_length = int(re.findall(length_pattern, buf)[0])
            while buf_length > 0:
                buf = conn.recv(4096)
                all_recv += buf
                buf_length -= len(buf)
            conn.send('1')
            obj = json.loads(all_recv)
            if isinstance(obj, dict) and 'secret_key' in obj and obj['secret_key'] == secret_key:
                cmd_type = obj['cmd_type']
                pass
        elif re.match(file_pattern,buf):
            print 'send file'
            conn.send('0')
            filename = re.findall(file_pattern,buf)[0]
            fhead = struct.pack('128sI', filename, os.stat(filename).st_size)  # 按照规则进行打包
            conn.send(fhead)  # 发送文件基本信息数据
            f = open(filename, 'rb')
            conn.sendall(f.read())
            f.close()
            print 'send end'

        else:
            print False, len(buf)
            conn.send('2')
    except Exception as e:
        print e.message
    conn.close()


if __name__ == '__main__':
    run_server()