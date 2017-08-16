#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup, element
import re


def test_open():
    soup = BeautifulSoup(open('1.jpg'), 'lxml')
    print soup.prettify()


def test_tag():
    soup = BeautifulSoup(open('1.html'), 'lxml')
    print soup.div


def test_children():
    soup = BeautifulSoup(open('1.html'), 'lxml')
    print soup.body.contents
    for child in soup.body.children:
        if child.string != "\n":
            print child


def test_find():
    soup = BeautifulSoup(open('1.html'), 'lxml')
    key = u'测试'
    results = soup.find_all(text=re.compile(key))
    for r in results:
        if len(r.find_parents('a')) > 0:
            print r, r.find_parents('a')[0]

    return


def test_find_keyword():
    soup = BeautifulSoup(open('1.html'), 'lxml')
    results = soup.find_all('a', href=(re.compile('^(/|\./).*?')))
    for r in results:
        print r.get('href')
    return


def test_find_and_children():
    soup = BeautifulSoup(open('1.html'), 'lxml')
    key = u'测试'
    for child in soup.body.children:
        if type(child) != element.NavigableString:
            print child.find_all('a', text=re.compile(key))
            # print child.string
            # print type(child),child


def test_bs4_parse():
    a = '<a href="0000">11111</a>'
    soup = BeautifulSoup(a, 'lxml')
    print soup.a.string
    print soup.a.get('href')


def test_find_re():
    soup = BeautifulSoup(open('test2.html'), 'lxml')
    results = soup.find_all(text=re.compile(u'特朗普'))
    result_list = []
    for r in results:
        result_list.append(r.find_parent('div').text)
    index = 0
    max_length = 0
    for i in range(len(result_list)):
        print len(result_list[i])
        if len(result_list[i]) > max_length:
            max_length = len(result_list[i])
            index = i
    print index,':',len(result_list[index])
    print result_list[index]



if __name__ == '__main__':
    test_find_re()
