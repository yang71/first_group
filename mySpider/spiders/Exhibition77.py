#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition77.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition77_supporting


class Exhibition77(scrapy.Spider):
    name = "Exhibition77"
    allowed_domains = ['zgdjss.com']
    start_urls = Exhibition77_supporting.Exhibition77Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition11Middleware': 65544,
        },
    }

    def parse(self, response, **kwargs):
            item = ExhibitionItem()
            item["museumID"] = 77
            item["museumName"] = "杭州工艺美术博物馆"
            item["exhibitionName"] = StrFilter.filter(
                response.xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/h2").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                response.xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/p[1]/span/img/@src").extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter(
                response.xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div[2]").xpath('string(.)').extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                response.xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/p[3]").xpath('string(.)').extract_first())
