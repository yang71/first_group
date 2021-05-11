#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 16:18 
# @Author  : ana
# @File    : Collection26.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection26_supporting


class Collection26(scrapy.Spider):
    name = "Collection26"
    allowed_domains = ['coalmus.org.cn']
    start_urls = Collection26_supporting.Collection26Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='wrap']/div[2]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 26
            item["museumName"] = "中国煤炭博物馆"
            item['collectionName'] = str(li.xpath("./div/a/@title").extract_first())
            item['collectionImageLink'] = str(li.xpath(
                "./div/a/img/@src").extract_first())
            url = li.xpath("./div/a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='wrap']/div[2]/div[5]/div[3]").xpath('string(.)').extract_first()).replace('[',
                                                                                                               '').replace(
            ']', '')
        print(item)
        yield item
