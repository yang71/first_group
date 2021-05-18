#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition103.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition103_supporting

class Exhibition103(scrapy.Spider):
    name = "Exhibition103"
    allowed_domains = ['pxmuseum.com']
    start_urls = Exhibition103_supporting.Exhibition103Supporting.startUrl

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
            item["museumID"] = 103
            item["museumName"] = "萍乡博物馆"
            item["exhibitionName"] = StrFilter.filter(
                response.xpath("//*[@id='module12']/div/div/div/div/h1").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                response.xpath("//*[@id='module12']/div/div/div/div/div[3]/div/p[1]/img/@src").extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter(
                response.xpath("//*[@id='module12']/div/div/div/div/div[3]/div").xpath('string(.)').extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                response.xpath("//*[@id='module12']/div/div/div/div/div[3]/div").xpath('string(.)').extract_first())
            print(item)
            yield item