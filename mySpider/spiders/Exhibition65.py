#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition65.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition65_supporting

class Exhibition65(scrapy.Spider):
    name = "Exhibition65"
    allowed_domains = ['wxmuseum.com']
    start_urls = Exhibition65_supporting.Exhibition65Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[5]/div/div/div/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 65
            item["museumName"] = "无锡博物院"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./a[2]/h2").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./a[1]/i/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./a[2]/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[5]/div/div/div/div[2]/div[2]").xpath('string(.)').extract_first())
        item["exhibitionTime"] = StrFilter.filter(
            response.xpath("/html/body/div[5]/div/div/div/div[2]/div[1]/span[1]").xpath('string(.)').extract_first())
        print(item)
        yield item