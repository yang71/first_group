#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 19:31 
# @Author  : ana
# @File    : Collection48.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection48(scrapy.Spider):
    name = "Collection48"
    allowed_domains = ['hljsmzbwg.com']
    start_urls = ['http://www.hljsmzbwg.com/cp.html',
                  'http://www.hljsmzbwg.com/cp_2.html',
                  'http://www.hljsmzbwg.com/cp_3.html',
                  'http://www.hljsmzbwg.com/cp_4.html',
                  'http://www.hljsmzbwg.com/cp_5.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("///html/body/div[3]/div[2]/div[2]/div/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 48
            item["museumName"] = "黑龙江省民族博物馆"
            item['collectionName'] = StrFilter.filter(li.xpath("./a/p/text()").extract_first()).replace('[',
                                                                                                        '').replace(
                ']', '')
            item['collectionImageLink'] = 'https:' + str(li.xpath(
                "./a/img/@src").extract_first())
            url = "http://www.hljsmzbwg.com/" + str(li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[3]/div[2]/div[2]/section").xpath('string(.)').extract_first()).replace('[',
                                                                                                                  '').replace(
            ']', '')
        print(item)
        yield item
