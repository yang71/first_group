#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 20:10
# @Author  : 10711
# @File    : Exhibition179.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition179_supporting

class Exhibition179(scrapy.Spider):
    name = "Exhibition179"
    allowed_domains = ['hongyan.info']
    start_urls = Exhibition179_supporting.Exhibition179Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@class='exhibit-item']")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 179
            item["museumName"] = "重庆红岩革命历史博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./div[1]/a/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div[2]/h2").xpath('string(.)').extract_first())
            item["exhibitionTime"] = "常设展览"
            item['exhibitionIntroduction'] = StrFilter.filter(
                li.xpath("./div[2]/p").xpath('string(.)').extract_first())
            print(item)
            yield item