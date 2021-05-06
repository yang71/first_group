#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/5 0:47
# @Author  : 10711
# @File    : Collection159.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection159_supporting


class Collection159(scrapy.Spider):
    name = "Collection159"
    allowed_domains = ['nanhaimuseum.org']
    start_urls = Collection159_supporting.Collection159Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='tiles']/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 159
            item["museumName"] = "中国（海南）南海博物馆"
            url = str(
                li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionName'] = StrFilter.filter(
            response.xpath("/html/body/div/div[2]/div[1]/div[2]/h1").xpath('string(.)').extract_first())
        item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
            response.xpath("/html/body/div/div[2]/div[1]/div[2]/div[4]/p[1]/span/img/@src").extract_first())
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div/div[2]/div[1]/div[2]/div[4]").xpath('string(.)').extract_first())
        print(item)
        yield(item)