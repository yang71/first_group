#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/3 16:55
# @Author  : 10711
# @File    : Collection199.py
# @software: PyCharm

from ..items import *
from ..str_filter import *


class Collection199(scrapy.Spider):
    name = "Collection199"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E9%9D%92%E6%B5%B7%E7%9C%81%E5%8D%9A%E7%89%A9%E9%A6%86/1627225?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div/div[1]/table/tr")
        print(len(li_list))
        for li in li_list[1:]:
            item = CollectionItem()
            item["museumID"] = 199
            item["museumName"] = "青海省博物馆"
            item['collectionName'] = li.xpath("./td[1]").xpath('string(.)').extract_first()
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(li.xpath(
                "./td[3]/div/div/a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./td[2]").xpath('string(.)').extract_first())
            print(item)
            yield(item)


