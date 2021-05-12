#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:10
# @Author  : 10711
# @File    : Exhibition193.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition193_supporting

class Exhibition193(scrapy.Spider):
    name = "Exhibition193"
    allowed_domains = ['gansumuseum.com']
    start_urls = Exhibition193_supporting.Exhibition193Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 193
            item["museumName"] = "甘肃省博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./div/a/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div/div/div[1]/label").xpath('string(.)').extract_first())
            item["exhibitionTime"] = "常设展览"
            item['exhibitionIntroduction'] = StrFilter.filter(
                li.xpath("./div/div/div[2]/p").xpath('string(.)').extract_first())
            print(item)
            yield item