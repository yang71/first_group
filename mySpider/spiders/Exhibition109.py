#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition109.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition109_supporting

class Exhibition109(scrapy.Spider):
    name = "Exhibition109"
    allowed_domains = ['wfsbwg.com']
    start_urls = Exhibition109_supporting.Exhibition109Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='productlist']/div[1]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 109
            item["museumName"] = "潍坊市博物馆"

            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./div/a/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./div/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["exhibitionName"] = StrFilter.filter(
            response.xpath("//*[@id='showproduct']/h1").xpath('string(.)').extract_first())
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='metbox']").xpath('string(.)').extract_first())
        item["exhibitionTime"] = "临时展览"
        print(item)
        yield item