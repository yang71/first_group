#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition139.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition139_supporting

class Exhibition139(scrapy.Spider):
    name = "Exhibition139"
    allowed_domains = ['hnmuseum.com']
    start_urls = Exhibition139_supporting.Exhibition139Supporting.startUrl

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
            item["museumID"] = 139
            item["museumName"] = "湖南省博物馆"
            item["exhibitionName"] = StrFilter.filter(
                response.xpath("//*[@id='node-850']/div/div/div/div/div[2]/div[2]/h3").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                response.xpath("//*[@id='node-850']/div/div/div/div/div[2]/div[1]/img/@src").extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter(
                response.xpath("//*[@id='node-850']/div/div/div/div/div[2]/div[2]/p").xpath('string(.)').extract_first())
            item["exhibitionTime"] = "临时展览"
            print(item)
            yield item