#!/usr/bin/env python
# coding=utf-8

import os
import re
import multiprocessing
import subprocess


def test_adb():
    space_pattern = re.compile('\s+')
    output = os.popen('adb devices')
    result = output.read().splitlines()
    if len(result) > 1:
        print len(result)
        for i in range(1, len(result)):
            if result[i]:
                print re.split(space_pattern, result[i])
            pass
        pass
    pass


def test_subprocess():
    p = subprocess.call('ping www.baidu.com',shell=True)#使用这个可以行
    print p

# "cmd.exe /k appium -a 127.0.0.1 -p "+phonePort+" -bp "+(Integer.parseInt(phonePort)+1)+" -U "+phoneCode+" >"+txtName
# appium -a 127.0.0.1 -p 10011 -bp 10012 -U RSOJAMO7OFKJW8WK

def start_server():
    os.system('appium -a 127.0.0.1 -p 10011 -bp 10012 -U RSOJAMO7OFKJW8WK')
def test_start_server():
    p = multiprocessing.Process(target=start_server)
    p.start()
    pass


if __name__ == '__main__':
    # p_in ,p_out = os.popen2('netstat -ano|findstr 3306','t',1)
    # print p_out.read()
    # PIPE = subprocess.PIPE
    # p = subprocess.Popen('netstat -ano|findstr 3306', shell=True, stdin=PIPE, stdout=PIPE,
    #                      stderr=PIPE)
    # print p.stdout.read()
    out = subprocess.check_output('C:\\Windows\\System32\\netstat -ano|findstr 3306',shell=True)
    print out
    print 'main end'
