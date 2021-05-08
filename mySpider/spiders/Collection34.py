#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/8 8:47 
# @Author  : ana
# @File    : Collection34.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection34_supporting


class Collection34(scrapy.Spider):
    name = "Collection34"
    allowed_domains = ['lnmuseum.com.cn']
    start_urls = Collection34_supporting.Collection34Supporting.startUrl
    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        }
    }

    def parse(self, response, **kwargs):
        tr_list = response.xpath("//td[@class='wz1']/table[1]//tr[position()<4]")
        print(len(tr_list))
        for tr in tr_list:
            td_list = tr.xpath("./td")
            for td in td_list:
                item = CollectionItem()
                item["museumID"] = 34
                item["museumName"] = "辽宁省博物馆"
                item['collectionName'] = StrFilter.filter_2(td.xpath("./table[2]").xpath('string(.)').extract_first())
                item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                    td.xpath("./table[1]//img/@src").extract_first())[2:]
                item['collectionIntroduction'] = None
                if item['collectionName'] != 'None':
                    print(item)
                    yield item
