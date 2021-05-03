#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/3 22:49
# @Author  : 10711
# @File    : Collection196.py
# @software: PyCharm

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection196_supporting


class Collection196(scrapy.Spider):
    name = "Collection196"
    allowed_domains = ['plsbwg.com']
    start_urls = Collection196_supporting.Collection196Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div[3]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 196
            item["museumName"] = "平凉市博物馆"
            item['collectionImageLink'] = str(li.xpath(
                "./a/div/img/@src").extract_first())
            url = str(li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionName'] = StrFilter.filter(
            response.xpath("/html/body/div[3]/div/div[1]/div/div").xpath('string(.)').extract_first())
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[3]/div/div[1]/div/ul").xpath('string(.)').extract_first())
        print(item)
        yield(item)