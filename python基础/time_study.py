#!/usr/bin/env python
# coding=utf-8
'''
Python格式化日期时间的函数为datetime.datetime.strftime()；由字符串转为日期型的函数为：datetime.datetime.strptime()，两个函数都涉及日期时间的格式化字符串，列举如下：

%a Abbreviated weekday name
%A Full weekday name
%b Abbreviated month name
%B Full month name
%c Date and time representation appropriate for locale
%d Day of month as decimal number (01 - 31)
%H Hour in 24-hour format (00 - 23)
%I Hour in 12-hour format (01 - 12)
%j Day of year as decimal number (001 - 366)
%m Month as decimal number (01 - 12)
%M Minute as decimal number (00 - 59)
%p Current locale's A.M./P.M. indicator for 12-hour clock
%S Second as decimal number (00 - 59)
%U Week of year as decimal number, with Sunday as first day of week (00 - 51)
%w Weekday as decimal number (0 - 6; Sunday is 0)
%W Week of year as decimal number, with Monday as first day of week (00 - 51)
%x Date representation for current locale
%X Time representation for current locale
%y Year without century, as decimal number (00 - 99)
%Y Year with century, as decimal number
%z, %Z Time-zone name or abbreviation; no characters if time zone is unknown
%% Percent sign

举一个例子：

ebay中时间格式为‘Sep-21-09 16:34’

则通过下面代码将这个字符串转换成datetime

c = datetime.datetime.strptime('Sep-21-09 16:34','%b-%d-%y %H:%M');
c
datetime.datetime(2009, 9, 21, 16, 34)

又如：datetime转换成字符串

datetime.datetime.now().strftime('%b-%d-%y %H:%M:%S');
'Sep-22-09 16:48:08'
'''
import datetime
print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),type(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print type(datetime.datetime.now())