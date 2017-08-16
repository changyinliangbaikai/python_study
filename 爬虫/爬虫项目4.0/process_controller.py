#!/usr/bin/env python
# coding=utf-8

from process_manage_dao import ProcessList
from spider_queue_dao import SpiderQueue
from time import sleep
import multiprocessing
from spider_controller import SpiderController
import task_mysql_dao as task_dao
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class ProcessManage:
    __process_list = ProcessList()
    __num_retried = 0

    def run_task_process(self,task_process_number):
        for i in range(task_process_number):
            spider = SpiderController(i)
            p = multiprocessing.Process(target=spider.GoSpider)
            self.__process_list.process_regist(i)
            p.start()

    def run_manage_process(self):
        print 'manage process start running~'
        while True:
            try:
                records = task_dao.task_peek()#这边应该要做成取出此刻所有需要进行的任务，然后依次加入到任务量较少的进程中
                process_id = self.__process_list.find_process_id_by_least_task_number()
                if records and process_id!=None:
                    for record in records:
                        spider_queue = SpiderQueue(process_id)
                        task_id = record[0]
                        root_urls = record[1].split(",")
                        type = record[2]
                        depth = record[3]
                        keywords = record[4].replace(',','|')
                        for root_url in root_urls:
                            spider_queue.add_one(task_id,root_url,depth,keywords,type)
                        task_dao.update_status_and_endtime(task_id,2)
                    #del spider_queue
                self.__num_retried = 0
            except Exception as e:
                print "exception",e
                self.__num_retried += 1
            if self.__num_retried > 5:
                print u'mysql数据库连续5次出现异常，已终止进程'
                break

            sleep(1)




