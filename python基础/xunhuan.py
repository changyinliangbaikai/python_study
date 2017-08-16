#!/usr/bin/env python
# coding=utf-8

for i in range(1, 10):
    for j in range(i):
        print "%s×%s=%s " % (i, (j + 1), (i * (j + 1))),
    print
    pass
a = 1
print type(a)
print isinstance(a, int)

for i in range(10):
    print i,
