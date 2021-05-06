#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 22:35
# @Author  : 10711
# @File    : Collection169.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection169_supporting


class Collection169(scrapy.Spider):
    name = "Collection169"
    allowed_domains = ['jc-museum.cn']
    start_urls = Collection169_supporting.Collection169Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[2]/div[3]/div[3]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 169
            item["museumName"] = "四川省建川博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a/p").xpath('string(.)').extract_first())
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
            response.xpath("//div[@class='box2 wf100'][1]").xpath('string(.)').extract_first()) + StrFilter.filter(
            response.xpath("//div[@class='box2 wf100'][2]").xpath('string(.)').extract_first()) + StrFilter.filter(
            response.xpath("//div[@class='box2 wf100'][3]").xpath('string(.)').extract_first())
        print(item)
        yield(item)