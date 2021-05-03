#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/3 23:24
# @Author  : 10711
# @File    : Collection194.py
# @software: PyCharm

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection194_supporting


class Collection194(scrapy.Spider):
    name = "Collection194"
    allowed_domains = ['tssbwg.com.cn']
    start_urls = Collection194_supporting.Collection194Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='layout']/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 194
            item["museumName"] = "天水市博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./table/tr[2]/td/span").xpath('string(.)').extract_first())
            item['collectionImageLink'] = str(
                li.xpath("./table/tr[1]/td/a/img/@src").extract_first())
            url = str(
                li.xpath("./table/tr[1]/td/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='Article']/div[5]").xpath('string(.)').extract_first())
        print(item)
        yield(item)