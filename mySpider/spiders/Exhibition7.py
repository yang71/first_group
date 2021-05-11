#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 15:19 
# @Author  : ana
# @File    : Exhibition7.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition7_supporting


class Exhibition7(scrapy.Spider):
    name = "Exhibition7"
    allowed_domains = ['bmnh.org.cn']
    start_urls = Exhibition7_supporting.Exhibition7Supporting.startUrl

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
        item["museumID"] = 7
        item["museumName"] = "北京自然博物馆"
        item["exhibitionImageLink"] = StrFilter.getDoamin(response) + response.xpath(
            "//div[@class='single_block']//img/@src").extract_first()
        item["exhibitionName"] = StrFilter.filter_2(response.xpath("//p[@class='single_title']/text()").extract_first())
        item["exhibitionTime"] = "常设展览"
        item['exhibitionIntroduction'] = StrFilter.filter_2(
            response.xpath("//div[@class='single_block']").xpath('string(.)').extract_first())
        print(item)
        yield item
