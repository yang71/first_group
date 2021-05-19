#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition122.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition122_supporting

class Exhibition122(scrapy.Spider):
    name = "Exhibition122"
    allowed_domains = ['chnmus.net']
    start_urls = Exhibition122_supporting.Exhibition122Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='articleListTable']/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 122
            item["museumName"] = "河南博物院"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./a/h5").xpath('string(.)').extract_first())
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
            response.xpath("/html/body").xpath('string(.)').extract_first())
        item["exhibitionTime"] = "临时展览"
        print(item)
        yield item