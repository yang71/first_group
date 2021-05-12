#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 21:33
# @Author  : 10711
# @File    : Collection174.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection174_supporting


class Collection174(scrapy.Spider):
    name = "Collection174"
    allowed_domains = ['gzsmzmuseum.cn']
    start_urls = Collection174_supporting.Collection174Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@class='proli clearfix']/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 174
            item["museumName"] = "贵州省民族博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a/div[2]/h3").xpath('string(.)').extract_first())
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("./a/div[1]/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + '/' +str(
                li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//*[contains(@class, 'MsoNormal')]").xpath('string(.)').extract_first())
        if(item['collectionIntroduction'] == 'None'):
            item['collectionIntroduction'] = '暂无'
        print(item)
        yield(item)