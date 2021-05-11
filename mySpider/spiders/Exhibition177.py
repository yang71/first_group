#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 20:10
# @Author  : 10711
# @File    : Exhibition177.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition177_supporting

class Exhibition177(scrapy.Spider):
    name = "Exhibition177"
    allowed_domains = ['ynnmuseum.cn']
    start_urls = Exhibition177_supporting.Exhibition177Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='datalist']/div[1]/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 177
            item["museumName"] = "云南民族博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./div[1]/a/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div[2]/div[1]/a").xpath('string(.)').extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./div[2]/div[3]").xpath('string(.)').extract_first()).replace("时间：","")
            item['exhibitionIntroduction'] = StrFilter.filter(
                li.xpath("./div[2]/div[2]").xpath('string(.)').extract_first())
            print(item)
            yield item