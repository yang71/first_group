#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 22:35
# @Author  : 10711
# @File    : Collection168.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection168_supporting


class Collection168(scrapy.Spider):
    name = "Collection168"
    allowed_domains = ['cdmuseum.com']
    start_urls = Collection168_supporting.Collection168Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 168
            item["museumName"] = "成都博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a/p").xpath('string(.)').extract_first())
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("./a/div/img/@src").extract_first())
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
            response.xpath("/html/body/div[3]/div[1]/div[2]/div/div[2]/div").xpath('string(.)').extract_first())
        print(item)
        yield(item)