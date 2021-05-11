#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 20:10
# @Author  : 10711
# @File    : Exhibition176.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition176_supporting

class Exhibition176(scrapy.Spider):
    name = "Exhibition176"
    allowed_domains = ['ynmuseum.org']
    start_urls = Exhibition176_supporting.Exhibition176Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div/div[3]/div[1]/div/div[3]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list[1:]:
            item = ExhibitionItem()
            item["museumID"] = 176
            item["museumName"] = "云南省博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div[3]/div[1]/a").xpath('string(.)').extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./div[3]/div[1]/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div/div[3]/div[1]/div/div[2]").xpath('string(.)').extract_first())
        item["exhibitionTime"] = StrFilter.filter(
            response.xpath("//*[@class='time']").xpath('string(.)').extract_first())
        item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
            response.xpath("/html/body/div/div[3]/div[1]/div/div[2]/*/img/@src").extract_first())
        print(item)
        yield item