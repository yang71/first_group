#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 18:51 
# @Author  : ana
# @File    : Collection39.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection39(scrapy.Spider):
    name = "Collection39"
    allowed_domains = ['dlnm.org.cn']
    start_urls = ['http://www.dlnm.org.cn/?_f=boutique&p=1',
                  'http://www.dlnm.org.cn/?_f=boutique&p=2',
                  'http://www.dlnm.org.cn/?_f=boutique&p=3',
                  'http://www.dlnm.org.cn/?_f=boutique&p=4', ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 39
            item["museumName"] = "大连自然博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a/@data-title").extract_first()).replace('[', '').replace(']', '')
            item['collectionImageLink'] = str(li.xpath(
                "./a/img/@src").extract_first())
            url = "http://www.dlnm.org.cn/" + str(li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div/div[3]/div[1]/div[2]/div[2]/div[2]").xpath(
                'string(.)').extract_first()).replace('[', '').replace(
            ']', '')
        print(item)
        yield item
