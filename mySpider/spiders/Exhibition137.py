#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition137.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition137_supporting

class Exhibition137(scrapy.Spider):
    name = "Exhibition137"
    allowed_domains = ['ycbwg.com']
    start_urls = Exhibition137_supporting.Exhibition137Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div/div[1]/div[3]/div/div[2]/div[3]/div/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 137
            item["museumName"] = "宜昌博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div[2]/a/h5").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
               li.xpath("./div[1]/a/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./div[2]/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div/div[1]/div[3]/div/div[2]/div[3]/div").xpath('string(.)').extract_first())
        item["exhibitionTime"] = "临时展览"
        print(item)
        yield item