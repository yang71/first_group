#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 16:41
# @Author  : 10711
# @File    : Collection171.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection171_supporting


class Collection171(scrapy.Spider):
    name = "Collection171"
    allowed_domains = ['zhudeguli.com']
    start_urls = Collection171_supporting.Collection171Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[2]/div/div[2]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 171
            item["museumName"] = "朱德同志故居纪念馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a/span").xpath('string(.)').extract_first())
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
            response.xpath("//*[@id='content']").xpath('string(.)').extract_first())
        print(item)
        yield(item)