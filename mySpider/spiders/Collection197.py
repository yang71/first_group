#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/3 21:27
# @Author  : 10711
# @File    : Collection197.py
# @software: PyCharm
from urllib.parse import urlparse

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection197_supporting


class Collection197(scrapy.Spider):
    name = "Collection197"
    allowed_domains = ['nxgybwg.com']
    start_urls = Collection197_supporting.Collection197Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='body_wrap']/div/div[2]/div[2]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 197
            item["museumName"] = "固原博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./p/a").xpath('string(.)').extract_first())
            item['collectionImageLink'] = str(li.xpath(
                "./div/a/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + str(li.xpath("./div/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='body_wrap']/div/div[2]/div[2]/div/div[2]/div").xpath('string(.)').extract_first())
        print(item)
        yield(item)