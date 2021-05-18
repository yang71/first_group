#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:06
# @Author  : 10711
# @File    : ExhibitionXXX.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import ExhibitionXXX_supporting


class ExhibitionXXX(scrapy.Spider):
    name = "ExhibitionXXX"
    allowed_domains = ['']
    start_urls = ExhibitionXXX_supporting.ExhibitionXXXSupporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = XXX
            item["museumName"] = ""
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("").extract_first())
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("").xpath('string(.)').extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("").xpath('string(.)').extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("").xpath('string(.)').extract_first())
        print(item)
        #yield item