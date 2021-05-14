#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/13 18:04
# @Author  : 10711
# @File    : start.py
# @Software: PyCharm
import sys

from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor, defer
import time
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

'''
以下是多个爬虫顺序执行的命令（比较慢）
'''
configure_logging()
# 加入setting配置文件，否则配置无法生效
# get_project_settings()获取的是setting.py的配置
runner = CrawlerRunner(get_project_settings())

#忽略爬虫列表
ignore = ['Collection0', 'Exhibition0']

@defer.inlineCallbacks
def crawl(key):
    spider_list = runner.spider_loader.list()
    for name in spider_list:  # 遍历所有爬虫
        if name.startswith(key):
            if (name not in ignore):
                yield runner.crawl(name)
    reactor.stop()

if __name__ == '__main__':
    start = time.time()
    if len(sys.argv) != 2:
        print("参数个数有误！")
        sys.exit()
    if sys.argv[1] == 'Museum':
        crawl('Museum')
    elif sys.argv[1] == 'Collection':
        crawl('Collection')
    elif sys.argv[1] == 'Exhibition':
        crawl('Exhibition')
    elif sys.argv[1] == 'All':
        crawl('')
    else:
        print("输入参数有误！")
        sys.exit()
    reactor.run()
    end = time.time()
    print(sys.argv[1] + "爬取完成，运行时间:%.2f秒" % (end - start))