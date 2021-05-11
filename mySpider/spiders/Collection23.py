#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 15:43 
# @Author  : ana
# @File    : Collection23.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection23_supporting


class Collection23(scrapy.Spider):
    name = "Collection23"
    allowed_domains = ['xbpjng.cn']
    start_urls = Collection23_supporting.Collection23Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='main']/div[3]/div[1]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 23
            item["museumName"] = "西柏坡纪念馆"
            item['collectionName'] = StrFilter.filter(li.xpath("./a/h2/text()").extract_first()).replace('[',
                                                                                                         '').replace(
                ']', '')
            item['collectionImageLink'] = li.xpath("./a/img/@src").extract_first()
            item['collectionIntroduction'] = "暂无介绍"
            print(item)
            yield item
