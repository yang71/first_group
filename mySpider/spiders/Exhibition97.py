#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition97.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition97_supporting

class Exhibition97(scrapy.Spider):
    name = "Exhibition97"
    allowed_domains = ['aymuseum.com']
    start_urls = Exhibition97_supporting.Exhibition97Supporting.startUrl

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
            item["museumID"] = 97
            item["museumName"] = "安源路矿工人运动纪念馆"
            item["exhibitionName"] = StrFilter.filter(
                response.xpath("//*[@id='module12']/div/div/div/div/h1").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                response.xpath("//*[@id='module12']/div/div/div/div/div[2]/p[1]/span/img[1]/@src").extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter(
                response.xpath("//*[@id='module12']/div/div/div/div/div[2]").xpath('string(.)').extract_first())
            item["exhibitionTime"] = "常设展览"
            print(item)
            yield item