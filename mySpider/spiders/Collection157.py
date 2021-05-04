#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/5 0:47
# @Author  : 10711
# @File    : Collection157.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection157_supporting


class Collection157(scrapy.Spider):
    name = "Collection157"
    allowed_domains = ['guilinmuseum.org.cn']
    start_urls = Collection157_supporting.Collection157Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='divList']/ul[2]/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 157
            item["museumName"] = "桂林博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a/p").xpath('string(.)').extract_first())
            item['collectionImageLink'] = str(
                li.xpath("./a/div/img/@src").extract_first())
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
            response.xpath("/html/body/div[4]/div/div/div/h3").xpath('string(.)').extract_first())
        print(item)
        yield(item)