#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 10:26 
# @Author  : ana
# @File    : Collection12.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection12(scrapy.Spider):
    name = "Collection12"
    allowed_domains = ['pgm.org.cn']
    start_urls = ['http://www.pgm.org.cn/pgm/jiaj/list.shtml',
                  'http://www.pgm.org.cn/pgm/jiaj/list_2.shtml', ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div/div[3]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 12
            item["museumName"] = "恭王府博物馆"
            url = 'http://www.pgm.org.cn' + str(li.xpath("./a/@href").extract_first())[5:]
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionName'] = response.xpath("/html/body/div/div[2]/div/div[2]/div[2]/text()").extract_first()
        item['collectionImageLink'] = 'http://www.pgm.org.cn/pgm/jiaj/201308/' + str(response.xpath(
            "//p/img/@src").extract_first())
        if item['collectionImageLink'] == 'http://www.pgm.org.cn/pgm/jiaj/201308/None':
            print("yes")
            item['collectionImageLink'] = 'http://www.pgm.org.cn/pgm/jiaj/201308/' + str(response.xpath(
                "//font/img/@src").extract_first())
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath('//*[@id="content"]').xpath('string(.)').extract_first()).replace('[',
                                                                                             '').replace(
            ']', '').split("文物简介：")[1]
        print(item)
        yield item
