#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 15:38 
# @Author  : ana
# @File    : Collection22.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection22(scrapy.Spider):
    name = "Collection22"
    allowed_domains = ['bwy.hbdjdz.com']
    start_urls = ['http://bwy.hbdjdz.com/html/second.html?id=1']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[3]/table/tbody/tr[2]")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 22
            item["museumName"] = "河北博物院"
            url = "https://www.tjnhm.com/" + str(li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionName'] = response.xpath("//*[@id='aboutus_text']/h1/text()").extract_first()
        if response.xpath(
                "//*[@id='aboutus_text']/p[1]/span/img/@src").extract_first() is not None:
            item['collectionImageLink'] = 'https://www.tjnhm.com/' + str(response.xpath(
                "//*[@id='aboutus_text']/p[1]/span/img/@src").extract_first())
        else:
            item['collectionImageLink'] = None

        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='aboutus_text']/span").xpath('string(.)').extract_first()).replace('[', '').replace(
            ']', '')
        print(item)
        yield item
