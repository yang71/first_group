#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/5 0:47
# @Author  : 10711
# @File    : Collection151.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection151_supporting


class Collection151(scrapy.Spider):
    name = "Collection151"
    allowed_domains = ['gzam.com.cn']
    start_urls = Collection151_supporting.Collection151Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='wrapper']/div[1]/div[1]/section/section/div[2]/article/dl/dd")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 151
            item["museumName"] = "广州艺术博物院"
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("./a/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionName'] = StrFilter.filter(
            response.xpath("//*[@id='wrapper']/div[1]/div[1]/section/section/div[2]/article/div[2]/p[1]").xpath('string(.)').extract_first())
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='wrapper']/div[1]/div[1]/section/section/div[2]/article/div[2]").xpath('string(.)').extract_first())
        if item['collectionName'] != 'None' and item['collectionName'] != '' and len(item['collectionName']) < 50:
            print(item)
            yield(item)