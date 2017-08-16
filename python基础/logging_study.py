#!/usr/bin/env python
# coding=utf-8

import logging


def test_basic():
    logging.debug('this debug')
    logging.warning('this warning')
    logging.info('this info')
    logging.error('this error')
    '''
    WARNING:root:this warning
    ERROR:root:this error
    '''
    pass


def test_more():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='myapp.log',
                        filemode='w')

    logging.debug('This is debug message')
    logging.info('This is info message')
    logging.warning('This is warning message')
    # 此项不会在控制台输出，会输出在文件中


# 同时输出在控制台和文件当中
def test_console_and_file():
    # 第一步，创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Log等级总开关

    # 第二步，创建一个handler，用于写入日志文件
    logfile = 'logger.txt'
    fh = logging.FileHandler(logfile, mode='w')
    fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

    # 第三步，再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关

    # 第四步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 第五步，将logger添加到handler里面
    logger.addHandler(fh)
    logger.addHandler(ch)

    # 日志
    logger.debug('this is a logger debug message')
    logger.info('this is a logger info message')
    logger.warning('this is a logger warning message')
    logger.error('this is a logger error message')
    logger.critical('this is a logger critical message')
    pass


class Log:
    # 第一步，创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Log等级总开关
    # 第二步，创建一个handler，用于写入日志文件
    logfile = 'logger.txt'
    fh = logging.FileHandler(logfile, mode='a')
    fh.setLevel(logging.WARNING)  # 输出到file的log等级的开关
    # 第三步，再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)  # 输出到console的log等级的开关
    # 第四步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(thread)d %(filename)s : %(funcName)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # 第五步，将logger添加到handler里面
    logger.addHandler(fh)
    logger.addHandler(ch)

    @staticmethod
    def info(content):
        Log.logger.info(content)

    @staticmethod
    def warning(content):
        Log.logger.warning(content)

    @staticmethod
    def error(content):
        Log.logger.error(content)


# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关
# 第二步，创建一个handler，用于写入日志文件
logfile = 'logger.txt'
fh = logging.FileHandler(logfile, mode='a')
fh.setLevel(logging.WARNING)  # 输出到file的log等级的开关
# 第三步，再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)  # 输出到console的log等级的开关
# 第四步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(thread)d %(filename)s : %(funcName)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 第五步，将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)

if __name__ == '__main__':

    try:
        raise Exception('test')
    except Exception ,e:
        print e
        logger.error(e)
    # test_console_and_file()
    pass
