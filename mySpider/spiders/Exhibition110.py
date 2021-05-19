#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition110.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition110_supporting

class Exhibition110(scrapy.Spider):
    name = "Exhibition110"
    allowed_domains = ['kzbwg.cn']
    start_urls = Exhibition110_supporting.Exhibition110Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[6]/div/div/div[3]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 110
            item["museumName"] = "孔子博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div/h3/a").xpath('string(.)').extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./div/span").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./a/img/@src").extract_first())

            item['exhibitionIntroduction'] = StrFilter.filter(
                li.xpath("./div/p").xpath('string(.)').extract_first())

            print(item)
            yield item