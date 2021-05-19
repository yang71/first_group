#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition108.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition108_supporting

class Exhibition108(scrapy.Spider):
    name = "Exhibition108"
    allowed_domains = ['ytmuseum.com']
    start_urls = Exhibition108_supporting.Exhibition108Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='MainLeft']/div[4]/div/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 108
            item["museumName"] = "烟台市博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div[2]/a").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./div[1]/a/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./div[2]/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='MainLeft']/div[4]/div[1]/table").xpath('string(.)').extract_first())
        item["exhibitionTime"] = "临时展览"
        print(item)
        yield item