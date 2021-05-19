#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition86.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition86_supporting

class Exhibition86(scrapy.Spider):
    name = "Exhibition86"
    allowed_domains = ['sz-museum.com']
    start_urls = Exhibition86_supporting.Exhibition86Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[1]/div[4]/div/div/div[2]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 86
            item["museumName"] = "宿州市博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./h4/a").xpath('string(.)').extract_first())

            url = StrFilter.getDoamin(response) + str(
                li.xpath("./h4/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
            response.xpath("/html/body/div[1]/div[4]/div/div/div[2]/div[2]/p[2]/img/@src").extract_first())
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[1]/div[4]/div/div/div[2]/div[2]").xpath('string(.)').extract_first())
        item["exhibitionTime"] = StrFilter.filter(
            response.xpath("/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[2]/p[6]").xpath('string(.)').extract_first())
        print(item)
        yield item