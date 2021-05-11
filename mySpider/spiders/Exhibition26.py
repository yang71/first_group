#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 22:50 
# @Author  : ana
# @File    : Exhibition26.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *


class Exhibition26(scrapy.Spider):
    name = "Exhibition26"
    allowed_domains = ['coalmus.org.cn']
    start_urls = ['http://www.coalmus.org.cn/html/list_1613.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='wrap']/div[2]/div[2]/ul/li[position()>1]")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 26
            item["museumName"] = "中国煤炭博物馆"
            item["exhibitionImageLink"] = str(li.xpath("./div[1]/a/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./div[1]/a/img/@alt").extract_first())
            item["exhibitionTime"] = "常设展览"
            url = str(li.xpath("./div[1]/a/@href").extract_first())
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = None
        print(item)
        yield item
