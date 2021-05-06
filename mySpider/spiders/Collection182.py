#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 15:22
# @Author  : 10711
# @File    : Collection182.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection182_supporting


class Collection182(scrapy.Spider):
    name = "Collection182"
    allowed_domains = ['dzshike.com']
    start_urls = Collection182_supporting.Collection182Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div[1]/div")
        print(len(li_list))
        for li in li_list[5:10]:
            item = CollectionItem()
            item["museumID"] = 182
            item["museumName"] = "大足石刻博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./div[1]/h2").xpath('string(.)').extract_first())
            item['collectionImageLink'] = str(
                li.xpath("//*[@class='imgdiv']/a/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("//*[@class='bei fr']").xpath('string(.)').extract_first())
            print(item)
            yield(item)