#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 15:35
# @Author  : 10711
# @File    : Collection181.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection181_supporting


class Collection181(scrapy.Spider):
    name = "Collection181"
    allowed_domains = ['baike.baidu.com']
    start_urls = Collection181_supporting.Collection181Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div/div[1]/table/tr")
        print(len(li_list))
        for li in li_list[2:]:
            item = CollectionItem()
            item["museumID"] = 181
            item["museumName"] = "重庆三峡移民纪念馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./td[1]").xpath('string(.)').extract_first())
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("./td[3]/div/div/a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./td[2]").xpath('string(.)').extract_first())
            print(item)
            #yield(item)