#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 11:18 
# @Author  : ana
# @File    : Collection14.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection14(scrapy.Spider):
    name = "Collection14"
    allowed_domains = ['printingmuseum.cn']
    start_urls = ['http://www.printingmuseum.cn/Collection/List/JPDC#comehere',
                  'http://www.printingmuseum.cn/Collection/List/YSQY?pno=YSQY#comehere',
                  ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='ulImgList']/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 14
            item["museumName"] = "中国印刷博物馆"
            item['collectionImageLink'] = str(li.xpath("./a/img/@src").extract_first())
            item['collectionName'] = li.xpath("./a/@title").extract_first()
            url = 'http://www.printingmuseum.cn/' + str(li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = \
            StrFilter.filter(response.xpath("//*[@id='divBDetail']/div[2]").xpath('string(.)').extract_first()).replace(
                '[', '').replace(']', '')
        print(item)
        yield item
