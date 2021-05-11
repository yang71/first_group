#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 17:49 
# @Author  : ana
# @File    : Exhibition12.py
# @Software: PyCharm


from ..items import *
from ..auxiliary_files import Exhibition12_supporting


class Exhibition12(scrapy.Spider):
    name = "Exhibition12"
    allowed_domains = ['bjp.org.cn']
    start_urls = ['http://www.bjp.org.cn/cgzn/twzl/list.shtml']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        for i in Exhibition12_supporting.Exhibition12Supporting.values:
            item = ExhibitionItem()
            item["museumID"] = 12
            item["museumName"] = "北京天文馆"
            item["exhibitionImageLink"] = i[0]
            item["exhibitionName"] = i[1]
            item["exhibitionTime"] = "常设展览"
            item['exhibitionIntroduction'] = None
            print(item)
            yield item
