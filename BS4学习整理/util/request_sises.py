#!/usr/bin/env python
# coding=utf-8

import requests
import re
import random
'''一二三四五六七八九我你大小有的'''
__zhPattern = re.compile(u'[\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u6211\u4f60\u5927\u5c0f\u6709\u7684]+')

__user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]

def __get_iplist():
    iplist = []  ##初始化一个list用来存放我们获取到的IP
    html = requests.get("http://haoip.cc/tiqu.htm")  ##不解释咯
    iplistn = re.findall(r'r/>(.*?)<b', html.text,
                         re.S)  ##表示从html.text中获取所有r/><b中的内容，re.S的意思是包括匹配包括换行符，findall返回的是个list哦！
    for ip in iplistn:
        i = re.sub('\n', '', ip)  ##re.sub 是re模块替换的方法，这儿表示将\n替换为空
        iplist.append(i.strip())  ##添加到我们上面初始化的list里面
    return iplist

def get_html(url,proxy=None):
    UA = random.choice(__user_agent_list)  ##从self.user_agent_list中随机取出一个字符串
    headers = {'User-Agent': UA}  ##构造成一个完整的User-Agent （UA代表的是上面随机取出来的字符串哦）
    if proxy is None:
        try:
            resp = requests.get(url, headers=headers, timeout=3)
            if resp.status_code == 200:
                if len(requests.utils.get_encodings_from_content(resp.content)) > 0:
                    charset = requests.utils.get_encodings_from_content(resp.content)[0].lower()
                    resp.encoding = charset
                pageCode = resp.text
                match = __zhPattern.search(pageCode)
                if match:
                    pass
                else:
                    resp.encoding = 'gbk'
                    page_code_gbk = resp.text
                    resp.encoding = 'utf-8'
                    page_code_utf8 = resp.text
                    if __zhPattern.search(page_code_gbk):
                        pageCode = page_code_gbk
                    elif __zhPattern.search(page_code_utf8):
                        pageCode = page_code_utf8
                    else:
                        pass
                pageCode = re.sub(re.compile('<script.*?</script>', re.MULTILINE | re.S | re.I), "", pageCode)
                pageCode = re.sub(re.compile('<style.*?</style>', re.MULTILINE | re.S | re.I), "", pageCode)
                pageCode = re.sub(re.compile('<!--.*?-->', re.S), "", pageCode)
                return pageCode
            else:
                return None
        except:
            IP = ''.join(str(random.choice(__get_iplist())).strip())  ##下面有解释哦
            proxy = {'http': IP}
            return get_html(url, proxy, )  ##代理不为空的时候
    else:
        try:
            resp = requests.get(url, headers=headers, proxies=proxy, timeout=5)
            if resp.status_code == 200:
                if len(requests.utils.get_encodings_from_content(resp.content)) > 0:
                    charset = requests.utils.get_encodings_from_content(resp.content)[0].lower()
                    resp.encoding = charset
                pageCode = resp.text
                match = __zhPattern.search(pageCode)
                if match:
                    pass
                else:
                    resp.encoding = 'gbk'
                    page_code_gbk = resp.text
                    resp.encoding = 'utf-8'
                    page_code_utf8 = resp.text
                    if __zhPattern.search(page_code_gbk):
                        pageCode = page_code_gbk
                    elif __zhPattern.search(page_code_utf8):
                        pageCode = page_code_utf8
                    else:
                        pass
                pageCode = re.sub(re.compile('<script.*?</script>', re.MULTILINE | re.S | re.I), "", pageCode)
                pageCode = re.sub(re.compile('<style.*?</style>', re.MULTILINE | re.S | re.I), "", pageCode)
                pageCode = re.sub(re.compile('<!--.*?-->', re.S), "", pageCode)
                return pageCode
            else:
                return None
        except:
            return None

def get_real_url(url):
    UA = random.choice(__user_agent_list)  ##从self.user_agent_list中随机取出一个字符串
    headers = {'User-Agent': UA}  ##构造成一个完整的User-Agent （UA代表的是上面随机取出来的字符串哦）
    try:
        resp = requests.get(url, headers=headers, timeout=3,)
        if resp.status_code == 302:
            return get_real_url(resp.headers['Location'])
        elif resp.status_code == 200:
            return resp
        else:
            return None
    except:
        return None

def test():
    url = "http://short.58.com/zd_p/47d03533-5666-45be-827d-3630753763c6/?target=oc-16-xgk_ephv_36908940647448q-feykn&end=end"
    UA = random.choice(__user_agent_list)  ##从self.user_agent_list中随机取出一个字符串
    headers = {'User-Agent': UA}  ##构造成一个完整的User-Agent （UA代表的是上面随机取出来的字符串哦）
    resp = requests.get(url,headers=headers)
    print resp.status_code,resp.url
