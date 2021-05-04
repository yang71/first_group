#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 22:35
# @Author  : 10711
# @File    : Collection165.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection165_supporting


class Collection165(scrapy.Spider):
    name = "Collection165"
    allowed_domains = ['scmuseum.cn']
    start_urls = Collection165_supporting.Collection165Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='portfolio']/div")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 165
            item["museumName"] = "四川博物院"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a/div/span").xpath('string(.)').extract_first())
            item['collectionImageLink'] = str(
                li.xpath("./a/img/@src").extract_first())
            url = str(
                li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='MyContent']").xpath('string(.)').extract_first())
        print(item)
        #yield(item)