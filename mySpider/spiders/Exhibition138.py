#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition138.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition138_supporting

class Exhibition138(scrapy.Spider):
    name = "Exhibition138"
    allowed_domains = ['szbwg.net']
    start_urls = Exhibition138_supporting.Exhibition138Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div/div[2]/div/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 138
            item["museumName"] = "随州市博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div/a/h2").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("/a/i/img/@src").extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./div/div").xpath('string(.)').extract_first())
            url = StrFilter.filter(
                li.xpath("./div/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='Article']/div[2]").xpath('string(.)').extract_first())

        print(item)
        yield item