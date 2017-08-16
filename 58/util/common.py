#!/usr/bin/env python
# coding=utf-8
from bs4 import BeautifulSoup
import request_sises as request





# if __name__ == '__main__':
#     url = "http://short.58.com/zd_p/47d03533-5666-45be-827d-3630753763c6/?target=oc-16-xgk_ephv_36908940647448q-feykn&end=end"
#     url2 = 'http://jing.58.com/adJump?adType=3&target=pZwY0jCfsvOJsWN3shPfUiqCugGds1c3PW01PWTLrjTQnjT1XaO1pZwVUakQn1N1PWm3PjbQrHEdnW0QPW9zrHDQrHNvnH9_PjbdnWDYnWb_sau_UvIMpyOxIgP-0-qGujYhuA-107qWmgw-5HnLnjnQFhwG0LKxUAqWmykqnH0zFhP_pyR8I7qd0vRzgv-b5iu-UMwGIZ-GujYzrjmLn1mkP19knHTknzud0vRzpyEqPjEYP1EdPWcLnWbznWbhpyd-pHYhuyOYpgwOIZ-kuHYkFhR8IA-YXRqWmgw-5iu-UMwGIZ-xUAqWmykqFhwG0LKxIA-VuHYQPj9YnHcYPHD1rHmQFMKf0v-Ypyq85HDzPiuWUA-Wpv-b5HELujT1PHn1sHNvPWmVPjRBuiY3nWIbsHnvn1TLPHnLPWPWPBukmgF6UHYh0AQ6IAuf0hYqsHDhUA-1IZGb5yQG0LwluaukmyI-gLwO0ANqnikQnk&end=end'
#     url3 = 'http://nj.58.com/hezu/28673607801003x.shtml?adtype=3'
#     page_code = open("../1.html").read()
#     soup = BeautifulSoup(page_code,'lxml')
#     for i in soup.find_all("div",class_="des"):
#         resp = request.get_real_url(i.a.get('href'))
#         if resp is not None:
#             item_url = resp.url
#             item_desc = i.a.string.strip()
#             print item_desc,item_url
#     print len(soup.find_all("div",class_="des"))
#
#
#
#
#
#     pass