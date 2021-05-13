#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/13 18:04
# @Author  : 10711
# @File    : start_All.py
# @Software: PyCharm

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

@defer.inlineCallbacks
def crawl():
    spider_list = runner.spider_loader.list()
    for name in spider_list:  # 遍历所有爬虫
        if name.startswith('Museum1'):
            yield runner.crawl(name)
    reactor.stop()

if __name__ == '__main__':
    start = time.time()
    crawl()
    reactor.run()  # the script will block here until the last crawl call is finished
    end = time.time()
    print("runningtime:%.2f秒" % (end - start))