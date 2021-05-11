#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 13:47
# @Author  : 10711
# @File    : Exhibition198.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition198_supporting

class Exhibition198(scrapy.Spider):
    name = "Exhibition198"
    allowed_domains = ['nxbwg.com']
    start_urls = Exhibition198_supporting.Exhibition198Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='content-container']/div[2]/div[2]/main/div/div/div/article")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 198
            item["museumName"] = "宁夏回族自治区博物馆"
            item["exhibitionImageLink"] = str(
                li.xpath("./div[2]/div[1]/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div[1]/h3/a").xpath('string(.)').extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./div[1]/span").xpath('string(.)').extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter(
                li.xpath("./div[2]/div[2]").xpath('string(.)').extract_first())
            print(item)
            yield item