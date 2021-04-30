#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/30 18:42 
# @Author  : ana
# @File    : Collection5.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection5(scrapy.Spider):
    name = "Collection5"
    allowed_domains = ['luxunmuseum.com.cn']
    start_urls = ['http://www.luxunmuseum.com.cn/guancangjingpin/',
                  'http://www.luxunmuseum.com.cn/guancangjingpin/list_19_2.htm',
                  'http://www.luxunmuseum.com.cn/guancangjingpin/list_19_3.htm', ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div[2]/div[1]/dl")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 5
            item["museumName"] = "北京鲁迅博物馆"
            item['collectionImageLink'] = 'http://www.luxunmuseum.com.cn' + li.xpath(
                "./dt/div[1]/a/img/@src").extract_first()
            item['collectionName'] = li.xpath("./dd/a/text()").extract_first()
            url = 'http://www.luxunmuseum.com.cn' + li.xpath("./dt/div[1]/a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        print(item)
        item['collectionIntroduction'] = StrFilter.filter(
            str(response.xpath("/html/body/div[3]/div[2]/div[2]/div[3]/div[2]/div[1]/text()").extract_first())).replace(
            "[", "").replace("]", "")
        print(item)
        yield item
