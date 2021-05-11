#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 14:26 
# @Author  : ana
# @File    : Collection27.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection27(scrapy.Spider):
    name = "Collection27"
    allowed_domains = ['balujun.cn']
    start_urls = ['http://www.balujun.cn/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='ca-container']/div/div")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 27
            item["museumName"] = "八路军太行纪念馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./div[1]/div[1]/div[2]/a/h3/text()").extract_first()).replace('[', '').replace(']', '')
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./div[1]/div[1]/div[2]/a/p/text()").extract_first()).replace('[', '').replace(']', '')
            item['collectionImageLink'] = 'http://www.balujun.cn' + str(
                li.xpath("./div[1]/div[1]/div[1]/@style").extract_first()).replace("background-image: url('",
                                                                                   '').replace("')", '')
            print(item)
            yield item
