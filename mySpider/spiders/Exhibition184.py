#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 15:44
# @Author  : 10711
# @File    : Exhibition184.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition184_supporting

class Exhibition184(scrapy.Spider):
    name = "Exhibition184"
    allowed_domains = ['sxhm.com']
    start_urls = Exhibition184_supporting.Exhibition184Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 184
            item["museumName"] = "陕西历史博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + '/' + str(
                li.xpath("./a/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./a/span").xpath('string(.)').extract_first())
            item["exhibitionTime"] = "常设展览"
            url = str(
                li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[3]/div[2]/div[2]/div[3]").xpath('string(.)').extract_first())
        print(item)
        yield item