#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition130.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition130_supporting

class Exhibition130(scrapy.Spider):
    name = "Exhibition130"
    allowed_domains = ['aybwg.org']
    start_urls = Exhibition130_supporting.Exhibition130Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div/div[4]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 130
            item["museumName"] = "安阳博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./a/div/div").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./a/img/@src").extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./a/div/p[1]").xpath('string(.)').extract_first())
            url =  StrFilter.filter(
                li.xpath("./a/@href").extract_first())
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='content']").xpath('string(.)').extract_first())

        print(item)
        yield item