#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 16:36 
# @Author  : ana
# @File    : Collection29.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection29(scrapy.Spider):
    name = "Collection29"
    allowed_domains = ['sxgm.org']
    start_urls = ['http://www.sxgm.org/home/picnews/index/c_id/106/lanmu/61.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[5]/div/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 29
            item["museumName"] = "山西地质博物馆"
            item['collectionName'] = StrFilter.filter(li.xpath(".").xpath('string(.)').extract_first()).replace('[',
                                                                                                                '').replace(
                ']', '')
            item['collectionImageLink'] = "http://www.sxgm.org" + str(
                li.xpath(".//img/@src").extract_first())
            url = "http://www.sxgm.org" + str(li.xpath(".//@href").extract_first())
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[5]/div/div[2]/div[4]/table").xpath(
                'string(.)').extract_first()).replace('[', '').replace(
            ']', '')
        print(item)
        yield item
