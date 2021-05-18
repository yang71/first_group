#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition88.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition88_supporting

class Exhibition88(scrapy.Spider):
    name = "Exhibition88"
    allowed_domains = ['fjbwy.com']
    start_urls = Exhibition88_supporting.Exhibition88Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 88
            item["museumName"] = "福建博物院"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div[2]/div[2]/span").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./div[1]/a/img/@src").extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./div[2]/div[2]").xpath('string(.)').extract_first())
            url = StrFilter.filter(
                li.xpath("./div[1]/a/@href").extract_first())
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[4]/div/div[4]/div[1]").xpath('string(.)').extract_first())

        print(item)
        yield item