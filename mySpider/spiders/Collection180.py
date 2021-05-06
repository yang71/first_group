#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 15:44
# @Author  : 10711
# @File    : Collection180.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection180_supporting


class Collection180(scrapy.Spider):
    name = "Collection180"
    allowed_domains = ['cmnh.org.cn']
    start_urls = Collection180_supporting.Collection180Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[2]/div[3]/div/div[2]/div[1]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 180
            item["museumName"] = "重庆自然博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./div/div[2]/a/h6").xpath('string(.)').extract_first())
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("./p/a/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./p/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[2]/div[3]/div/div[2]").xpath('string(.)').extract_first())
        print(item)
        yield(item)