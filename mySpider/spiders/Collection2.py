#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 17:36 
# @Author  : ana
# @File    : Collection2.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection2(scrapy.Spider):
    name = "Collection2"
    allowed_domains = ['gmc.org.cn']
    start_urls = ['http://www.gmc.org.cn/mineral.html',
                  'http://www.gmc.org.cn/fossil.html',
                  'http://www.gmc.org.cn/gemandjade.html',
                  'http://www.gmc.org.cn/other.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//div[@class='clist clear']/div[@class='li']")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 2
            item["museumName"] = "中国地质博物馆"
            url = 'http://www.gmc.org.cn' + li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionName'] = response.xpath("//div[@class='r']/div[@class='t28']/text()").extract_first()
        item['collectionImageLink'] = 'http://www.gmc.org.cn' + str(
            response.xpath("//div[@class='limg']/img/@src").extract_first())
        p_list = response.xpath("//div[@class='r']/div[@class='con']/div[@class='p']/p")
        content = ''
        for p in p_list:
            content += p.xpath("./text()").extract_first()
        item['collectionIntroduction'] = StrFilter.filter(content).replace('[', '').replace(']', '')
        print(item)
        yield item
