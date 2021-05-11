#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 15:44
# @Author  : 10711
# @File    : Exhibition185.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition185_supporting

class Exhibition185(scrapy.Spider):
    name = "Exhibition185"
    allowed_domains = ['bmy.com.cn']
    start_urls = Exhibition185_supporting.Exhibition185Supporting.startUrl

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
        item["museumID"] = 185
        item["museumName"] = "秦始皇兵马俑博物馆"
        item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
            response.xpath("/html/body/div[2]/div[4]/*/img/@src").extract_first())
        item["exhibitionName"] = StrFilter.filter(
            response.xpath("/html/body/div[2]/div[3]/b").xpath('string(.)').extract_first())
        item["exhibitionTime"] = "常设展览"
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[2]/div[4]").xpath('string(.)').extract_first())
        print(item)
        yield item