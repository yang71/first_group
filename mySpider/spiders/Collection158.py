#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/5 0:47
# @Author  : 10711
# @File    : Collection158.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection158_supporting


class Collection158(scrapy.Spider):
    name = "Collection158"
    allowed_domains = ['baike.baidu.com']
    start_urls = Collection158_supporting.Collection158Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div/div[1]/table/tr")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 158
            item["museumName"] = "海南省博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./td[1]/div[1]/b").xpath('string(.)').extract_first()).replace('：', '')
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("./td[2]/div/div/a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./td[1]/div[3]").xpath('string(.)').extract_first())
            print(item)
            yield(item)