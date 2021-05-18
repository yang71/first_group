#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 19:00 
# @Author  : ana
# @File    : Exhibition16.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Exhibition16(scrapy.Spider):
    name = "Exhibition16"
    allowed_domains = ['automuseum.org.cn']
    start_urls = ['http://www.automuseum.org.cn/ZLJS/CSZL/CZG/list.html?/ZLJS/CSZL/CZG/',
                  'http://www.automuseum.org.cn/ZLJS/CSZL/JBG/list.html?/ZLJS/CSZL/JBG/',
                  'http://www.automuseum.org.cn/ZLJS/CSZL/WLG/list.html?/ZLJS/CSZL/WLG/', ]

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
        item["museumID"] = 16
        item["museumName"] = "北京汽车博物馆"
        item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(response.xpath(
            "//div/a/img/@src").extract_first())
        item["exhibitionName"] = StrFilter.filter_2(
            response.xpath("/html/body/div[2]/div[2]/div[2]/div[3]/table//tr[1]/td/span").xpath(
                'string(.)').extract_first())
        item["exhibitionTime"] = "常设展览"
        item['exhibitionIntroduction'] = StrFilter.filter_2(
            response.xpath("//td[@class='wz']").xpath('string(.)').extract_first())
        print(item)
        yield item
