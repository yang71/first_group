#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/5 0:47
# @Author  : 10711
# @File    : Collection152.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection152_supporting


class Collection152(scrapy.Spider):
    name = "Collection152"
    allowed_domains = ['zgkjbwg.com']
    start_urls = Collection152_supporting.Collection152Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div/div[3]/div[8]/div[3]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 152
            item["museumName"] = "广东中国客家博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a/p").xpath('string(.)').extract_first())
            item['collectionImageLink'] = StrFilter.getDoamin(response) + '/' +str(
                li.xpath("./a/img/@src").extract_first())
            item['collectionIntroduction'] = "暂无"
            print(item)
            #yield(item)