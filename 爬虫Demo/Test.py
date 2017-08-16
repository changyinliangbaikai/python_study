#!/usr/bin/env python
# coding=utf-8


from mongodb_queue import MogoQueue
crawl_queue = MogoQueue('meinvxiezhenji', 'crawl_queue')
url = crawl_queue.pop()
title = crawl_queue.pop_title(url)
print title
path = title.replace('?', '')
print path