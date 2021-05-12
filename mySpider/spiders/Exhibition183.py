#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 15:44
# @Author  : 10711
# @File    : Exhibition183.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition183_supporting

class Exhibition183(scrapy.Spider):
    name = "Exhibition183"
    allowed_domains = ['tibetmuseum.com.cn']
    start_urls = Exhibition183_supporting.Exhibition183Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        for value in Exhibition183_supporting.Exhibition183Supporting.values:
            item = ExhibitionItem()
            item["museumID"] = 183
            item["museumName"] = "西藏博物馆"
            item["exhibitionImageLink"] = value["exhibitionImageLink"]
            item["exhibitionName"] = value["exhibitionName"]
            item["exhibitionTime"] = value["exhibitionTime"]
            item['exhibitionIntroduction'] = value["exhibitionIntroduction"]
            print(item)
            yield item