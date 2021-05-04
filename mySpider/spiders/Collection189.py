#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 13:46
# @Author  : 10711
# @File    : Collection189.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection189_supporting


class Collection189(scrapy.Spider):
    name = "Collection189"
    allowed_domains = ['bpmuseum.com']
    start_urls = Collection189_supporting.Collection189Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='brand-waterfall']/div")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 189
            item["museumName"] = "西安半坡博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./div/div/h3/a").xpath('string(.)').extract_first())
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("./div/a/img/@src").extract_first())
            url = str(
                li.xpath("./div/a/@href").extract_first())
            item['collectionIntroduction'] = item['collectionName']
            print(item)
            yield(item)