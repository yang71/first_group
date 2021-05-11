#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 20:10
# @Author  : 10711
# @File    : Exhibition178.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition178_supporting

class Exhibition178(scrapy.Spider):
    name = "Exhibition178"
    allowed_domains = ['3gmuseum.cn']
    start_urls = Exhibition178_supporting.Exhibition178Supporting.startUrl

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
        item["museumID"] = 178
        item["museumName"] = "重庆中国三峡博物馆"
        item["exhibitionImageLink"] = str(
            response.xpath("//*[@id='js-article-one-info-content']/*/img/@src").extract_first())
        item["exhibitionName"] = StrFilter.filter(
            response.xpath("//*[@id='js-article-one-info-title']").xpath('string(.)').extract_first())
        item["exhibitionTime"] = StrFilter.filter(
            response.xpath("//*[@id='js-article-one-info-content']/p[1]").xpath('string(.)').extract_first()).replace("展览时间：", "")
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='js-article-one-info-content']").xpath('string(.)').extract_first())
        print(item)
        yield item