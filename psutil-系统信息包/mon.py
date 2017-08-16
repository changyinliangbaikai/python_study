#coding:utf-8
from pymongo import*
import platform
from mongoengine import*
from pymongo import MongoClient
import psutil
import time


client = MongoClient("localhost", 27017)
db = client.Mseeage
#collection = db.Total
class GetMessage(Document):
    while True:
        vm = psutil.virtual_memory()
        memory = '{0:.2f} %'.format(vm.percent)#内存使用率
        total = '{0:.2f} M'.format(vm.total / 1024.0 / 1024.0)#总内存
        preocessor = platform.processor()#cpu信息
        Machine = platform.machine() #cup架构
        CPU_pecent = '{0:.2f} %'.format(psutil.cpu_percent(interval=1))#cpu使用率
        Disk = psutil.disk_partitions()  # 获取磁盘的完整信息
        # psutil.disk_io_counters(perdisk=True)磁盘IO信息
        disk = psutil.disk_usage('/')
        pf = platform.platform(aliased=True, terse=True)#操作系统
        #获取当前网卡流量数据
        net = psutil.net_io_counters()
        STsent = net.bytes_sent/1024.0
        STrcvd = net.bytes_recv/1024.0
        time.sleep(1)
        #获取结束时的网卡流量数据
        net = psutil.net_io_counters()
        bytes_EDsent = net.bytes_sent/1024.0
        bytes_EDrcvd = net.bytes_recv/1024.0
        #计算
        sent =bytes_EDsent - STsent
        rcvd =bytes_EDrcvd - STrcvd
        bytes_sent = '{0:.2f} kb/s'.format(sent/60)
        bytes_rcvd = '{0:.2f} kb/s'.format(rcvd/60)

        mydict = {"Platform": "%s" % pf,
                  "Machine": "%s" % Machine,
                  "Bytes_sent": "%s" % bytes_sent,
                  "Bytes_rcvd": "%s" % bytes_rcvd,
                  "Preocessor": "%s" % preocessor,
                  "Percent": "%s" % memory,
                  "memory_total": "%s" % total,
                  "cpu_pecent": "%s" % CPU_pecent,
                  "Disk": "%s" % Disk
                  }
        print memory,CPU_pecent,disk
        # 更新
        db.total.update({'_id': "Message"}, mydict, upsert=True)
        # 删除
        #db.collection.drop()




























