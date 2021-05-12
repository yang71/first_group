#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:10
# @Author  : 10711
# @File    : Exhibition194.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition194_supporting

class Exhibition194(scrapy.Spider):
    name = "Exhibition194"
    allowed_domains = ['tssbwg.com.cn']
    start_urls = Exhibition194_supporting.Exhibition194Supporting.startUrl

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
        item["museumID"] = 194
        item["museumName"] = "天水市博物馆"
        item["exhibitionImageLink"] = str(
            response.xpath("//*[@valign='top']/span/*/img/@src").extract_first())
        item["exhibitionName"] = StrFilter.filter(
            response.xpath("//*[@class='STYLE55']").xpath('string(.)').extract_first())
        item["exhibitionTime"] = "常设展览"
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@class='STYLE56']").xpath('string(.)').extract_first())
        print(item)
        yield item