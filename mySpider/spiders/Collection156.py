#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/5 0:47
# @Author  : 10711
# @File    : Collection156.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection156_supporting


class Collection156(scrapy.Spider):
    name = "Collection156"
    allowed_domains = ['baike.baidu.com']
    start_urls = Collection156_supporting.Collection156Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div/div[1]/table")
        print(len(li_list))
        for li in li_list[2:4]:
            item = CollectionItem()
            item["museumID"] = 156
            item["museumName"] = "广西民族博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./tr[1]/th").xpath('string(.)').extract_first())
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("./tr[2]/td[1]/div/div/a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./tr[3]/td[1]/div").xpath('string(.)').extract_first())
            print(item)
            yield(item)