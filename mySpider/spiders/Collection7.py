#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/30 20:04 
# @Author  : ana
# @File    : Collection7.py
# @Software: PyCharm

from ..auxiliary_files import Collection7_supporting
from ..items import *


class Collection7(scrapy.Spider):
    name = "Collection7"
    allowed_domains = ['bmnh.org.cn']
    start_urls = Collection7_supporting.Collection7Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        list_li = response.xpath("//div[@class='col-sm-4']")
        for i in list_li:
            item = CollectionItem()
            item["museumID"] = 7
            item["museumName"] = "北京自然博物馆"
            item['collectionName'] = i.xpath("./div[@class='thumbnail']/a/img/@alt").extract_first()
            item['collectionImageLink'] = 'www.bmnh.org.cn' + i.xpath(
                "./div[@class='thumbnail']/a/img/@src").extract_first()
            item['collectionIntroduction'] = "暂无介绍"
            print(item)
            yield item
