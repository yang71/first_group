#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 22:35
# @Author  : 10711
# @File    : Collection166.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection166_supporting


class Collection166(scrapy.Spider):
    name = "Collection166"
    allowed_domains = ['jinshasitemuseum.com']
    start_urls = Collection166_supporting.Collection166Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='content']/div/div[2]/div/div/div[1]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 166
            item["museumName"] = "成都金沙遗址博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./p").xpath('string(.)').extract_first())
            item['collectionImageLink'] = str(
                li.xpath("./div/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./div/img/@name2").extract_first())
            print(item)
            yield(item)