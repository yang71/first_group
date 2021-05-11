#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:10
# @Author  : 10711
# @File    : Exhibition196.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition196_supporting

class Exhibition196(scrapy.Spider):
    name = "Exhibition196"
    allowed_domains = ['']
    start_urls = Exhibition196_supporting.Exhibition196Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 196
            item["museumName"] = "平凉市博物馆"
            item["exhibitionImageLink"] = str(
                li.xpath("./a/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./h2").xpath('string(.)').extract_first())
            item["exhibitionTime"] = "常设展览"
            item['exhibitionIntroduction'] = StrFilter.filter(
                li.xpath("./a/p").xpath('string(.)').extract_first())
            print(item)
            yield item