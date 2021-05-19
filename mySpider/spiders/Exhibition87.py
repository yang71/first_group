#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition87.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition87_supporting

class Exhibition87(scrapy.Spider):
    name = "Exhibition87"
    allowed_domains = ['ahbbmuseum.com']
    start_urls = Exhibition87_supporting.Exhibition87Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='lists']/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 87
            item["museumName"] = "蚌埠市博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./h1/a").xpath('string(.)').extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./h1/span").xpath('string(.)').extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
            response.xpath("//*[@id='hl_content']/div[2]/div[2]/p[2]/span/img/@src").extract_first())
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='hl_content']/div[2]/div[2]").xpath('string(.)').extract_first())

        print(item)
        yield item