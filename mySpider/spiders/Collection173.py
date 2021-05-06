#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 16:41
# @Author  : 10711
# @File    : Collection173.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection173_supporting


class Collection173(scrapy.Spider):
    name = "Collection173"
    allowed_domains = ['gzmuseum.com']
    start_urls = Collection173_supporting.Collection173Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[2]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 173
            item["museumName"] = "贵州省博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a/div/p").xpath('string(.)').extract_first())
            item['collectionImageLink'] = str(
                li.xpath("./a/img/@src").extract_first())
            url = str(
                li.xpath("./a/@alt").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[1]/div[1]/div[2]/div[2]").xpath('string(.)').extract_first())
        print(item)
        yield(item)