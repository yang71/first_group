#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition74.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition74_supporting

class Exhibition74(scrapy.Spider):
    name = "Exhibition74"
    allowed_domains = ['wzmuseum.cn']
    start_urls = Exhibition74_supporting.Exhibition74Supporting.startUrl

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
            item["museumID"] = 74
            item["museumName"] = "温州博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./a/div/div").xpath('string(.)').extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./a/div/p[1]").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./a/img/@src").extract_first())
            url = StrFilter.filter(
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
            response.xpath("/html/body/div/div[4]/div[2]/div[2]").xpath('string(.)').extract_first())
        print(item)
        yield item