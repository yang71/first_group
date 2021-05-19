#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition60.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition60_supporting

class Exhibition60(scrapy.Spider):
    name = "Exhibition60"
    allowed_domains = ['yzmuseum.com']
    start_urls = Exhibition60_supporting.Exhibition60Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
            item = ExhibitionItem()
            item["museumID"] = 60
            item["museumName"] = "扬州博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                response.xpath("//*[@id='content_body']/div/*/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter(
                response.xpath("//*[@id='content_body']/p[1]").xpath('string(.)').extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                response.xpath("//*[@id='content_body']/p[2]").xpath('string(.)').extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter(
                response.xpath("//*[@id='content_body']/div").xpath('string(.)').extract_first())
            print(item)
            yield item