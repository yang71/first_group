#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition120.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition120_supporting

class Exhibition120(scrapy.Spider):
    name = "Exhibition120"
    allowed_domains = ['jiningmuseum.com']
    start_urls = Exhibition120_supporting.Exhibition120Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div[1]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 120
            item["museumName"] = "济宁市博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./a/div[2]/h3").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./a/div[1]/img/@src").extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./a/div[2]/p").xpath('string(.)').extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='gs-all']/dl").xpath('string(.)').extract_first())

        print(item)
        yield item