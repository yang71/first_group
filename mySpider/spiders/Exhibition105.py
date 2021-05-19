#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition105.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition105_supporting

class Exhibition105(scrapy.Spider):
    name = "Exhibition105"
    allowed_domains = ['jiawuzhanzheng.org']
    start_urls = Exhibition105_supporting.Exhibition105Supporting.startUrl

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
            item["museumID"] = 105
            item["museumName"] = "中国甲午战争博物馆"
            item["exhibitionName"] = StrFilter.filter(
                response.xpath("//*[@id='gallery']/h1").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                response.xpath("//*[@id='gallery']/div[1]/div[1]/img/@src").extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter(
                response.xpath("//*[@id='gallery']/p[3]").xpath('string(.)').extract_first())
            item["exhibitionTime"] = "常设展览"
            print(item)
            yield item