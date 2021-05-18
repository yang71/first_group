#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition136.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition136_supporting

class Exhibition136(scrapy.Spider):
    name = "Exhibition136"
    allowed_domains = ['changjiangcp.com']
    start_urls = Exhibition136_supporting.Exhibition136Supporting.startUrl

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
            item["museumID"] = 136
            item["museumName"] = "南京市博物总馆"
            item["exhibitionName"] = StrFilter.filter(
                response.xpath("/html/body/div[5]/div/div[1]/div/div[1]").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                response.xpath("//*[@id='form']/div[3]/div[2]/div/div[1]/img/@src").extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter(
                response.xpath("/html/body/div[5]/div/div[1]/div").xpath('string(.)').extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                response.xpath("/html/body/div[5]/div/div[1]/div").xpath('string(.)').extract_first())
            print(item)
            yield item