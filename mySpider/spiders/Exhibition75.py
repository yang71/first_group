#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition75.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition75_supporting

class Exhibition75(scrapy.Spider):
    name = "Exhibition75"
    allowed_domains = ['westlakemuseum.com']
    start_urls = Exhibition75_supporting.Exhibition75Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='adminForm']/table/tbody/tr")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 75
            item["museumName"] = "杭州西湖博物馆总馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./td[1]/a").xpath('string(.)').extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./td[2]").xpath('string(.)').extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./td[1]/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["exhibitionImageLink"] = "NULL"
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='main']/div[3]").xpath('string(.)').extract_first())

        print(item)
        yield item