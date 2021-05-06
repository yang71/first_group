#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 14:24
# @Author  : 10711
# @File    : Collection185.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection185_supporting


class Collection185(scrapy.Spider):
    name = "Collection185"
    allowed_domains = ['bmy.com.cn']
    start_urls = Collection185_supporting.Collection185Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[2]/div/div[1]/div[1]/div")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 185
            item["museumName"] = "秦始皇兵马俑博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./div[1]/p[1]").xpath('string(.)').extract_first())
            item['collectionImageLink'] = str(
                li.xpath("./div[2]/div[1]/div/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./div[1]/p[2]").xpath(
                    'string(.)').extract_first())
            print(item)
            yield(item)