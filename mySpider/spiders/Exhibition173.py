#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 20:10
# @Author  : 10711
# @File    : Exhibition173.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition173_supporting

class Exhibition173(scrapy.Spider):
    name = "Exhibition173"
    allowed_domains = ['gzmuseum.com']
    start_urls = Exhibition173_supporting.Exhibition173Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@class='bd']/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 173
            item["museumName"] = "贵州省博物馆"
            item["exhibitionImageLink"] = str(
                li.xpath("./div[2]/a/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div[1]/h2/a/@title").extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./div[1]/div/p[1]").xpath('string(.)').extract_first()) + ' ' + StrFilter.filter(
                li.xpath("./div[1]/div/p[2]").xpath('string(.)').extract_first())
            url = str(
                li.xpath("./div[1]/h2/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='Zoom']/div").xpath('string(.)').extract_first())[:500] + "..."
        print(item)
        yield item