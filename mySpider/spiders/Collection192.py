#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 11:17
# @Author  : 10711
# @File    : Collection192.py
# @software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection192_supporting


class Collection192(scrapy.Spider):
    name = "Collection192"
    allowed_domains = ['dtxsmuseum.com']
    start_urls = Collection192_supporting.Collection192Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='form1']/div[4]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 192
            item["museumName"] = "大唐西市博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a/span[2]").xpath('string(.)').extract_first())
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("./a/span[1]/img/@src").extract_first())
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
            response.xpath("//*[@id='form1']/div[4]/div[2]/div[4]").xpath('string(.)').extract_first())
        print(item)
        yield(item)