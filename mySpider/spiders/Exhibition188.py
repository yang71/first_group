#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 15:44
# @Author  : 10711
# @File    : Exhibition188.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition188_supporting

class Exhibition188(scrapy.Spider):
    name = "Exhibition188"
    allowed_domains = ['beilin-museum.com']
    start_urls = Exhibition188_supporting.Exhibition188Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[5]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 188
            item["museumName"] = "西安碑林博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./a/div/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./a/p").xpath('string(.)').extract_first())
            item["exhibitionTime"] = "常设展览"
            item['exhibitionIntroduction'] = "暂无"
            print(item)
            yield item