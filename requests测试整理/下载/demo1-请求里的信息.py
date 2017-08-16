#!/usr/bin/env python
# coding=utf-8


import requests
import zipfile
import threading

def test_head():
    url = 'http://www.anzhi.com/dl_app.php?s=2762379'
    url2 = 'http://a.gdown.baidu.com/data/wisegame/98e1f98430ecabe4/jianlicai_41.apk?from=a1101'

    url3 = 'http://apk.hiapk.com/appdown/com.tencent.mobileqq'
    url4 = 'http://180.97.244.80/apk.r1.market.hiapk.com/data/upload/apkres/2017/3_15/9/com.tencent.mobileqq_095803.apk?wsiphost=local'
    headers = {'Range': 'Bytes=0-15000', 'Accept-Encoding': '*'}
    resp = requests.get(url3, stream=True, headers=headers)
    head = requests.head(url3)
    print head.headers
    print resp.headers
    print resp.url
    # with open('1.apk', 'wb') as f:
    #     for chunk in resp.iter_content(chunk_size=2048):
    #         if chunk:
    #             f.write(chunk)


# 下载器的类
class downloader:
    # 构造函数
    def __init__(self):
        # 要下载的数据连接
        self.url = 'http://apk.hiapk.com/appdown/com.tencent.mobileqq'
        # 要开的线程数
        self.num = 8
        # 存储文件的名字，从url最后面取
        self.name = '2.apk'
        # head方法去请求url
        r = requests.get(self.url,stream=True)
        # headers中取出数据的长度
        self.total = int(r.headers['Content-Length'])
        print 'total is %s' % (self.total)

    def get_range(self):
        ranges = []
        # 比如total是50,线程数是4个。offset就是12
        offset = int(self.total / self.num)
        for i in range(self.num):
            if i == self.num - 1:
                # 最后一个线程，不指定结束位置，取到最后
                ranges.append((i * offset, ''))
            else:
                # 没个线程取得区间
                ranges.append((i * offset, (i + 1) * offset))
        # range大概是[(0,12),(12,24),(25,36),(36,'')]
        return ranges

    def run(self):

        f = open(self.name, 'wb')
        for ran in self.get_range():
            # 拼出Range参数 获取分片数据
            r = requests.get(self.url, headers={'Range': 'Bytes=%s-%s' % ran, 'Accept-Encoding': '*'},stream=True)
            # seek到相应位置
            f.seek(ran[0])
            for chunk in r.iter_content(chunk_size=2048):
                if chunk:
                    f.write(chunk)
        f.close()

def test_write():
    t_lis = []
    with open('1.txt','w') as f:
        t = threading.Thread(target=f_write,args=(f,0,'11111111'))
        t.start()
        t_lis.append(t)
        t = threading.Thread(target=f_write, args=(f, 20, '22222222'))
        t.start()
        t_lis.append(t)
    for t in t_lis:
        t.join()



def f_write(start,content):
    f.seek(start)
    f.write(content)
    pass


if __name__ == '__main__':
    test_write()
