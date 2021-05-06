#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 23:30
# @Author  : 10711
# @File    : Collection162.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection162_supporting


class Collection162(scrapy.Spider):
    name = "Collection162"
    allowed_domains = ['baike.baidu.com']
    start_urls = Collection162_supporting.Collection162Supporting.startUrl

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
            item["museumID"] = 162
            item["museumName"] = "成都武侯祠博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./td[2]/div/div/span").xpath('string(.)').extract_first())
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("./td[2]/div/div/a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./td[1]/div/text()").extract_first())
            print(item)
            yield(item)