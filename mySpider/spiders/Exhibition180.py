#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 15:44
# @Author  : 10711
# @File    : Exhibition180.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition180_supporting

class Exhibition180(scrapy.Spider):
    name = "Exhibition180"
    allowed_domains = ['cmnh.org.cn']
    start_urls = Exhibition180_supporting.Exhibition180Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[2]/div[3]/div[1]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 180
            item["museumName"] = "重庆自然博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./div/p/a/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div/p/a/@title").extract_first())
            item["exhibitionTime"] = "常设展览"
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./div/p/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[2]/div[3]/div/div[2]").xpath('string(.)').extract_first())
        print(item)
        yield item