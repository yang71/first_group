#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 18:43 
# @Author  : ana
# @File    : Collection38.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection38_supporting


class Collection38(scrapy.Spider):
    name = "Collection38"
    allowed_domains = ['dlmodernmuseum.com']
    start_urls = Collection38_supporting.Collection38Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[6]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 38
            item["museumName"] = "大连博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a/@title").extract_first()).replace('[', '').replace(']', '')
            item['collectionImageLink'] = 'https://www.dlmodernmuseum.com/' + str(li.xpath(
                "./a/div[1]/img/@src").extract_first())
            url = str(li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[6]").xpath('string(.)').extract_first()).replace('[', '').replace(
            ']', '')
        print(item)
        yield item
