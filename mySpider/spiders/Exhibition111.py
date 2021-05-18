#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition111.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition111_supporting

class Exhibition111(scrapy.Spider):
    name = "Exhibition111"
    allowed_domains = ['jnmuseum.com']
    start_urls = Exhibition111_supporting.Exhibition111Supporting.startUrl

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
            item["museumID"] = 111
            item["museumName"] = "济南市博物馆"
            item["exhibitionName"] = StrFilter.filter(
                response.xpath("//*[@id='app']/div[2]/div/div[2]/div/div[1]/div[1]").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                response.xpath("//*[@id='app']/div[2]/div/div[2]/div/div[1]/div[4]/img/@src").extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter(
                response.xpath("//*[@id='app']/div[2]/div/div[2]/div/div[2]").xpath('string(.)').extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                response.xpath("//*[@id='app']/div[2]/div/div[2]/div/div[1]/div[2]/p[1]").xpath('string(.)').extract_first())
            print(item)
            yield item