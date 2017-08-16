项目结构：完整工程
项目功能：爬取指定url并查找指定关键词
传参：socket获取
已完成 ：多进程+多线程+mongodb+爬虫
缺点：结果保存，不同任务的队列无法区分，全部线程都参与到一个任务的爬取中  无法再加新的任务



param={
    'url':'http://www.targetUrl.com',
    'depth':num,
    'keywords':[key1,key2,key3]
}