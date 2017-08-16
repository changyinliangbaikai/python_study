#!/usr/bin/env python
# coding=utf-8
import socket
import select

host = 'localhost'
port = 6666
addr = (host, port)

sock_lists = []


def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(addr)
    server.listen(1024)
    sock_lists.append(server)
    while True:
        print 1
        r,w,e = select.select(sock_lists,[],[])
        print 2
        for sc in r:
            if sc is server:
                try:
                    client, address = sc.accept()
                    print 'have new come',address
                    client.send('welcome')
                    sock_lists.append(client)
                except socket.error,e:
                    print 'e1:',e
            else:
                try:
                    buf = sc.recv(4096)
                    print sc,buf
                    for other in sock_lists:
                        if other!=server and other != sc:
                            other.send(buf)
                except Exception,e:
                    print 'e2:',e
                    sock_lists.remove(sc)


if __name__ == '__main__':
    run_server()
