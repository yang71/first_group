#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/3 23:42
# @Author  : 10711
# @File    : Collection193.py
# @software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection193_supporting


class Collection193(scrapy.Spider):
    name = "Collection193"
    allowed_domains = ['gansumuseum.com']
    start_urls = Collection193_supporting.Collection193Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 193
            item["museumName"] = "甘肃省博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./div/div/div[1]").xpath('string(.)').extract_first())
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("./div/a/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./div/div/div[2]/a[2]/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div/div[2]/div[1]/div[2]/div[2]/div/div/div/div[3]").xpath('string(.)').extract_first())
        print(item)
        yield(item)