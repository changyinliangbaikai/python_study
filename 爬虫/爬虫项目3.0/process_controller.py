#!/usr/bin/env python
# coding=utf-8

from process_manage_dao import ProcessList
from spider_queue_dao import SpiderQueue
from time import sleep
import multiprocessing
from spider_controller import SpiderController
import task_mysql_dao as task_dao


class ProcessManage:
    __process_list = ProcessList()

    def run_task_process(self,task_process_number):
        for i in range(task_process_number):
            spider = SpiderController(i)
            p = multiprocessing.Process(target=spider.GoSpider)
            self.__process_list.process_regist(i)
            p.start()

    def run_manage_process(self):
        print 'manage process start running~'
        while True:
            record = task_dao.task_peek()
            process_id = self.__process_list.find_process_id_by_least_task_number()
            if record and process_id!=None:
                spider_queue = SpiderQueue(process_id)
                task_id = record[0]
                root_url = record[1]
                type = record[2]
                depth = record[3]
                param = record[4].split(',')
                spider_queue.add_one(task_id,root_url,depth,param,type)
                task_dao.update_status_and_endtime(task_id,2)
                #del spider_queue
            sleep(1)




