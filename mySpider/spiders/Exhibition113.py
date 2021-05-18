#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition113.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition113_supporting

class Exhibition113(scrapy.Spider):
    name = "Exhibition113"
    allowed_domains = ['museum.sdu.edu.cn']
    start_urls = Exhibition113_supporting.Exhibition113Supporting.startUrl

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
            item["museumID"] = 113
            item["museumName"] = "山东大学博物馆"
            item["exhibitionName"] = StrFilter.filter(
                response.xpath("/html/body/div[2]/div[2]/form/div[1]").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                response.xpath("//*[@id='85FFFFAH']/@src").extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter(
                response.xpath("//*[@id='vsb_content']/div").xpath('string(.)').extract_first())
            item["exhibitionTime"] ="专题展览"
            print(item)
            yield item