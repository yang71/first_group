#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 23:30
# @Author  : 10711
# @File    : Collection160.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection160_supporting


class Collection160(scrapy.Spider):
    name = "Collection160"
    allowed_domains = ['baike.baidu.com']
    start_urls = Collection160_supporting.Collection160Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        item = CollectionItem()
        item["museumID"] = 160
        item["museumName"] = "自贡恐龙博物馆"
        item['collectionName'] = StrFilter.filter(
            response.xpath("/html/body/div[3]/div[2]/div/div[1]/dl/dd/h1").xpath('string(.)').extract_first())
        item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
            response.xpath("/html/body/div[3]/div[2]/div/div[2]/div[1]/a/@href").extract_first())
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div").xpath('string(.)').extract_first())
        print(item)
        yield(item)