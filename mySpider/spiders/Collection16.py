#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 13:03 
# @Author  : ana
# @File    : Collection16.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection16_supporting


class Collection16(scrapy.Spider):
    name = "Collection16"
    allowed_domains = ['automuseum.org.cn']
    start_urls = Collection16_supporting.Collection16Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        item = CollectionItem()
        item["museumID"] = 16
        item["museumName"] = "北京汽车博物馆"
        item['collectionName'] = str(response.xpath(
            "//span/strong/text()").extract_first())
        item['collectionImageLink'] = 'http://www.automuseum.org.cn/' + str(response.xpath(
            "//div/img/@src").extract_first())
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath(
                "/html/body/div[2]/div[2]/div[2]").xpath(
                'string(.)').extract_first()).replace("','", '').replace(']', '').split('();')[1][
                                         len(item['collectionName']):]
        print(item)
        yield item
