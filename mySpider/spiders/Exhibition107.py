#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition107.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition107_supporting

class Exhibition107(scrapy.Spider):
    name = "Exhibition107"
    allowed_domains = ['sdmuseum.com']
    start_urls = Exhibition107_supporting.Exhibition107Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 107
            item["museumName"] = "山东博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div[2]/div[1]/a").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./div[1]/a/img/@src").extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter(
                li.xpath("./div[2]/div[2]/a").xpath('string(.)').extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./div[2]/div[3]").xpath('string(.)').extract_first())
            print(item)
            yield item