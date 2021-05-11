#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 22:34 
# @Author  : ana
# @File    : Exhibition25.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *


class Exhibition25(scrapy.Spider):
    name = "Exhibition25"
    allowed_domains = ['shanximuseum.com']
    start_urls = ['http://www.shanximuseum.com/sx/exhibition/base_sxsoul.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='datalist']/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 25
            item["museumName"] = "山西博物院"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(li.xpath(
                "./div[1]/a/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./div[2]/div[1]/div[1]/a/text()").extract_first())
            item["exhibitionTime"] = "常设展览"
            item['exhibitionIntroduction'] = StrFilter.filter_2(
                li.xpath("./div[2]/div[1]/div[2]").xpath('string(.)').extract_first())
            print(item)
            yield item
