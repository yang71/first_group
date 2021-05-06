#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 14:36
# @Author  : 10711
# @File    : Collection184.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection184_supporting


class Collection184(scrapy.Spider):
    name = "Collection184"
    allowed_domains = ['sxhm.com']
    start_urls = Collection184_supporting.Collection184Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 184
            item["museumName"] = "陕西历史博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a/span").xpath('string(.)').extract_first())
            item['collectionImageLink'] = StrFilter.getDoamin(response) + '/' + str(
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
            response.xpath("/html/body/div[3]/div[2]/div[2]/div[3]").xpath('string(.)').extract_first())
        print(item)
        yield(item)