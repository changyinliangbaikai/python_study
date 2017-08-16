#!/usr/bin/env python
# coding=utf-8
from suds.client import Client
import time



if __name__ == '__main__':
    test = Client('http://localhost:7799/server?wsdl')
    start = time.time()
    for i in range(10):
        print test.service.checkSoftStatus('hello')
    end = time.time()
    print end-start