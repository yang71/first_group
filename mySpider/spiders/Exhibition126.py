#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition126.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition126_supporting

class Exhibition126(scrapy.Spider):
    name = "Exhibition126"
    allowed_domains = ['kfsbwg.com']
    start_urls = Exhibition126_supporting.Exhibition126Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='list']/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 126
            item["museumName"] = "开封市博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./p[1]").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./div/a/img/@src").extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter(
                li.xpath("./p[4]").xpath('string(.)').extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./p[2]").xpath('string(.)').extract_first())

            print(item)
            yield item