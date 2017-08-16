#!/usr/bin/env python
# coding=utf-8
import time
from spider_queue_dao import SpiderQueue
from task_list_dao import TaskList
from do_keyword_spider import KeyWordSpider
import task_mysql_dao as task_dao
import datetime


class SpiderService():
    def __init__(self, spider_record, process_id):
        self.spider_queue = SpiderQueue(process_id)
        self.spider_record = spider_record
        self.process_id = process_id

    def run_spider(self):
        task_id = self.spider_record['task_id']
        if self.spider_record['type']==1:
            keyword_spider = KeyWordSpider(self.process_id)
            keyword_spider.do_start(self.spider_record)
        self.spider_queue.spider_complete(self.spider_record['_id'])
        all_spider_task = float(self.spider_queue.count_all_by_task_id(task_id))
        completed = float(self.spider_queue.count_complete_by_task_id(task_id))
        completion = float(completed/all_spider_task)
        task_dao.updata_completion(task_id,float("%.4f"%completion))
        if completion == 1.0:
            task_dao.update_status_and_endtime(task_id,4,datetime.datetime.now())
