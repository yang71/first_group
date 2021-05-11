#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 19:51 
# @Author  : ana
# @File    : Collection46.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection46(scrapy.Spider):
    name = "Collection46"
    allowed_domains = ['hljmuseum.com']
    start_urls = ['http://www.hljmuseum.com/cpgz/cpxs/zgzb/', ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='erji-cent']/div[1]/ul/div")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 46
            item["museumName"] = "黑龙江省博物馆"
            item['collectionName'] = StrFilter.filter(li.xpath("./li/a/span/text()").extract_first()).replace('[',
                                                                                                              '').replace(
                ']', '')
            item['collectionImageLink'] = str(li.xpath("./li/a/img/@src").extract_first())
            url = "http://www.hljmuseum.com" + str(li.xpath("./li/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='erji-cent']/div[1]/div[2]/div[1]").xpath('string(.)').extract_first()).replace(
            '[', '').replace(
            ']', '')
        print(item)
        yield item
