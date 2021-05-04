#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/3 23:12
# @Author  : 10711
# @File    : CollectionXXX.py
# @software: PyCharm

from ..items import *
from ..str_filter import *
from ..auxiliary_files import CollectionXXX_supporting


class CollectionXXX(scrapy.Spider):
    name = "CollectionXXX"
    allowed_domains = ['']
    start_urls = CollectionXXX_supporting.CollectionXXXSupporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = XXX
            item["museumName"] = ""
            item['collectionName'] = StrFilter.filter(
                li.xpath("").xpath('string(.)').extract_first())
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("").extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("").xpath('string(.)').extract_first())
        print(item)
        #yield(item)