#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 14:55 
# @Author  : ana
# @File    : Collection20.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection20_supporting


class Collection20(scrapy.Spider):
    name = "Collection20"
    allowed_domains = ['mzhoudeng.com']
    start_urls = Collection20_supporting.Collection20Supporting.startUrl
    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div/div[1]/div[2]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 20
            item["museumName"] = "周恩来邓颖超纪念馆"
            item['collectionName'] = li.xpath("./a/p/text()").extract_first()
            item['collectionImageLink'] = 'http://www.mzhoudeng.com/' + str(li.xpath(
                "./a/img/@src").extract_first())
            url = "http://www.mzhoudeng.com/" + str(li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[3]/div/div[1]/div[2]/div[2]/div[3]").xpath(
                'string(.)').extract_first()).replace('[', '').replace(']', '')
        print(item)
        yield item
