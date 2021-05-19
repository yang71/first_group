#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition82.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition82_supporting

class Exhibition82(scrapy.Spider):
    name = "Exhibition82"
    allowed_domains = ['ahm.cn']
    start_urls = Exhibition82_supporting.Exhibition82Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='zltj']/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 82
            item["museumName"] = "安徽省博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div/a/h3").xpath('string(.)').extract_first())
            item["exhibitionTime"] = StrFilter.filter(
               li.xpath("./div/p[1]").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.filter(
                li.xpath("./a/div/img/@src").extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter(
                li.xpath("./div/p[4]").xpath('string(.)').extract_first())

            print(item)
            yield item