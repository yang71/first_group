#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 9:30 
# @Author  : ana
# @File    : Collection10.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection10(scrapy.Spider):
    name = "Collection10"
    allowed_domains = ['ciae.com.cn']
    start_urls = ['https://www.ciae.com.cn/collection/zh/collection.html', ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='ajax-list']/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 10
            item["museumName"] = "中国农业博物馆"
            item['collectionName'] = li.xpath("./a/@title").extract_first()
            item['collectionImageLink'] = 'www.ciae.com.cn' + li.xpath(
                "./a/div[1]/img/@src").extract_first()
            url = 'http://www.ciae.com.cn/' + str(li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(response.xpath(
            "/html/body/div[3]/div[1]/div/div/div/div/div[2]/text()").extract_first()).replace('[', '').replace(']', '')
        print(item)
        yield item
