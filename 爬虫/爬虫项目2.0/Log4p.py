#!/usr/bin/env python
# coding=utf-8

#打印日志方法
import codecs
import datetime
import os

logDir = "./log"
logFile = logDir +"/"+"log,log"
def logINFO(string):
    if not os.path.exists(logDir):
        os.makedirs(logDir)
    if os.path.exists(logFile) and os.path.getsize(logFile)>1024**3:
        os.rename(logFile,logFile+"."+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    string = str(string).decode('utf-8')
    f = codecs.open('log/log.log','a','utf-8')
    b = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print "[%s INFO : %s]\n"%(b,string)
    f.write("[%s INFO : %s]\n"%(b,string))
    f.close()

def logERROR(string):
    if not os.path.exists(logDir):
        os.makedirs(logDir)
    if os.path.exists(logFile) and os.path.getsize(logFile)>1024**3:
        os.rename(logFile,logFile+"."+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    string = str(string).decode('utf-8')
    f = codecs.open('log/log.log','a','utf-8')
    b = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f.write("[%s ERROR : %s]\n"%(b,string))
    f.close()
def logWARN(string):
    if not os.path.exists(logDir):
        os.makedirs(logDir)
    if os.path.exists(logFile) and os.path.getsize(logFile)>1024**3:
        os.rename(logFile,logFile+"."+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    string = str(string).decode('utf-8')
    f = codecs.open('log/log.log','a','utf-8')
    b = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f.write("[%s WARN : %s]\n"%(b,string))
    f.close()
def logConsole(string):
    string = str(string).decode('utf-8')
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print "[%s CONSOLE : %s]"%(time,string)
