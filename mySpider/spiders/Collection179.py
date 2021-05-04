#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 15:53
# @Author  : 10711
# @File    : Collection179.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection179_supporting


class Collection179(scrapy.Spider):
    name = "Collection179"
    allowed_domains = ['hongyan.info']
    start_urls = Collection179_supporting.Collection179Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[8]/div[2]/div/div[3]/div")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 179
            item["museumName"] = "重庆红岩革命历史博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./h2/a").xpath('string(.)').extract_first())
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("./a/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./h2/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[7]/div[3]/div[3]/div[2]").xpath('string(.)').extract_first())
        print(item)
        #yield(item)