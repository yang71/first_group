#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/3 20:45
# @Author  : 10711
# @File    : Collection198.py
# @software: PyCharm

from ..items import *
from ..str_filter import *


class Collection198(scrapy.Spider):
    name = "Collection198"
    allowed_domains = ['nxbwg.com']
    start_urls = ['http://www.nxbwg.com/c/jpww.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='pb-box']/div")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 198
            item["museumName"] = "宁夏回族自治区博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./h3/a").xpath('string(.)').extract_first())
            item['collectionImageLink'] = str(li.xpath(
                "./a/div/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + str(li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='content-container']/div/main/div/div[2]/div[2]").xpath('string(.)').extract_first())
        print(item)
        yield(item)