#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition127.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition127_supporting

class Exhibition127(scrapy.Spider):
    name = "Exhibition127"
    allowed_domains = ['eywsqsfbwg.com']
    start_urls = Exhibition127_supporting.Exhibition127Supporting.startUrl

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
            item["museumID"] = 127
            item["museumName"] = "鄂豫皖苏区首府革命博物馆"
            item["exhibitionName"] = StrFilter.filter(
                response.xpath("/html/body/div[4]/div[2]/div/h2").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                response.xpath("//*[@id='conbox']/p[1]/img/@src").extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter(
                response.xpath("//*[@id='conbox']/p[1]").xpath('string(.)').extract_first())
            t = StrFilter.filter(
                response.xpath("/html/body/div[4]/div[2]/div/p").xpath('string(.)').extract_first())
            t1 = t.replace('发布时间：', '')
            item["exhibitionTime"] = t1
            print(item)
            yield item