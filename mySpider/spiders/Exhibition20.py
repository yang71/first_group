#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 19:50 
# @Author  : ana
# @File    : Exhibition20.py
# @Software: PyCharm


from ..items import *
from ..auxiliary_files import Exhibition20_supporting


class Exhibition20(scrapy.Spider):
    name = "Exhibition20"
    allowed_domains = ['mzhoudeng.com']
    start_urls = ['http://www.mzhoudeng.com/exhibits.aspx?cateid=86']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        for i in Exhibition20_supporting.Exhibition20Supporting.values:
            item = ExhibitionItem()
            item["museumID"] = 20
            item["museumName"] = "周恩来邓颖超纪念馆"
            item["exhibitionImageLink"] = i[0]
            item["exhibitionName"] = i[1]
            item["exhibitionTime"] = "常设展览"
            item['exhibitionIntroduction'] = i[2]
            print(item)
            yield item
