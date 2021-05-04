#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/5 0:47
# @Author  : 10711
# @File    : Collection154.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection154_supporting


class Collection154(scrapy.Spider):
    name = "Collection154"
    allowed_domains = ['msrmuseum.com']
    start_urls = Collection154_supporting.Collection154Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[1]/div[3]/div/div[1]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 154
            item["museumName"] = "广东海上丝绸之路博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a").xpath('string(.)').extract_first())
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("./a/span/img/@src").extract_first())
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
            response.xpath("/html/body/div[1]/div[3]/div/div[1]").xpath('string(.)').extract_first())
        print(item)
        yield(item)