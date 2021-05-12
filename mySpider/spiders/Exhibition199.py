#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 13:04
# @Author  : 10711
# @File    : Exhibition199.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition199_supporting


class Exhibition199(scrapy.Spider):
    name = "Exhibition199"
    allowed_domains = ['baike.baidu.com']
    start_urls = Exhibition199_supporting.Exhibition199Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div")
        print(len(li_list))
        for index in range(31, 37, 3):
            item = ExhibitionItem()
            item["museumID"] = 199
            item["museumName"] = "青海省博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li_list[index+2].xpath("./div/a/@href").extract_first())
            item["exhibitionName"] = StrFilter.filter(
                li_list[index].xpath("./b").xpath('string(.)').extract_first())
            item["exhibitionTime"] = "常设展览"
            item['exhibitionIntroduction'] = StrFilter.filter(
                li_list[index+1].xpath(".").xpath('string(.)').extract_first())
            print(item)
            yield item