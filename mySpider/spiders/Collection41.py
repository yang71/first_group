#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 20:18 
# @Author  : ana
# @File    : Collection41.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection41(scrapy.Spider):
    name = "Collection41"
    allowed_domains = ['jlmuseum.org']
    start_urls = ['http://www.jlmuseum.org/collection/',
                  'http://www.jlmuseum.org/collection/2.html',
                  'http://www.jlmuseum.org/collection/3.html', ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[2]/div[2]/div[3]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 41
            item["museumName"] = "吉林省博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./div[1]/a/@title").extract_first()).replace('[', '').replace(']', '')
            item['collectionImageLink'] = 'http://www.jlmuseum.org' + str(li.xpath(
                "./div[1]/a/img/@src").extract_first())
            url = "http://www.jlmuseum.org" + str(li.xpath("./div[1]/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[2]/div[2]/div[2]/div/p[2]").xpath('string(.)').extract_first()).replace('[',
                                                                                                                   '').replace(
            ']', '')
        print(item)
        yield item
