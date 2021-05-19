#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition123.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition123_supporting

class Exhibition123(scrapy.Spider):
    name = "Exhibition123"
    allowed_domains = ['hnzzmuseum.com']
    start_urls = Exhibition123_supporting.Exhibition123Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[4]/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 123
            item["museumName"] = "郑州博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./ul/li/a/p[1]").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./ul/img/@src").extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./ul/li/a/p[2]").xpath('string(.)').extract_first())

            url = StrFilter.getDoamin(response) + str(
                li.xpath("./ul/li/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[4]/ul/div[2]/li[2]").xpath('string(.)').extract_first())
        print(item)
        yield item