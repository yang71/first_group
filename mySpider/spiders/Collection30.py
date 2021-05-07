#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 16:51 
# @Author  : ana
# @File    : Collection30.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection30_supporting


class Collection30(scrapy.Spider):
    name = "Collection30"
    allowed_domains = ['linfenmuseum.com']
    start_urls = Collection30_supporting.Collection30Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='weekly']/div/div/div[2]/div/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 30
            item["museumName"] = "临汾市博物馆"
            url = "http://www.linfenmuseum.com/" + str(li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionName'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[2]/text()").extract_first()
        item['collectionImageLink'] = str(response.xpath(
            "//*[@id='gallery']/a/@href").extract_first())
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[2]/div[2]/div[2]/div[5]").xpath('string(.)').extract_first()).replace('[',
                                                                                                                 '').replace(
            ']', '')
        print(item)
        yield item
