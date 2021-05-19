#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition121.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition121_supporting

class Exhibition121(scrapy.Spider):
    name = "Exhibition121"
    allowed_domains = ['museum.linyi.cn']
    start_urls = Exhibition121_supporting.Exhibition121Supporting.startUrl

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
            item["museumID"] = 121
            item["museumName"] = "临沂市博物馆"
            item["exhibitionName"] = StrFilter.filter(
                response.xpath("//*[@id='index_con']/div/div[2]/form").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                response.xpath("//*[@id='vsb_content_2']/div/p[1]/img/@src").extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter(
                response.xpath("//*[@id='vsb_content_2']/div").xpath('string(.)').extract_first())
            item["exhibitionTime"] = "临时展览"
            print(item)
            yield item