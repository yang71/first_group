#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition190.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition190_supporting


class Exhibition190(scrapy.Spider):
    name = "Exhibition190"
    allowed_domains = ['xabwy.com']
    start_urls = Exhibition190_supporting.Exhibition190Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        for value in Exhibition190_supporting.Exhibition190Supporting.values:
            item = ExhibitionItem()
            item["museumID"] = 190
            item["museumName"] = "西安博物院"
            item["exhibitionImageLink"] = value.get("exhibitionImageLink")
            item["exhibitionName"] = value.get("exhibitionName")
            item["exhibitionTime"] = "常设展览"
            item['exhibitionIntroduction'] = value.get("exhibitionIntroduction")
            print(item)
            yield item