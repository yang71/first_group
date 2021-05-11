#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 13:58 
# @Author  : ana
# @File    : Collection19.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection19_supporting


class Collection19(scrapy.Spider):
    name = "Collection19"
    allowed_domains = ['tjnhm.com']
    start_urls = Collection19_supporting.Collection19Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='news_content']/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 19
            item["museumName"] = "天津自然博物馆"
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
