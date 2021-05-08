#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 14:49 
# @Author  : ana
# @File    : Exhibition5.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *


class Exhibition5(scrapy.Spider):
    name = "Exhibition5"
    allowed_domains = ['luxunmuseum.com.cn']
    start_urls = ['http://www.luxunmuseum.com.cn/zuixinzhanlan/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div[2]/div[1]/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 5
            item["museumName"] = "北京鲁迅博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + li.xpath(
                "./div[1]/a/img/@src").extract_first()
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./div[2]/dt/a/text()").extract_first())
            item["exhibitionTime"] = "见详细介绍"
            item['exhibitionIntroduction'] = StrFilter.filter_2(
                li.xpath("./div[2]/dd/text()").extract_first())
            # url = StrFilter.getDoamin(response) + str(li.xpath("./div[1]/a/@href").extract_first())
            print(item)
            yield item
