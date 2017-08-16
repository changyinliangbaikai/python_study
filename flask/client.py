#!/usr/bin/env python
# coding=utf-8
import requests
import time

start = time.time()
for i in range(10):
    req = requests.get('http://127.0.0.1:5000/test')
    print req.text
end = time.time()
print end - start