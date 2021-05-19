#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition73.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition73_supporting

class Exhibition73(scrapy.Spider):
    name = "Exhibition73"
    allowed_domains = ['hzmuseum.com']
    start_urls = Exhibition73_supporting.Exhibition73Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition11Middleware': 65543,
        },
    }


    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='app']/div[2]/div/ul/li")
       # print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 73
            item["museumName"] = "南京市博物总馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div/p[2]").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./img/@src").extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter(
                li.xpath("./div/p[3]").xpath('string(.)').extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./div/p[1]").xpath('string(.)').extract_first())
