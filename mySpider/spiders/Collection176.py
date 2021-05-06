#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 15:58
# @Author  : 10711
# @File    : Collection176.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection176_supporting


class Collection176(scrapy.Spider):
    name = "Collection176"
    allowed_domains = ['ynmuseum.org']
    start_urls = Collection176_supporting.Collection176Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div/div[3]/div[1]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 176
            item["museumName"] = "云南省博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a/div[2]").xpath('string(.)').extract_first())
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("./a/div[1]/img/@src").extract_first())
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
            response.xpath("//meta[@name='description']/@content").extract_first())
        print(item)
        yield(item)