#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 14:13
# @Author  : 10711
# @File    : Collection188.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection188_supporting


class Collection188(scrapy.Spider):
    name = "Collection188"
    allowed_domains = ['beilin-museum.com']
    start_urls = Collection188_supporting.Collection188Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[5]/div/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 188
            item["museumName"] = "西安碑林博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a/p").xpath('string(.)').extract_first())
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("./a/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[5]/div/div/div[2]").xpath('string(.)').extract_first())
        print(item)
        yield(item)